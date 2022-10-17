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
NPC = 0

# RV32I Base Instruction Set
class OPS(Enum):
  # U-Type
  LUI   = 0b0110111
  AUIPC = 0b0110111

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
  SLLI = SRLI = ADD = SLL = SLT = SLTU = XOR = SRL = OR = AND = 0b0000000
  SRAI = SUB = SRA = 0b0100000

# load the program into memory
def load_program(addr, data, OFFSET):
  global memory
  addr -= OFFSET
  assert addr >=0 and addr < len(memory)
  memory = memory[:addr] + data + memory[addr+len(data):]


def fetch(addr, OFFSET):
  addr -= OFFSET
  print('aaaa', addr)

  if addr < 0 or addr >= len(memory):
    raise Exception(f"Read out of Bounds:0x{addr:02x}")
  return struct.unpack("<I", memory[addr:addr+4])[0]

# get_bytes
def gb(s,e):
# puts in beginning & right amount of 1111s
  return (ins >> e) & ((1 << (s-e+1))-1)

def decode(ins):
  global f3, f7, rd, rs1, rs2, imm_j
  print(f"Decoding: {bin(ins)}")

  op = OPS(gb(6,0))

  # Funct3
  if op not in (OPS.LUI, OPS.AUIPC, OPS.JAL):
    f3 = Funct3(gb(14,12))

  # Funct7
  if op in (OPS.SLLI, OPS.SRLI, OPS.SRAI, OPS.ADD, OPS.SUB, OPS.SLL, OPS.SLT,
                 OPS.SLTU, OPS.XOR, OPS.SRL, OPS.SRA, OPS.OR, OPS.AND):

    f7 = Funct7(gb(31,25))

  # rd
  if op not in (OPS.BEQ, OPS.BNE, OPS.BLT, OPS.BGE, OPS.BLTU, OPS.BGEU, OPS.SB,
                OPS.SH, OPS.SW, OPS.ECALL, OPS.EBREAK):
    rd = (gb(11,7))

  # rs1
  if op not in (OPS.LUI, OPS.AUIPC, OPS.JAL, OPS.ECALL, OPS.EBREAK, OPS.CSRRWI,
                     OPS.CSRRSI, OPS.CSRRCI):
    rs1 = (gb(19,15))

  # rs2
  if op in (OPS.BEQ, OPS.BNE, OPS.BLT, OPS.BGE, OPS.BLTU, OPS.BGEU, OPS.SB, OPS.SH, OPS.SW,
            OPS.ADD, OPS.SUB, OPS.SLL, OPS.SLT, OPS.SLTU, OPS.XOR, OPS.SRL, OPS.SRA, OPS.OR,
            OPS.AND):
    rs2 = (gb(24,20))

  # immediate values
  # if op == OPS.JAL:
  #   imm_j = ins[-1]*12 << 31
  print(f"OPS: {op.name}")

  return op

def execute(op):
  if op == OPS.ADD and f7 == Funct7.ADD:
    rf[rd] = rs1 + rs2
  elif op == OPS.ADD and f7 == Funct7.SUB:
    rf[rd] = rs1 - rs2
  elif op == OPS.JAL:
    pass

  else:
    raise Exception(f"Operation {op} not implemented yet!")

def memget(addr):
  pass

def write_back(is_jump=False):
  if is_jump:
    rf[PC] += NPC
  else:
    rf[PC] += 4
  return

def state():
  pp = ''
  for i in range(32):
    if i != 0 and i % 8 == 0:
      pp += '\n'
    pp += "%3s: %08x " % ("x%d" % i, rf[i])
  pp += f'\n PC: {rf[PC]:08x} '
  print(''.join(pp))

def reset():
  global rf, memory, OFFSET
  rf = RegFile()

  # 64k
  memory = b'\x00*0x10000'

  OFFSET=0x80000000

  # Beginning of program
  rf[PC] = OFFSET


if __name__ == "__main__":

  f3, f7 = None, None
  rs1, rs2, rd = None, None, None
  imm_j = None
  OFFSET = 0x0

  for x in glob.glob("riscv-tests/isa/rv32ui/*"):
      if x.endswith('.dump'):
        continue
      with open(x, 'rb') as f:
        print(f"Testing file: {x}")

      # Put registers to initial state
        reset()
        e = ELFFile(f)

        for s in e.iter_segments():
          addr, dat = s.header.p_paddr, s.data()
          load_program(addr, dat, OFFSET)

          # Instruction Fetch
          ins = fetch(rf[PC], OFFSET)

          # Instruction Decode and Register Fetch
          op = decode(ins) 
          print(op)

          # Execute
          execute(op)

          # Memory Access
          memget(0)

          # Register Write Back
          write_back(is_jump=False) # If is not a branch / jump then add 4

          state()
          exit(0)
