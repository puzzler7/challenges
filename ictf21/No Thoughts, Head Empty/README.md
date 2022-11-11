# No Thoughts, Head Empty
**Category:** Reversing
**Difficulty:** Medium/Hard
**Author:** puzzler7

## Description

When I was making Roolang, of course I took a look at the mother of all esolangs! So, have some bf code. Run it here (https://copy.sh/brainfuck/) with 32 bit cells and dynamic memory enabled. Run the program to get the flag, and then some.

## Distribution

Players get `flag_min.bf`

## Deploy notes

N/A

## Solution

There's a few ways to solve this. The easiest is noticing that the first chunk of the file executes very quickly, and the execution time is mostly spent in the loop(s) at the end. Removing the last loop and looking at the memory will show the flag in ascii codes. This can also be realized by formatting to show loop nest depth, and that the only nested loop is at the end.

The most magical way to solve this is to replace the only run of exactly 2 plus signs with 1 plus sign. This will print the flag, as it prints each character 1 time, rather than doubling it each time.

Of the provided files, `flag.bf` is the original commented source. `flag_patch.bf` is `flag.bf` with the "magical" patch above applied (the changed line is marked). `gen.py` generates code to store a string in memory.
