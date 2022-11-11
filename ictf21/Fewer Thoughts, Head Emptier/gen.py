#!/usr/bin/env python3
from math import sqrt, floor
from primefac import primefac

def bad(num):
    if num == 0:
        return ''
    sign = 1*(num>0)
    op = '+' if num > 0 else '-'
    nop = '-' if num > 0 else '+'
    num = abs(num)
    try:
        p = list(primefac(num))[-1]
    except: 
        p = num
    q = num//p  
    p, q = (p, q) if p < q else (q, p)
    ret = '>'+op*p+'[<'+op*q+'>'+nop+']'
    return ret

def make(num):
    if num == 0:
        return ''
    sign = 1*(num>0)
    op = '+' if num > 0 else '-'
    nop = '-' if num > 0 else '+'
    num = abs(num)
    cnt = 0
    while num!= floor(sqrt(num))*floor(sqrt(num)):
        # print(num)
        num += 1
        cnt += 1
    p = int(sqrt(num))
    q = num//p  
    p, q = (p, q) if p < q else (q, p)
    ret = '>'+op*p+'[<'+op*q+'>'+nop+']'
    if cnt != 0:
        ret += '<'+bad(-1*sign*cnt)
    return ret


if __name__ == '__main__':
    flag = 'ictf{th3_l3s5_th0ugh+_+he_b3teR}'
    ret = [ord(flag[0])]
    for i, c in enumerate(flag[1:]):
        ret.append(ord(c)+sum(range(ord(flag[i])+1)))

    out = '>>>'

    print(ret)

    for num in ret:
        out += make(num)+"\n"

    out += '>'+make(len(flag))

    out = out.replace('<>', '').replace('><', '')

    print(out)

