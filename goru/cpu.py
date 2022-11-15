#! /usr/bin/python3
from enum import Enum
import os
import glob
import binascii
import struct
from elftools.elf.elffile import ELFFile

class RegFile:
  def __init__(self):
    self.regs = [0]*33
  def __getitem__(self, key):
    return self.regs[key]
  def __setitem__(self, key, value):
    if key == 0:
      return
    self.regs[key] = value & 0xFFFFFFFF

PC = 32

# RV32I Base Instruction Set
class OPS(Enum):
  # U-Type
  LUI   = 0b0110111
  AUIPC = 0b0010111

  # J-Type
  JAL  =  0b1101111
  JALR =  0b1100111

  # B-Type
  BEQ  = BNE = BLT = BGE = BLTU = BGEU = 0b1100011

  # I-Type
  LB = LBU = LH = LW = LHU = 0b0000011
  ADDI = SLTI = SLTIU = XORI = ORI = ANDI = SLLI = SRLI = SRAI = 0b0010011
  CSRRW = CSRRS = CSRRC = CSRRWI = CSRRSI = CSRRCI = 0b1110011

  # S-Type
  SB = SH = SW = 0b0100011

  # R-Type
  ADD = SUB = SLL = SLT = SLTU = XOR = SRL = SRA = OR = AND = 0b0110011

  # System
  ECALL = EBREAK = 0b1110011

  # NO OPS
  FENCE = 0b0001111

  # END OF PROGRAM
  UNIMP = 0b0

class Funct3(Enum):
  JALR = BEQ = LB = SB = ADDI = ADD = SUB = ECALL = EBREAK = 0b000
  BNE = LH = SH = SLLI = CSRRW = SLL = 0b001
  SW = SLTI = SLT = CSRRS = LW = 0b010
  SLTU = CSRRC = 0b011
  BLT = LBU = XORI = XOR = 0b100
  BGE = LHU = SRLI = SRAI = SRL = SRA = CSRRWI = 0b101
  BLTU = ORI = OR = CSRRSI = 0b110
  BGEU = ANDI = AND = CSRRCI = 0b111

class Funct7(Enum):
  SLLI = SRLI = ADD = SLL = SLT = SLTU = XOR = SRL = OR = AND = ECALL = 0b0000000
  SRAI = SUB = SRA = 0b0100000

# get_bytes
def gb(ins, s,e):
# puts in beginning & right amount of 1111s
  return (ins >> e) & ((1 << (s-e+1))-1)

# load the program into memory
def load_program(addr, data, OFFSET):
  global memory
  addr -= OFFSET
  assert addr >=0 and addr < len(memory)
  memory = memory[:addr] + data + memory[addr+len(data):]

# instruction already shifted right (in to beginning)
# length: size of bit
def sign_extend(ins, length):
  # if most significant bit is 1
  if ins >> (length - 1) == 1:
    # create lots of ones
    aux = ((1 << 32) - ins)

    # or ones with ins
    return (gb(aux, 31,length) << length) | ins
  else:
    return ins 

def fetch(addr):
  addr -= OFFSET

  if addr < 0 or addr >= len(memory):
    raise Exception(f"Read out of Bounds: 0x{addr:02x}")
  return struct.unpack("<I", memory[addr:addr+4])[0]

def decode(ins):
  global f3, f7, rd, rs1, rs2
  global imm_j, imm_b, imm_i, imm_r, imm_s, imm_u
  global shamt_i

  f3, f7 = None, None

  # TODO: make the decode smarter. Currently we are assigning f3,f7 to wrong ops
  op = OPS(gb(ins, 6,0))

  # Funct3
  if op not in (OPS.LUI, OPS.AUIPC, OPS.JAL):
    try:
      f3 = Funct3(gb(ins, 14,12))
    except ValueError:
      f3 = None

  # Funct7
  if op in (OPS.SLLI, OPS.ADD, OPS.ECALL): 
    try:
      f7 = Funct7(gb(ins, 31,25))
    except ValueError:
      f7 = None

  # rd
  if op not in (OPS.BEQ, OPS.SB, OPS.ECALL):
    rd = (gb(ins, 11,7))

  # rs1
  if op not in (OPS.LUI, OPS.AUIPC, OPS.JAL, OPS.ECALL): 
    rs1 = (gb(ins, 19,15))

  # rs2
  if op in (OPS.BEQ, OPS.SB, OPS.ADD):
    rs2 = (gb(ins, 24,20))

  # imm_u
  if op in (OPS.LUI, OPS.AUIPC):
    imm_u = gb(ins, 31,12) << 12

  # imm_j
  if op == OPS.JAL:
    aux = (gb(ins, 19,12) << 12) | (gb(ins,11,11) << 11) | (gb(ins, 30,21) << 1)
    imm_j = sign_extend(aux, 20)

  # imm_i
  if op in (OPS.JALR, OPS.LB, OPS.ADDI, OPS.CSRRW):
    imm_i = sign_extend(gb(ins, 31,20), 12)

  # imm_b
  if op in (OPS.BEQ, OPS.BNE, OPS.BLT, OPS.BGE, OPS.BLTU, OPS.BGEU):
    aux = ( (gb(ins, 30,25) << 5) | (gb(ins, 11,8) << 1) | (gb(ins, 7,7) << 11) )
    imm_b = sign_extend(aux, 12)

  # imm_s
  if op == OPS.SB:
    aux = ( gb(ins, 31,25) << 5 ) | gb(ins, 11,7)
    imm_s = sign_extend(aux, 12)

  # shamt_i
  if op == OPS.ADDI and f3 == Funct3.SLLI:
    shamt_i = gb(ins, 24,20)

  return op

