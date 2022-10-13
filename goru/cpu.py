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
  op_code = OPS(ins & 0b1111111)
  f3 = None
  f7 = None

  print(f"OPS: {op_code.name}")

  # Funct3
  if op_code not in (OPS.LUI, OPS.AUIPC, OPS.JAL):
    f3 = Funct3((ins & 0b111) >> 12)
    print(f"OPS: {op_code.name} Funct3: {bin(f3.value)}")

  # Funct7
  if op_code in (OPS.SLLI, OPS.SRLI, OPS.SRAI, OPS.ADD, OPS.SUB, OPS.SLL, OPS.SLT,
                 OPS.SLTU, OPS.XOR, OPS.SRL, OPS.SRA, OPS.OR, OPS.AND):

    f7 = Funct7((ins & 0b1111111) >> 25)
    print(f"OPS: {op_code.name} Funct3: {bin(f3.value)}  Funct7: {bin(f7.value)}")

  return op_code

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

if __name__ == "__main__":

  dat = [0b01000001111100011000001110110011, 0b01000001111100011000001110110111]
  for d in dat:

    # Instruction Fetch
    ins = fetch()

    # Instruction Decode and Register Fetch
    op = decode(d) 

    # Execute
    execute()

    # Memory Access
    memget(0)

    # Register Write Back
    write_back(is_jump=False) # If is not a branch / jump then add 4
