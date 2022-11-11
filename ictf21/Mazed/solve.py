## Playtest by Robin_Jadoul
from maze import Maze
from pwn import *
from collections import deque
import itertools

def solve(m):
    print("Solving")
    def at(x):
        if not all(0 <= y < 10 for y in x): return "#"
        return m[x[0]][x[1]][x[2]][x[3]]

    parent = {}
    parent[(0, 0, 0, 0)] = None
    q = deque([(0, 0, 0, 0)])
    while q:
        pos = q.popleft()
        if at(pos) == "F": break
        for x, d in zip("AaBbCcDd", [(1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0), (0, 0, 1, 0), (0, 0, -1, 0), (0, 0, 0, 1), (0, 0, 0, -1)]):
            npos = tuple(a + b for a, b in zip(pos, d))
            if npos not in parent and at(npos) != "#":
                parent[npos] = (pos, x)
                q.append(npos)
    assert at(pos) == "F"
    r = ""
    while parent[pos] is not None:
        pos, t = parent[pos]
        r = t + r
    return r

if args.LOCAL:
    io = process(["python3", "-u", "maze.py"])
else:
    io = remote("localhost", 42017)
   # io.recvuntil(b"work: ")
   # io.sendline(process(io.recvline().strip().decode(), shell=True).recvall())
io.recvuntil(b"This is your maze:\n")
m = Maze.fromstr(io.recvuntil(b"=")[:-2].decode())
print(m)
io.sendline("".join(solve(m.maze)).encode())
io.interactive()
