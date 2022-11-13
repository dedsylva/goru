#ELF
/opt/riscv/bin/riscv32-unknown-linux-gnu-gcc -march=rv32g -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles  -I../env/p -I./macros/scalar -T../env/p/link.ld rv32ui/add.S -o rv32ui/add

#DUMP
 /opt/riscv/bin/riscv32-unknown-linux-gnu-objdump -D --disassemble-zeroes --section=.text --section=.text.startup --section=.text.init --section=.data rv32ui/add > rv32ui/add.dump
