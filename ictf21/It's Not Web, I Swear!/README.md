# It's Not Web, I Swear
**Category:** Pwn
**Difficulty:** Easy/Medium/Hard
**Author:** puzzler7

## Description

In the spirit of DEFCON, I present you with this challenge that is not a web challenge! Go forth and pwn this notweb challenge. (The flag is not in `flag.txt`.)

## Distribution

`server`, website link

## Deploy notes

Run "make run" to build the file and host it on port 1500. This is gonna need a Dockerfile, but I'm too tired to figure that right now. Is a reverse shell even possible with a redpwn jail?

## Solution

The provided file is a custom c webserver, with a buffer overflow in `respond`. The `jmp rsp` gadget is available in the file, so the payload `"GET / " + filler + jmp_rsp + shellcode + " HTTP"` will jump to the shellcode. One caveat is that the filler must be null bytes, as some of the overwritten variables on the stack get freed, and freeing NULL does nothing, while freeing random data will segfault.

A reverse shell shellcode will let you connect to the server and cat the_real_flag.txt.
