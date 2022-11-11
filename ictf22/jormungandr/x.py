#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes

primes = [277, 283, 307, 313, 331, 347]

ct = 'ce10e59f40c8d954d9dad1ea81811a834d26580107149d16c3a769198fb158f0cb0e33dbd98f8dc8bb874105974b71719790b23c971736e8fe8ec88e8695'
mod = 16**len(ct)

n = int(ct, 16)

for p in primes:
    mult = 3**p
    n = (n-p)%mod
    inv = pow(mult, -1, mod)
    n = (n*inv)%mod


print(long_to_bytes(n))


