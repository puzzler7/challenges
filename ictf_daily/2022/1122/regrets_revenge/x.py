#!/usr/bin/env python3

from pwn import *
from re import escape, fullmatch

# p = process(["python3", "server.py"])
p = remote('puzzler7.imaginaryctf.org', 7003)

flag_chars = []

reqs = 0

for c in range(32, 127):
    p.recvuntil(b"regex: ")
    p.sendline(escape(chr(c)).encode())
    reqs += 1
    rec = p.recvline()
    if b"flag" in rec:
        flag_chars.append(c)

print(len(flag_chars), "flag chars", ''.join(map(chr, flag_chars)))

flag = "ictf{"
while '}' not in flag:
    chars = list(flag_chars)
    while len(chars) > 1:
        idx = len(chars) // 2
        rx = '[ -~]'*len(flag)
        rx += '[' + ''.join(f"\\{'{:03o}'.format(c)}" for c in chars[:idx]) + ']'
        rx += '[ -~]+'
        rx = '(' + rx + ')?(\\([ -~]+)?'
        assert fullmatch(rx, rx)
        p.recvuntil(b"regex: ")
        p.sendline(rx.encode())
        reqs += 1
        if b"Match" in p.recvline():
            chars = chars[:idx]
        else:
            chars = chars[idx:]
    flag += chr(chars[0])
    print(flag)
    if '~' in flag:
        break


print(flag)
print("Solved in", reqs, "requests")
