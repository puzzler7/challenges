# Roolang
**Category:** Reversing
**Difficulty:** Medium/Hard
**Author:** puzzler7

## Description

ELF files are *sooooo* last year :rooVoid:. Instead of making yet *another* ELF to reverse, I made a new type of executable binary for you to reverse :rooYay:! It uses my new language Roolang. Just execute flag.roo to get the flag :rooPuzzlerDevil:! It's dynamically linked, so make sure you have the provided roo library files in the same directory :rooCash:. It's not very optimized, so it might take a moment (sorry about that) :rooNobooli:...

Special shoutout to :rooRobin: and :rooOreos:, who have nothing to do with this challenge, but are both very cool people :rooHeart:. Good luck, and I hope you have fun :rooNervous:!  

## Distribution

Players get all of the .roo files (robin.roo, oreos.roo, blind.roo, imag.roo, nobooli.roo, flag.roo), as well as roolang.py.

## Deploy notes

No hosting notes. `flag.roo` can be created with `./rooify fib.base; mv fib.png flag.roo`

## Solution

The provided roo files are simply pngs. All of the roos aside from flag.roo are 128x128 images of roo emotes from the server, and flag.roo is *many* of these concatenated together. roolang.py takes in flag.roo, and converts it to a string where each character in the string is the first letter of one of the emotes (a letter in "robin"). It then interprets them as a stack-based pseudo-assembly language. This language consists of 5-letter words, each word starting with 'r' and ending with 'n'.

The program flag.roo first pushes a large number of numbers to the stack. It then generates Fibonacci numbers recursively, xors them with the numbers on the stack, and prints the character of the output. Because recursive Fibonacci has an exponential runtime, this takes longer and longer for each character.

To solve, players can decompile the program or dump memory from the stack to get the xor encoded numbers, then simply xor them with Fibonacci numbers to get the flag.
