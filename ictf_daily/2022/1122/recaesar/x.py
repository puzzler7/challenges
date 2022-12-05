#!/usr/bin/env python3

from recaesar import caesar

alphabet = bytes(range(32, 127))

def uncaesar(ct, key):
    ret = [alphabet[(ct[0] - key[0] - 32)%len(alphabet)]]
    if len(ct) > 1:
           ret += uncaesar(ct[1:], caesar(key, key))
    return ret

flag = b'w Mw>Y2XE/cOO+8`mSIBd]_dQS3H!:{:gI5f!":%2SVgN1pM>|;lh[G9m]p`U?0@1O3'

for i in range(97):
    out = bytes(uncaesar(flag, [i]))
    if b'ictf' in out:
        print(out)
