#!/usr/bin/env python3

from maze import *
from pwn import *

LOCAL = 1

def get_new_process():
    if LOCAL:
        return process(["python3", "maze.py"])

def move_to_letter(loc, newloc):
    newloc = list(newloc)
    loc = list(loc)
    for i in range(len(newloc)):
        diff = newloc[i] - loc[i]
        if diff != 0:
            ret = chr(ord('a')+i)
            if diff > 0:
                ret = ret.upper()
            return ret


def solve(maze):
    d = {maze.loc: ''}
    solve_rec(maze, maze.loc, d)
    return d['win']

def solve_rec(maze, loc, d):
    here = d[loc]
    for newloc in maze.neighbors(*loc, typ='.@F'):
        letter = move_to_letter(loc, newloc)
        if maze.get(*newloc) == 'F':
            d['win'] = here+letter
            return here+letter
        if newloc not in d:
            d[newloc] = here+letter
            solve_rec(maze, newloc, d)


if __name__ == '__main__':
    p = get_new_process()
    p.recvuntil("maze:\n")
    maze = Maze.fromstr(p.recvuntil("===").decode().replace("=", '')[:-1])
    p.recvuntil("move: ")
    win = solve(maze)
    print(win)
    p.sendline(win)
    print(p.recvall())