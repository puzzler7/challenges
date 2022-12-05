#!/usr/bin/env python3

from recaesar_revenge import caesar
import sys

ct = open("output.txt", "rb").read()

def c_one(s, key):
    out = []
    for c in s:
        out += [alphabet[(c + key - 10)%len(alphabet)]]
        key = alphabet[(key + key - 10)%len(alphabet)]
    return out

def get_sorted_freqs(s):
    freqs = {}
    for c in s:
        if ord(c) not in list(alphabet):
            continue
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1

    sorted_chars = [i[0] for i in sorted(freqs.items(), key=lambda x:-x[1])]

    return sorted_chars


alphabet = bytes(range(10, 128))

corpus = open("dorian_gray.txt").read()
true_freqs = get_sorted_freqs(corpus)

print(true_freqs[:10])

bins = [[] for i in range(16)]

for i, c in enumerate(ct):
    bins[i%16].append(c)

key = []

for b in bins:
    for k in range(118):
        shifted = [chr(i) for i in c_one(b, k)]
        poss_freqs = get_sorted_freqs(shifted)
        # print(poss_freqs[:10], k)
        if len(set(poss_freqs[:10]) & set(true_freqs[:10])) >= 8:
            key.append(k)
            print('found key!', k)
            break

print(key, len(key))
sys.setrecursionlimit(2**31 - 1)
pt = caesar(ct, key)
solved = open("solved.txt", "wb")
solved.write(bytes(pt))