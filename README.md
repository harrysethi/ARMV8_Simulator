ARMV8_Simulator
===============

ARMv8 instruction set simulator:

Given an ELF format binary for the ARM architecture, ARMV8_Simulator simulates it. The simulator parses the ELF format binary, extracts
the instructions (along with other information), decodes them and take actions accordingly. It keeps track of the state of the memory and all the registers.

ARMV8_Simulator is also integrated with a tiny debugger.

Some more points:

1. Run make.sh from inside this directory. Very important. 
2. For help options inside ARMV8 directory, run "python main.py --help" and take help from help.
3. For running machine code in elf file, run as 'python main.py <filename>'
4. For running debugger run as 'python main.py --debug <filename>'
5. When inside debugger, type help for debugger options.
6. The instructions we have simulated are : 
ADD, ADDS, ADR, ADRP, ASR, AND, B.{cond}, B, BR, BL, BLR, CBNZ, CBZ, CMP, LDP, LDR, LDRSW, LSL, LSR, NOP, MOV, RET, STP, STR, SUB, SUBS.


We have used pyelftools for elf parsing, credits to "https://github.com/eliben/pyelftools"


---------------------------------Happy ARMV8 simulation. :)-------------------------------------------------------
