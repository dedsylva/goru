#! /usr/bin/env python3

import unittest
from unittest_prettify.colorize import colorize, GREEN 
from goru import cpu

@colorize(color=GREEN)
class TestDecodeOPS(unittest.TestCase):
  LUI    = 0b0110111
  AUIPC  = 0b0110111
  JAL    = 0b1101111
  JALR   = 0b1100111
  BEQ    = 0b1100011
  BNE    = 0b1100011
  BLT    = 0b1100011
  BGE    = 0b1100011
  BLTU   = 0b1100011
  BGEU   = 0b1100011
  LB     = 0b0000011
  LBU    = 0b0000011
  LH     = 0b0000011
  LW     = 0b0000011
  LHU    = 0b0000011
  ADDI   = 0b0010011
  SLTI   = 0b0010011
  SLTIU  = 0b0010011
  XORI   = 0b0010011
  ORI    = 0b0010011
  ANDI   = 0b0010011
  SLLI   = 0b0010011
  SRLI   = 0b0010011
  SRAI   = 0b0010011
  CSRRW  = 0b1110011
  CSRRS  = 0b1110011
  CSRRC  = 0b1110011
  CSRRWI = 0b1110011
  CSRRSI = 0b1110011
  CSRRCI = 0b1110011
  SB     = 0b0100011
  SH     = 0b0100011
  SW     = 0b0100011
  ADD    = 0b0110011
  SUB    = 0b0110011
  SLL    = 0b0110011
  SLT    = 0b0110011
  SLTU   = 0b0110011
  XOR    = 0b0110011
  SRL    = 0b0110011
  SRA    = 0b0110011
  OR     = 0b0110011
  AND    = 0b0110011
  ECALL  = 0b1110011
  EBREAK = 0b1110011

  def test_decode_LUI(self):
    """ Test Decode LUI OPCODE """
    self.assertEqual(cpu.decode(self.LUI), cpu.OPS.LUI)
    
  def test_decode_AUIPC(self):
    """ Test Decode AUIPC PCODE """
    self.assertEqual(cpu.decode(self.AUIPC), cpu.OPS.AUIPC)
    
  def test_decode_JAL(self):
    """ Test Decode JAL OPCODE """
    self.assertEqual(cpu.decode(self.JAL), cpu.OPS.JAL)
    
  def test_decode_JALR(self):
    """ Test Decode JALR OPCODE """
    self.assertEqual(cpu.decode(self.JALR), cpu.OPS.JALR)
    
  def test_decode_BEQ(self):
    """ Test Decode BEQ OPCODE """
    self.assertEqual(cpu.decode(self.BEQ), cpu.OPS.BEQ)
    
  def test_decode_BNE(self):
    """ Test Decode BNE OPCODE """
    self.assertEqual(cpu.decode(self.BNE), cpu.OPS.BNE)
    
  def test_decode_BLT(self):
    """ Test Decode BLT OPCODE """
    self.assertEqual(cpu.decode(self.BLT), cpu.OPS.BLT)
    
  def test_decode_BGE(self):
    """ Test Decode BGE OPCODE """
    self.assertEqual(cpu.decode(self.BGE), cpu.OPS.BGE)
    
  def test_decode_BLTU(self):
    """ Test Decode BLTU OPCODE """
    self.assertEqual(cpu.decode(self.BLTU), cpu.OPS.BLTU)
    
  def test_decode_BGEU(self):
    """ Test Decode BGEU OPCODE """
    self.assertEqual(cpu.decode(self.BGEU), cpu.OPS.BGEU)
    
  def test_decode_LB(self):
    """ Test Decode LB OPCODE """
    self.assertEqual(cpu.decode(self.LB), cpu.OPS.LB)
    
  def test_decode_LBU(self):
    """ Test Decode LBU OPCODE """
    self.assertEqual(cpu.decode(self.LBU), cpu.OPS.LBU)
    
  def test_decode_LH(self):
    """ Test Decode LH OPCODE """
    self.assertEqual(cpu.decode(self.LH), cpu.OPS.LH)
    
  def test_decode_LW(self):
    """ Test Decode LW OPCODE """
    self.assertEqual(cpu.decode(self.LW), cpu.OPS.LW)
    
  def test_decode_LHU(self):
    """ Test Decode LHU OPCODE """
    self.assertEqual(cpu.decode(self.LHU), cpu.OPS.LHU)
    
  def test_decode_ADDI(self):
    """ Test Decode ADDI OPCODE """
    self.assertEqual(cpu.decode(self.ADDI), cpu.OPS.ADDI)
    
  def test_decode_SLTI(self):
    """ Test Decode SLTI OPCODE """
    self.assertEqual(cpu.decode(self.SLTI), cpu.OPS.SLTI)
    
  def test_decode_SLTIU(self):
    """ Test Decode SLTIU OPCODE """
    self.assertEqual(cpu.decode(self.SLTIU), cpu.OPS.SLTIU)
    
  def test_decode_XORI(self):
    """ Test Decode XORI OPCODE """
    self.assertEqual(cpu.decode(self.XORI), cpu.OPS.XORI)
    
  def test_decode_ORI(self):
    """ Test Decode ORI OPCODE """
    self.assertEqual(cpu.decode(self.ORI), cpu.OPS.ORI)
    
  def test_decode_ANDI(self):
    """ Test Decode ANDI OPCODE """
    self.assertEqual(cpu.decode(self.ANDI), cpu.OPS.ANDI)
    
  def test_decode_SLLI(self):
    """ Test Decode SLLI OPCODE """
    self.assertEqual(cpu.decode(self.SLLI), cpu.OPS.SLLI)
    
  def test_decode_SRLI(self):
    """ Test Decode SRLI OPCODE """
    self.assertEqual(cpu.decode(self.SRLI), cpu.OPS.SRLI)
    
  def test_decode_SRAI(self):
    """ Test Decode SRAI OPCODE """
    self.assertEqual(cpu.decode(self.SRAI), cpu.OPS.SRAI)
    
  def test_decode_CSRRW(self):
    """ Test Decode CSRRW OPCODE """
    self.assertEqual(cpu.decode(self.CSRRW), cpu.OPS.CSRRW)
    
  def test_decode_CSRRS(self):
    """ Test Decode CSRRS OPCODE """
    self.assertEqual(cpu.decode(self.CSRRS), cpu.OPS.CSRRS)
    
  def test_decode_CSRRC(self):
    """ Test Decode CSRRC OPCODE """
    self.assertEqual(cpu.decode(self.CSRRC), cpu.OPS.CSRRC)
    
  def test_decode_CSRRWI(self):
    """ Test Decode CSRRWI OPCODE """
    self.assertEqual(cpu.decode(self.CSRRWI), cpu.OPS.CSRRWI)
    
  def test_decode_CSRRSI(self):
    """ Test Decode CSRRSI OPCODE """
    self.assertEqual(cpu.decode(self.CSRRSI), cpu.OPS.CSRRSI)
    
  def test_decode_CSRRCI(self):
    """ Test Decode CSRRCI OPCODE """
    self.assertEqual(cpu.decode(self.CSRRCI), cpu.OPS.CSRRCI)
    
  def test_decode_SB(self):
    """ Test Decode SB OPCODE """
    self.assertEqual(cpu.decode(self.SB), cpu.OPS.SB)
    
  def test_decode_SH(self):
    """ Test Decode SH OPCODE """
    self.assertEqual(cpu.decode(self.SH), cpu.OPS.SH)
    
  def test_decode_SW(self):
    """ Test Decode SW OPCODE """
    self.assertEqual(cpu.decode(self.SW), cpu.OPS.SW)
    
  def test_decode_ADD(self):
    """ Test Decode ADD OPCODE """
    self.assertEqual(cpu.decode(self.ADD), cpu.OPS.ADD)
    
  def test_decode_SUB(self):
    """ Test Decode SUB OPCODE """
    self.assertEqual(cpu.decode(self.SUB), cpu.OPS.SUB)
    
  def test_decode_SLL(self):
    """ Test Decode SLL OPCODE """
    self.assertEqual(cpu.decode(self.SLL), cpu.OPS.SLL)
    
  def test_decode_SLTU(self):
    """ Test Decode SLTU OPCODE """
    self.assertEqual(cpu.decode(self.SLTU), cpu.OPS.SLTU)
    
  def test_decode_XOR(self):
    """ Test Decode XOR OPCODE """
    self.assertEqual(cpu.decode(self.XOR), cpu.OPS.XOR)
    
  def test_decode_SRL(self):
    """ Test Decode SRL OPCODE """
    self.assertEqual(cpu.decode(self.SRL), cpu.OPS.SRL)
    
  def test_decode_SRA(self):
    """ Test Decode SRA OPCODE """
    self.assertEqual(cpu.decode(self.SRA), cpu.OPS.SRA)
    
  def test_decode_OR(self):
    """ Test Decode OR OPCODE """
    self.assertEqual(cpu.decode(self.OR), cpu.OPS.OR)
    
  def test_decode_AND(self):
    """ Test Decode AND OPCODE """
    self.assertEqual(cpu.decode(self.AND), cpu.OPS.AND)
    
  def test_decode_ECALL(self):
    """ Test Decode ECALL OPCODE """
    self.assertEqual(cpu.decode(self.ECALL), cpu.OPS.ECALL)

    
  def test_decode_EBREAK(self):
    """ Test Decode EBREAK OPCODE """
    self.assertEqual(cpu.decode(self.EBREAK), cpu.OPS.EBREAK)


