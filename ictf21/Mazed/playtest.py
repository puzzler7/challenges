## Playtest by Robin_Jadoul
from maze import Maze
from pwn import *
from collections import deque
import itertools

def solve(m):
    print("Solving")
    def at(x):
        if not all(0 <= y < 50 for y in x): return "#"
        return m[x[0]][x[1]][x[2]]

    parent = {}
    parent[(0, 0, 0)] = None
    q = deque([(0, 0, 0)])
    while q:
        pos = q.popleft()
        if at(pos) == "F": break
        for x, d in zip("AaBbCc", [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]):
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


io = process(["python", "-u", "maze.py"])
io.recvuntil("This is your maze:\n")
m = Maze.fromstr(io.recvuntil("=")[:-2].decode())
io.sendline("".join(solve(m.maze)))
io.interactive()
