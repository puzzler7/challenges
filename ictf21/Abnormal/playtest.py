## Playtest by Robin_Jadoul
# z3 and vim macros go brrrr
from z3 import *

def nor(a, b):
    return ~(a|b)

def nora(inp):
    assert len(inp) == 3
    out = [None for _ in range(2)]
    w1 = nor(inp[0], inp[1])
    w2 = nor(inp[0], w1)
    w3 = nor(inp[1], w1)
    w4 = nor(w2, w3)
    w5 = nor(w4, w4)
    w6 = nor(w5, inp[2])
    w7 = nor(w5, w6)
    w8 = nor(inp[2], w6)
    w9 = nor(w7, w8)
    out[0] = nor(w9, w9)
    w10 = nor(inp[0], inp[0])
    w11 = nor(inp[1], inp[1])
    w12 = nor(w10, w11)
    w13 = nor(inp[2], inp[2])
    w14 = nor(w11, w13)
    w15 = nor(w12, w14)
    w16 = nor(w10, w13)
    w17 = nor(w15, w15)
    w18 = nor(w17, w16)
    out[1] = nor(w18, w18)
    return out[1], out[0]

def norb(inp):
    assert len(inp) == 33
    out = [None for _ in range(17)]
    [w1, out[0]]       = nora([inp[32], inp[16], inp[0]] [::-1])
    [w2, out[1]]       = nora([w1,      inp[1],  inp[17]][::-1])
    [w3, out[2]]       = nora([w2,      inp[18], inp[2]] [::-1])
    [w4, out[3]]       = nora([w3,      inp[3],  inp[19]][::-1])
    [w5, out[4]]       = nora([w4,      inp[20], inp[4]] [::-1])
    [w6, out[5]]       = nora([w5,      inp[5],  inp[21]][::-1])
    [w7, out[6]]       = nora([w6,      inp[22], inp[6]] [::-1])
    [w8, out[7]]       = nora([w7,      inp[7],  inp[23]][::-1])
    [w9, out[8]]       = nora([w8,      inp[24], inp[8]] [::-1])
    [w10, out[9]]      = nora([w9,      inp[9],  inp[25]][::-1])
    [w11, out[10]]     = nora([w10,     inp[26], inp[10]][::-1])
    [w12, out[11]]     = nora([w11,     inp[11], inp[27]][::-1])
    [w13, out[12]]     = nora([w12,     inp[28], inp[12]][::-1])
    [w14, out[13]]     = nora([w13,     inp[13], inp[29]][::-1])
    [w15, out[14]]     = nora([w14,     inp[30], inp[14]][::-1])
    [out[16], out[15]] = nora([w15,     inp[15], inp[31]][::-1])
    return out[16], out[:16]

def norc(inp):
    assert len(inp) == 513
    out = [None for _ in range(257)]
    [w1,       out[0:16]]    = norb([*inp[0:16]   , *inp[256:272], inp[512], ])
    [w2,       out[16:32]]   = norb([*inp[272:288], *inp[16:32],   w1,       ])
    [w3,       out[32:48]]   = norb([*inp[32:48]  , *inp[288:304], w2,       ])
    [w4,       out[48:64]]   = norb([*inp[304:320], *inp[48:64],   w3,       ])
    [w5,       out[64:80]]   = norb([*inp[64:80]  , *inp[320:336], w4,       ])
    [w6,       out[80:96]]   = norb([*inp[336:352], *inp[80:96],   w5,       ])
    [w7,       out[96:112]]  = norb([*inp[96:112] , *inp[352:368], w6,       ])
    [w8,       out[112:128]] = norb([*inp[368:384], *inp[112:128], w7,       ])
    [w9,       out[128:144]] = norb([*inp[128:144], *inp[384:400], w8,       ])
    [w10,      out[144:160]] = norb([*inp[400:416], *inp[144:160], w9,       ])
    [w11,      out[160:176]] = norb([*inp[160:176], *inp[416:432], w10,      ])
    [w12,      out[176:192]] = norb([*inp[432:448], *inp[176:192], w11,      ])
    [w13,      out[192:208]] = norb([*inp[192:208], *inp[448:464], w12,      ])
    [w14,      out[208:224]] = norb([*inp[464:480], *inp[208:224], w12,      ])
    [w15,      out[224:240]] = norb([*inp[224:240], *inp[480:496], w14,      ])
    [out[256], out[240:256]] = norb([*inp[496:512], *inp[240:256], w15,      ])
    return out[256], out[:256]

def tobits(x, n):
    if isinstance(x, int):
        x = BitVecVal(x, n)
    return [Extract(i, i, x) for i in range(n)]
def frombits(x):
    return Concat(*x)

def abnormal(inp):
    c1, w1 = norc(tobits(inp, 256) + tobits(0x1a86f06e4e492e2c1ea6f4d5726e6d36bec57cf31472b986a675d3bc8e5d22b81, 257))
    c2, w2 = norc(tobits(0x1a5e20394c934fd1198b1517d57e730cd225ccfa064ff42db76c19f3b7c0da91a6bf077b696cc4b22c0e56f4d3e6e150e386d6f04479ac502600e01fcdc29f5e4, 513))
    s.add(c1 == c2)
    w1 = frombits(w1)
    w2 = frombits(w2)
    w3 = nor(w1, w2)
    w4 = nor(w1, w3)
    w5 = nor(w2, w3)
    w6 = nor(w4, w5)
    return nor(w6, w6)

s = Solver()
flag = BitVec("flag", 256)
s.add(UGT(flag, 0x696374667b00000000000000000000000000000000000000000000000000007d))
s.add(ULT(flag, 0x696374667c000000000000000000000000000000000000000000000000000000))

s.add(abnormal(flag) == 0)
assert s.check() == sat
print(s.model()[flag].as_long().to_bytes(32, "big").decode())