@colorize(color=GREEN)
class TestDecodeFunct3(unittest.TestCase):
  JALR   = 0b000
  BEQ    = 0b000
  LB     = 0b000
  SB     = 0b000
  ADDI   = 0b000
  ADD    = 0b000
  SUB    = 0b000
  ECALL  = 0b000
  EBREAK = 0b000
  BNE    = 0b001
  LH     = 0b001
  SH     = 0b001
  SLLI   = 0b001
  CSRRW  = 0b001
  SLL    = 0b001
  SW     = 0b010
  SLTI   = 0b010
  SLT    = 0b010
  CSRRS  = 0b010
  LW     = 0b010
  SLTU   = 0b011
  CSRRC  = 0b011
  BLT    = 0b100
  LBU    = 0b100
  XORI   = 0b100
  XOR    = 0b100
  BGE    = 0b101
  LHU    = 0b101
  SRLI   = 0b101
  SRAI   = 0b101
  SRL    = 0b101
  SRA    = 0b101
  CSRRWI = 0b101
  BLTU   = 0b110
  ORI    = 0b110
  OR     = 0b110
  CSRRSI = 0b110
  BGEU   = 0b111
  ANDI   = 0b111
  AND    = 0b111
  CSRRCI = 0b111

  def test_Funct3_JALR(self):
    """ Test Funct3 JALR OPCODE """
    self.assertEqual(self.JALR, cpu.Funct3.JALR.value)
 
  def test_Funct3_BEQ(self):
    """ Test Funct3 BEQ OPCODE """
    self.assertEqual(self.BEQ, cpu.Funct3.BEQ.value)
 
  def test_Funct3_LB(self):
    """ Test Funct3 LB OPCODE """
    self.assertEqual(self.LB, cpu.Funct3.LB.value)
 
  def test_Funct3_SB(self):
    """ Test Funct3 SB OPCODE """
    self.assertEqual(self.SB, cpu.Funct3.SB.value)
 
  def test_Funct3_ADDI(self):
    """ Test Funct3 ADDI OPCODE """
    self.assertEqual(self.ADDI, cpu.Funct3.ADDI.value)
 
  def test_Funct3_ADD(self):
    """ Test Funct3 ADD OPCODE """
    self.assertEqual(self.ADD, cpu.Funct3.ADD.value)
 
  def test_Funct3_SUB(self):
    """ Test Funct3 SUB OPCODE """
    self.assertEqual(self.SUB, cpu.Funct3.SUB.value)
 
  def test_Funct3_ECALL(self):
    """ Test Funct3 ECALL OPCODE """
    self.assertEqual(self.ECALL, cpu.Funct3.ECALL.value)
 
  def test_Funct3_EBREAK(self):
    """ Test Funct3 EBREAK OPCODE """
    self.assertEqual(self.EBREAK, cpu.Funct3.EBREAK.value)
 
  def test_Funct3_BNE(self):
    """ Test Funct3 BNE OPCODE """
    self.assertEqual(self.BNE, cpu.Funct3.BNE.value)
 
  def test_Funct3_LH(self):
    """ Test Funct3 LH OPCODE """
    self.assertEqual(self.LH, cpu.Funct3.LH.value)
 
  def test_Funct3_SH(self):
    """ Test Funct3 SH OPCODE """
    self.assertEqual(self.SH, cpu.Funct3.SH.value)
 
  def test_Funct3_SLLI(self):
    """ Test Funct3 SLLI OPCODE """
    self.assertEqual(self.SLLI, cpu.Funct3.SLLI.value)
 
  def test_Funct3_CSRRW(self):
    """ Test Funct3 CSRRW OPCODE """
    self.assertEqual(self.CSRRW, cpu.Funct3.CSRRW.value)
 
  def test_Funct3_SLL(self):
    """ Test Funct3 SLL OPCODE """
    self.assertEqual(self.SLL, cpu.Funct3.SLL.value)
 
  def test_Funct3_SW(self):
    """ Test Funct3 SW OPCODE """
    self.assertEqual(self.SW, cpu.Funct3.SW.value)
 
  def test_Funct3_SLTI(self):
    """ Test Funct3 SLTI OPCODE """
    self.assertEqual(self.SLTI, cpu.Funct3.SLTI.value)
 
  def test_Funct3_SLT(self):
    """ Test Funct3 SLT OPCODE """
    self.assertEqual(self.SLT, cpu.Funct3.SLT.value)
 
  def test_Funct3_CSRRS(self):
    """ Test Funct3 CSRRS OPCODE """
    self.assertEqual(self.CSRRS, cpu.Funct3.CSRRS.value)
 
  def test_Funct3_LW(self):
    """ Test Funct3 LW OPCODE """
    self.assertEqual(self.LW, cpu.Funct3.LW.value)
 
  def test_Funct3_SLTU(self):
    """ Test Funct3 SLTU OPCODE """
    self.assertEqual(self.SLTU, cpu.Funct3.SLTU.value)
 
  def test_Funct3_CSRRC(self):
    """ Test Funct3 CSRRC OPCODE """
    self.assertEqual(self.CSRRC, cpu.Funct3.CSRRC.value)
 
  def test_Funct3_BLT(self):
    """ Test Funct3 BLT OPCODE """
    self.assertEqual(self.BLT, cpu.Funct3.BLT.value)
 
  def test_Funct3_LBU(self):
    """ Test Funct3 LBU OPCODE """
    self.assertEqual(self.LBU, cpu.Funct3.LBU.value)
 
  def test_Funct3_XORI(self):
    """ Test Funct3 XORI OPCODE """
    self.assertEqual(self.XORI, cpu.Funct3.XORI.value)
 
  def test_Funct3_XOR(self):
    """ Test Funct3 XOR OPCODE """
    self.assertEqual(self.XOR, cpu.Funct3.XOR.value)
 
  def test_Funct3_BGE(self):
    """ Test Funct3 BGE OPCODE """
    self.assertEqual(self.BGE, cpu.Funct3.BGE.value)
 
  def test_Funct3_LHU(self):
    """ Test Funct3 LHU OPCODE """
    self.assertEqual(self.LHU, cpu.Funct3.LHU.value)
 
  def test_Funct3_SRLI(self):
    """ Test Funct3 SRLI OPCODE """
    self.assertEqual(self.SRLI, cpu.Funct3.SRLI.value)
 
  def test_Funct3_SRAI(self):
    """ Test Funct3 SRAI OPCODE """
    self.assertEqual(self.SRAI, cpu.Funct3.SRAI.value)
 
  def test_Funct3_SRL(self):
    """ Test Funct3 SRL OPCODE """
    self.assertEqual(self.SRL, cpu.Funct3.SRL.value)
 
  def test_Funct3_SRA(self):
    """ Test Funct3 SRA OPCODE """
    self.assertEqual(self.SRA, cpu.Funct3.SRA.value)
 
  def test_Funct3_CSRRWI(self):
    """ Test Funct3 CSRRWI OPCODE """
    self.assertEqual(self.CSRRWI, cpu.Funct3.CSRRWI.value)
 
  def test_Funct3_BLTU(self):
    """ Test Funct3 BLTU OPCODE """
    self.assertEqual(self.BLTU, cpu.Funct3.BLTU.value)
 
  def test_Funct3_ORI(self):
    """ Test Funct3 ORI OPCODE """
    self.assertEqual(self.ORI, cpu.Funct3.ORI.value)
 
  def test_Funct3_OR(self):
    """ Test Funct3 OR OPCODE """
    self.assertEqual(self.OR, cpu.Funct3.OR.value)
 
  def test_Funct3_CSRRSI(self):
    """ Test Funct3 CSRRSI OPCODE """
    self.assertEqual(self.CSRRSI, cpu.Funct3.CSRRSI.value)
 
  def test_Funct3_BGEU(self):
    """ Test Funct3 BGEU OPCODE """
    self.assertEqual(self.BGEU, cpu.Funct3.BGEU.value)
 
  def test_Funct3_ANDI(self):
    """ Test Funct3 ANDI OPCODE """
    self.assertEqual(self.ANDI, cpu.Funct3.ANDI.value)
 
  def test_Funct3_AND(self):
    """ Test Funct3 AND OPCODE """
    self.assertEqual(self.AND, cpu.Funct3.AND.value)
 
  def test_Funct3_CSRRCI(self):
    """ Test Funct3 CSRRCI OPCODE """
    self.assertEqual(self.CSRRCI, cpu.Funct3.CSRRCI.value)
 
    
if __name__ == '__main__':
  unittest.main(verbosity=2)