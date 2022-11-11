#!/usr/bin/env python3

from primefac import primefac
from Crypto.Util.number import *
from itertools import islice

from primetime import *

def decode(n):
    ret = 0
    primelist = list(islice(primes(), ELEMENT_LEN))
    fac = list(primefac(n))
    for num in primelist[::-1]:
        ret += fac.count(num)
        ret <<= 8
    return ret >> 8

if __name__ == '__main__':
    exec(open("output.txt").read())
    geninv = pow(decode(gen), -1, 2**128)
    akey = (decode(apub)*geninv)%2**128
    bkey = (decode(bpub)*geninv)%2**128
    print(akey, bkey)
    s = Element(gen)*akey*bkey
    sinv = pow(decode(s.n), -1, 2**128)
    flag = (decode(ct)*sinv) % 2**128
    print(b'ictf{'+long_to_bytes(flag)[::-1]+b'}')