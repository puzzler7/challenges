#!/usr/bin/env python3

#      b"The flag is ictf{did_you_know_fibonacci_loved_oreos?_740c3751}"
ctxt = b"The flag is ictf{thr33_ch33r5_t0_r00r0bin_th3_b3st_0f_u5_a11_r00h3art_7d2e2642}"

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    ret = fib(n-1)+fib(n-2)
    memo[n] = ret
    return ret

ret = []
for i, ch in enumerate(ctxt):
    ret.append("push {}".format(ch^fib(i)))

print("\n".join(ret[::-1]))
