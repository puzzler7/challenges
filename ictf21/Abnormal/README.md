# Abnormal

**Category:** Reversing
**Difficulty:** Medium
**Author:** puzzler7

## Description

"Nors galore, more and more!", I swore, "Ignore xor, no ors anymore!" In short, neither xor nor or's required, for four more nors restores your xor. 

## Distribution

abnormal.v, possibly the Makefile

## Deploy notes

Run make to run the file

## Solution

Nora implements a full adder with only nor gates. This can be seen by exhaustively testing all 8 possible inputs. Norb combines 16 of these to make a 16 bit adder, and norc combines 16 of those to make a 256 bit adder. Abnormal adds a constnant to the flag, and adds two other constants together. These are then xored. If the output is 0 (i.e. the sums are the same), "Correct!" is printed.
