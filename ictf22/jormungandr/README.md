# Jormungandr
**Category:** Reversing
**Difficulty:** Medium
**Author:** puzzler7

## Description

It's said that the great serpent Jormungandr encircles the world, devouring his own tail. When he ceases, he will devour the world itself, leaving nothing behind.

## Distribution

- jormungandr

## Deploy notes

n/a

## Solution

The provided file is the interpreter for an esolang, and it is also the source file. It splits itself by spaces, and treats each word as an instruction (with many of them simply nops). The flag checking is rather simple - it takes the provided hex, raises it to a large power and adds a prime, which can be easily reversed. 
