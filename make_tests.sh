#ELF
C:/SysGCC/risc-v/bin/riscv64-unknown-elf-gcc.exe -march=rv64g -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles  -I../env/p -I./macros/scalar -T../env/p/link.ld xori.S -o xori

#DUMP
C:/SysGCC/risc-v/bin/riscv64-unknown-elf-objdump.exe --disassemble-all --disassemble-zeroes --section=.text --section    =.text.startup --section=.text.init --section=.data xori.S -o xori.dump