def execute(op):
  global NPC
  NPC = 4
  # ALU INSTRUCTIONS
  if op == OPS.ADD and f7 == Funct7.ADD:
    rf[rd] = rf[rs1] + rf[rs2]
  elif op == OPS.ADD and f7 == Funct7.SUB:
    rf[rd] = rf[rs1] - rf[rs2]
  elif op == OPS.JAL:
    NPC = imm_j
  elif op == OPS.ADDI and f3 == Funct3.ADDI:
    rf[rd] = rf[rs1] + imm_i 
  elif op == OPS.ADDI and f3 == Funct3.SLLI:
    rf[rd] = rf[rs1] << shamt_i
  elif op == OPS.ADDI and f3 == Funct3.ORI:
    rf[rd] = rf[rs1] | imm_i
  elif op == OPS.ADDI and f3 == Funct3.ANDI:
    rf[rd] = rf[rs1] & imm_i
  elif op == OPS.AUIPC:
    rf[rd] = imm_u

  # BRANCH INSTRUCTIONS
  elif op == OPS.BNE and f3 == Funct3.BNE:
      NPC = imm_b + 4 if rf[rs1] != rf[rs2] else 4
  elif op == OPS.BNE and f3 == Funct3.BEQ:
      NPC = imm_b + 4 if rf[rs1] == rf[rs2] else 4
  elif op == OPS.BNE and f3 == Funct3.BLT:
      NPC = imm_b + 4 if rf[rs1] < rf[rs2] else 4
  elif op == OPS.BNE and f3 == Funct3.BGE:
      NPC = imm_b + 4 if rf[rs1] >= rf[rs2] else 4
  elif op == OPS.BNE and f3 == Funct3.BGEU:
      NPC = imm_b + 4 if rf[rs1] >= abs(rf[rs2]) else 4
  elif op == OPS.BNE and f3 == Funct3.BLTU:
      NPC = imm_b + 4 if rf[rs1] <= abs(rf[rs2]) else 4

  # LOAD INSTRUCTIONS
  elif op == OPS.LUI:
    rf[rd] = imm_u

  # System INSTRUCTIONS
  elif op == OPS.FENCE:
    pass
  elif op == OPS.CSRRW and f3 != Funct3.ECALL:
    pass
  elif op == OPS.CSRRW and f3 in (Funct3.ECALL, None):
    END = True
  else:
    state()
    raise Exception(f"Operation {op} not implemented, {f3}, {f7}")

def memget(addr):
  pass

def write_back():
  rf[PC] += NPC 
  return

def state():
  pp = ''
  for i in range(32):
    if i != 0 and i % 8 == 0:
      pp += '\n'
    pp += "%3s: %08x " % ("x%d" % i, rf[i])
  pp += f'\n PC: {rf[PC]:08x} '
  print(''.join(pp))
  print('\n')

def reset():
  global rf, memory, OFFSET
  rf = RegFile()

  # 64k
  memory = b'\x00'*0x10000

  OFFSET=0x80000000

  # Beginning of program
  rf[PC] = OFFSET

def run():

  # Instruction Fetch
  ins = fetch(rf[PC])

  if DEBUG:
    print(f"ins: {bin(ins)}")

  # Instruction Decode and Register Fetch
  op = decode(ins) 

  if DEBUG:
    print(op)
  if op == OPS.UNIMP:
    print(f"SUCCESS!")
    return False

  # Execute
  execute(op)

  # Memory Access
  memget(0)

  # Register Write Back
  write_back() # If is not a branch / jump then add 4

  if DEBUG:
    state()
  
  if END:
    return False
    # if rf[3] > 1:
      # raise Exception("TEST FAILED!")
    # else:
      # return False

  return True

if __name__ == "__main__":

  f3, f7 = None, None
  rs1, rs2, rd = None, None, None
  imm_j, imm_u, imm_b, imm_s, imm_i, imm_r = None, None, None, None, None, None
  shamt_i = None
  counter = 0
  END = False
  DEBUG = os.getenv('DEBUG', 0)

  OFFSET, NPC = 0x0, 0x0

  for x in glob.glob("riscv-tests/isa/rv32ui/*"):
      if x.endswith('.dump') or x.endswith('.S') or x.endswith('Makefrag'):
        continue
      with open(x, 'rb') as f:
        # if DEBUG:
        print(f"Testing file: {x}")

      # Put registers to initial state
        reset()
        e = ELFFile(f)

        for s in e.iter_segments():
          addr, dat = s.header.p_paddr, s.data()
          if addr == 0: continue
          load_program(addr, dat, OFFSET)

        while run():
          counter += 1

        print(f"Ran {counter} instructions")
