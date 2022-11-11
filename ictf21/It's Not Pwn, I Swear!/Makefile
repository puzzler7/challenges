all:
	gcc -fstack-protector-strong -c canary.c
	gcc -Wl,-z,now,--wrap=__stack_chk_fail -o temp canary.o 
	sed 's/__wrap___stack_chk_fail/__stack_chk_fail\x00\x00\x00\x00\x00\x00\x00/' temp > notpwn
	rm -f temp
