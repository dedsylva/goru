#! /usr/bin/python3
from enum import Enum

RegFile = [0]*33
PC = 32
NPC = 0

# 64k
memory = b'\x00*0x10000'

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

def fetch():
  return RegFile[PC]

def decode(ins):
  op = OPS(ins & 0x7f)
  f3, f7 = None, None
  rs1, rs2, rd = None, None, None

  print(f"OPS: {op.name}")

  # get_bytes
  def gb(s,e):
  # puts in beginning & right amount of 1111s
    return (op.value >> e) & ((1 << (s-e+1))-1)

  # Funct3
  if op not in (OPS.LUI, OPS.AUIPC, OPS.JAL):
    f3 = Funct3(gb(14,12))
    print(f"OPS: {op.name} Funct3: {hex(f3.value)}")

  # Funct7
  if op in (OPS.SLLI, OPS.SRLI, OPS.SRAI, OPS.ADD, OPS.SUB, OPS.SLL, OPS.SLT,
                 OPS.SLTU, OPS.XOR, OPS.SRL, OPS.SRA, OPS.OR, OPS.AND):

    f7 = Funct7(gb(31,25))
    print(f"OPS: {op.name} Funct3: {hex(f3.value)}  Funct7: {hex(f7.value)}")

  # rd
  if op not in (OPS.BEQ, OPS.BNE, OPS.BLT, OPS.BGE, OPS.BLTUU, OPS.BGEU, OPS.SB,
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

  return op

def execute():
  pass

def memget(addr):
  pass

def write_back(is_jump=False):
  if is_jump:
    RegFile[PC] += NPC
  else:
    RegFile[PC] += 4
  return

def state():
  pp = ''
  for i in range(32):
    if i != 0 and i % 8 == 0:
      pp += '\n'
    pp += "%3s: %08x " % ("x%d" % i, RegFile[i])
  pp += f'\n PC: {RegFile[PC]:08x} '
  print(''.join(pp))

if __name__ == "__main__":

  # dat = [0b01000001111100011000001110110011, 0b01000001111100011000001110110111]
  dat = [0b01000001111100011000001110110011]
  for d in dat:

    # Instruction Fetch
    ins = fetch()

    # Instruction Decode and Register Fetch
    op = decode(d) 
    state()

    # Execute
    execute()

    # Memory Access
    memget(0)

    # Register Write Back
    write_back(is_jump=False) # If is not a branch / jump then add 4
