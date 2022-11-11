## Playtest by Robin_Jadoul

import primetime
from Crypto.Util.number import long_to_bytes, bytes_to_long
with open("output.txt") as f:
    exec(f.read())

# Element: ~base prime, cut off after 16 primes with 8 bits per prime = 128 bits
# Element(1) == 0
# Addition = addition mod 2^128
# Multiplication (by int) = normal mult
# Multiplication (by element) = normal mult (same approach as L2R fast pow, extracting bits per prime instead)
def project(x):
    r = 0
    for _, p in list(zip(range(primetime.ELEMENT_LEN), primetime.primes()))[::-1]:
        # alternatively, extract with smth like log(gcd(p^256, x), p)
        e = 0
        while not (x % p):
            x //= p
            e += 1
        r = (r * 256) + e
    return r

assert project(gen) == bytes_to_long(b"+h3_g3n3ra+0r_pt"[::-1])
print(project((primetime.Element.encode([42]) * 1337).n), 1337*42)

gen = project(gen)
apub = project(apub)
bpub = project(bpub)
ct = project(ct)

# gen * akey = apub
# gen * bkey = bpub
# gen * akey * bkey = s
# ct = m * s
M = (1<<128)
akey = (apub * pow(gen, -1, M)) % M
s = bpub * akey
m = (ct * pow(s, -1, M)) % M
print(long_to_bytes(m)[::-1])
