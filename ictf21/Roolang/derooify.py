#!/usr/bin/env python3

import sys

# push, pop, add, sub, mult, div, mod, andd, orr, xorr, dupe, swap, reg, pr, prn, label, jump, jnz, ret, jal

words = ['push', 'pop', 'add', 'sub', 'mult', 'div', 'mod', 'andd', 'orr', 'xorr', 'dupe', 'swap', 'reg', 'pr', 'prn', 'label', 'jump', 'jnz', 'ret', 'jal']

newlineWords = ['pop', 'add', 'sub', 'mult', 'div', 'mod', 'andd', 'orr', 'xorr', 'dupe', 'swap', 'reg', 'pr', 'prn', 'ret']

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

def parseInt(s):
    words = [s[i:i+5] for i in range(0, len(s), 5)]
    ret = 0
    for i in range(parseDigit(words[0])):
        ret += parseDigit(words[i+1])
        ret *= 27
    return ret//27

def parseDigit(s):
    return int(s.replace('o', '0').replace('b', '1').replace('i', '2')[1:-1], 3)

def invert(d):
    ret = {}
    for key in d:
        ret[d[key]] = key
    return ret

plaindict = invert(roodict)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Usage: ./derooify.py [filename]")

    ret = []
    label = 0
    labels = []
    lastpush = 0
    lastlabel = 0
    with open(args[1], 'r') as program:
        program = program.read().strip().lower()
        program = [program[i:i+5] for i in range(0, len(program), 5)]
        insn_pointer = 0
        while insn_pointer < len(program):
            word = program[insn_pointer]
            if lastlabel:
                lastlabel = 0
                if word in labels:
                    ret.append(str(labels.index(word)))
                else:
                    ret.append(str(label))
                    labels.append(word)
                    label += 1
            elif lastpush and (word not in plaindict or plaindict[word] != 'reg'):
                lastpush = 0
                toParse = word
                for i in range(parseDigit(word)):
                    insn_pointer += 1
                    toParse += program[insn_pointer]
                ret.append(str(parseInt(toParse)))
            elif word in plaindict:
                ret.append(plaindict[word])
                if plaindict[word] == "push":
                    lastpush = 1
                if plaindict[word] in ["label", "jump", "jal", "jnz"]:
                    lastlabel = 1
                if lastpush and plaindict[word] == 'reg':
                    lastpush = 0
            elif word in labels:
                lastlabel = 0
                ret.append(str(labels.index(word)))
            else:
                lastlabel = 0
                ret.append(str(label))
                labels.append(word)
                label += 1

            insn_pointer += 1

        nextline = 0
        for i, word in enumerate(ret):
            if word in newlineWords or nextline:
                nextline = 0
                ret[i] += '\n'
            else:
                nextline = 1

        output = ' '.join(ret)
        print(output)

