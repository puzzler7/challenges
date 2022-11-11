# Jumprope
**Category:** Reversing
**Difficulty:** Medium
**Author:** puzzler7

## Description

CENSORED and CENSORED
Sitting in a tree,
H-A-C-K-I-N-G!
First comes pwn,
Then comes rev,
Then comes a flag
And a happy dev!

## Distribution

* `jumprope`

## Deploy notes

N/A. Use make to build the file.

## Solution

The initial print indicates that the binary will print "CORRECT" when the correct flag is input, but there is no code in the checkFlag function that does this. However, there are functions that will print the individual letters in the word. This, combined with the fact that the checkFlag function writes the flag to the stack in a buffer overflow, indicates that you are supposed to ROP the binary to print "CORRECT".

The program takes the input, xors each byte with a constant from an array, and a psuedorandom value. The pseudorandom value is a LFSR with prime bits xored to create the next bit. This function can be rewritten to get the values, or the values can be extracted dynamically from the binary when it runs. Thus, as the player knows the length of the flag, they can take a ROP exploit to run through all the functions, and xor it with these values to get the flag. As the flag is mostly normal english, and is a line from a jumprope rhyme (with the word "robbers" changed to "hackers"), it can be reconstructed from context if parts of the exploit differ from my implementation (e.g. if a different pop_rdi gadget is used).
