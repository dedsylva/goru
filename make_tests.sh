#ELF
C:/SysGCC/risc-v/bin/riscv64-unknown-elf-gcc.exe -march=rv32g -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles  -I../env/p -I./macros/scalar -T../env/p/link.ld rv32ui/xori.S -o rv32ui/xori

#DUMP
C:/SysGCC/risc-v/bin/riscv64-unknown-elf-objdump.exe --disassemble-all --disassemble-zeroes --section=.text --section    =.text.startup --section=.text.init --section=.data xori.S -o xori.dump