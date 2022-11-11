# Normal

**Category:** Reversing
**Difficulty:** Easy/Medium
**Author:** puzzler7

## Description

Norse senor snorts spores, abhors non-nors, adores s'mores, and snores.

## Distribution

normal.v, maybe the Makefile?

## Deploy notes

Run `make` to run the file.

## Solution

The `normal` module is an implementation of a few standard gates, using only NOR gates. First, it XORs the input with c1. It then XNORs the result with c2, and returns it. If this result is 0, the flag is correct. Thus, xoring the two constants and bit-negating the result will give the flag.
