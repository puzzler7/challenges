#!/usr/bin/env python3

from fixedint import FixedInt
from Crypto.Util.number import *
from random import randint

#        0123456789abcdef0123456789abcdef
flag = b"ictf{nero'ssonronrosenosoreores}"
flagnum = bytes_to_long(flag)

Fint = FixedInt(256, signed=0, mutable=0)

n1 = randint(2**255, 2**256)
flagsum = Fint(n1+flagnum+1)
print('1'+'{:032x}'.format(n1))

n2 = randint(2**255, 2**256)
n3 = Fint(flagsum-n2-1)
print('1'+'{:032x}'.format(n2)+'{:032x}'.format(n3))