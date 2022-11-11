# It's Not Pwn, I Swear!
**Category:** Reversing
**Difficulty:** Medium
**Author:** puzzler7

## Description

I've made a challenge that's not pwn! Just because it looks like a bird and sings like a bird doesn't mean it's pwn. And good thing it's not pwn, because this binary has full protections (including a canary!).

## Distribution

Players get `notpwn`.

## Deploy notes

No hosting notes. Run `make` to build the file.

## Solution

At first glance, the binary appears to be a classic buffer overflow problem - there's a call to gets, and a `win` function that opens `flag.txt` and prints its contents. However, the fact that this is a reversing challenge, and that it's not hosted, means that this is obviously a red herring.

As the description notes, the binary has full protections, including a canary. This canary is fake - the `__stack_chk_fail` function is actually a wrapper around the actual check for the stack canary. This function takes values off of the stack that would be overwritten by the buffer overflow, and uses them in an LCG, with the seed `d335dr1b` converted to an unsigned long (`b1rd533d` in little-endian). If the first few values are correct, it uses the rest of the values as an xor key and prints the flag.

The appropriate values are `r@n@c3ht` and `d3!ds@hy`, both converted to unsigned longs. As the buffer to be overflowed is 10 bytes long, the input `aaaaaaaaaath3c@n@ryh@sd!3d` will print the flag.
