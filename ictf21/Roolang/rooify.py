#!/usr/bin/env python3

import sys
from PIL import Image
import numpy as np
from math import sqrt, floor

# push, pop, add, sub, mult, div, mod, andd, orr, xorr, dupe, swap, reg, pr, prn, label, jump, jnz, ret, jal

words = ['push', 'pop', 'add', 'sub', 'mult', 'div', 'mod', 'andd', 'orr', 'xorr', 'dupe', 'swap', 'reg', 'pr', 'prn', 'label', 'jump', 'jnz', 'ret', 'jal']

roodict = {'push' : 'robin',
           'pop'  : 'rboin',
           'add'  : 'riobn',
           'sub'  : 'rooon',
           'mult' : 'riibn',
           'div'  : 'riion',
           'mod'  : 'ribon', 
           'andd' : 'ronon', 
           'orr'  : 'roion', 
           'xorr' : 'roibn', 
           'dupe' : 'riiin', 
           'swap' : 'rioin', 
           'reg'  : 'rinin', 
           'pr'   : 'rbiin', 
           'prn'  : 'rboon', 
           'label': 'rnbon', 
           'jump' : 'rioon', 
           'jnz'  : 'rbion', 
           'ret'  : 'ribbn', 
           'jal'  : 'roiin'}

def makeInt(n):
    assert n >= 0 and n < 27**27
    ret = []
    while n > 0:
        ret.append(makeDigit(n%27))
        n //= 27
    return makeDigit(len(ret))+"".join(ret[::-1])

def makeDigit(n):
    assert n < 27
    ret = ""
    while n > 0:
        ret = str(n%3) + ret
        n //= 3
    ret = "000"+ret
    return 'r'+ret[-3:].replace("0", 'o').replace('1', 'b').replace('2', 'i')+'n'

def writeImg(output, fname):
    size = floor(sqrt(len(output)))
    while len(output)%size != 0:
        size += 1
    w = size
    h = len(output)//w
    img = Image.new("RGBA", (w*128,h*128))

    R = Image.open("robin.png")
    O = Image.open("oreos.png")
    B = Image.open("blind.png")
    I = Image.open("imag.png")
    N = Image.open("nobooli.png")
    d = dict(zip("Robin", [R,O,B,I,N]))

    for i, c in enumerate(output):
        img.paste(d[c], ((i%w)*128, (i//w)*128))

    img.save(fname)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Usage: ./rooify.py [filename]")

    ret = []
    label = 0
    labelmap = {}
    fname = args[1].split('.')[0]+".png"
    with open(args[1], 'r') as program:
        program = program.read().strip().split()
        for word in program:
            if word in roodict:
                ret.append(roodict[word])
            elif word in labelmap:
                ret.append(labelmap[word])
            elif word.isnumeric():
                ret.append(makeInt(int(word)))
            else:
                if label == 27:
                    print("Too many labels!")
                    exit()
                ret.append(makeDigit(label))
                labelmap[word] = makeDigit(label)
                label += 1

        

        output = ''.join(ret).replace('r', 'R')
        writeImg(output, fname)
        print(output)

