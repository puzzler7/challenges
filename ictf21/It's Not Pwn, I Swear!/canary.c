#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <sys/syscall.h>

void __real___stack_chk_fail(void);

void __wrap___stack_chk_fail(void)
{
    register void *sp asm ("sp");
    char* stack = sp+0x68; //void* stack = sp+0x48;
    // printf("%s\n", (char*)stack);
    // printf("%lx\n", *(unsigned long*)stack);
    // printf("%p\n", stack);
    unsigned long a = *(unsigned long*)stack; 
    unsigned long b = *(unsigned long*)(stack+=8);
    unsigned long x = 7075562264290603876UL; //b1rd533d
    unsigned long* longstack = (unsigned long*) stack;
    *(longstack+1) = 3566538077784527305UL;
    *(longstack+2) = 7330727827507650445UL;
    *(longstack+3) = 3377462976985365597UL;
    *(longstack+4) = 10835700559972133364UL;
    *(longstack+5) = 7949707005276037348UL;
    *(longstack+6) = 9741924779362120173UL;
    *(longstack+7) = 14997418038272762300UL;
    *(longstack+8) = 13613749439049834741UL;
    *(longstack+9) = 15840330290047253419UL;
    *(longstack+10) = 264313207888901860UL;
    // printf("%lx\n", a);
    // printf("%lx\n", b);
    //need to put check values on the stack
    for(int i = 0; i < 3; i++) {
        x = a*x + b;
        // printf("x: %lu\n", x);
        // printf("stack val: %lu\n", *(unsigned long*)(longstack+1));
        if (x - *(unsigned long*)(longstack+=1)) __real___stack_chk_fail();
        // for (int j = 0; j < 8; j++) {
        //     if ((*(&x+j))-*(unsigned long*)(stack+=1)) {
        //         __real___stack_chk_fail();
        //     }
        // }
    }
    for(int i = 0; i < 7; i++) {
        x = a*x + b;
        unsigned long out = x^(*(unsigned long*)(longstack+=1));
        syscall(1, 1, &out, sizeof(out));
    }
    exit(0);
    //__real___stack_chk_fail();
}

void win() {
    FILE* f = fopen("flag.txt", "r");
    char flag[50];
    fscanf(f, "%s", flag);
    printf("Great job! Here's the flag: %s\n", flag);
    fclose(f);
}

void vuln() {
    char buf[10];
    printf("This is not a pwn challenge.\nEnter your input: ");
    gets(buf);
    return;
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    vuln();
}

