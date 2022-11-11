## Playtest by Robin_Jadoul
from z3 import *
def nor(a, b):
    return ~(a | b)

c1 = BitVec("c1", 256)
c2 = BitVec("c2", 256)
fl = BitVec("flag", 256)
w1 =  nor(fl, c1);
w2 =  nor(fl, w1);
w3 =  nor(c1, w1);
w4 =  nor(w2, w3);
w5 =  nor(w4, w4);
w6 =  nor(w5, c2);
w7 =  nor(w5, w6);
w8 =  nor(c2, w6);
out =  nor(w7, w8);
s = Solver()
s.add(out == 0)
s.add(c1 == 0x44940e8301e14fb33ba0da63cd5d2739ad079d571d9f5b987a1c3db2b60c92a3)
s.add(c2 == 0xd208851a855f817d9b3744bd03fdacae61a70c9b953fca57f78e9d2379814c21)
assert s.check() == sat
print(s.model()[fl].as_long().to_bytes(32, "big").decode())
