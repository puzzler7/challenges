#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define bitlen 8

char dead = 0;
unsigned long val = 2;
unsigned long x[88] = {253, 60, 196, 14, 118, 255, 75, 69, 31, 64, 244, 230, 128, 184, 181, 232, 118, 142, 59, 248, 228, 189, 201, 199, 63, 230, 207, 21, 148, 154, 138, 40, 78, 94, 30, 63, 37, 212, 44, 169, 54, 40, 66, 64, 147, 141, 15, 255, 174, 43, 43, 223, 126, 26, 78, 5, 99, 208, 136, 225, 161, 31, 90, 61, 54, 79, 174, 137, 123, 215, 39, 208, 41, 192, 158, 240, 32, 223, 105, 119, 148, 233, 88, 15, 184, 236, 249, 36};
int count;

int test(int n) {
    if (n==1) return 0;
    for (int i = 2; i < n-1; i++) {
        if (n%i == 0) {
            return 0;
        }
    }
    return 1;
}

unsigned long next(unsigned long val){
    for(int i = 0; i < bitlen; i++) {
        unsigned long bit = 0;
        unsigned long temp = val;
        for (int j = 0; j < bitlen; j++) {
            if (test(j+1)){
                bit ^= temp&1;
            }
            temp >>= 1;
        }
        val >>= 1;
        val += bit << (bitlen-1);
    }
    return val;
}

void c(){
    puts("C!");
    sleep(1);
}

void o(int arg){
    if (arg == 0x1337c0d3) {
        puts("O!");
        sleep(1);
    }
}

void r(){
    puts("R!");
    sleep(1);
}

void e(){
    puts("E!");
    sleep(1);
}

void t(int arg){
    if (arg == 0xdeadface) {
        puts("T!");
        sleep(1);
    }
}

int checkFlag() {
    char stack[0];
    printf(">>> ");
    scanf("%88s%c", &(stack[8]), &dead);
    for (count = 8; count < 88+8; count ++) {
        val = next(val);
        stack[count] ^= x[count-8]^val;
    }
    return 0;
}

int main() {
    puts("Ice cream!");
    puts("Soda Pop!");
    puts("Cherry on top!");
    puts("Is your flag exact?");
    puts("Well, let's find out!");
    sleep(1);
    puts("\nEighty-eight characters!");
    puts("A secret well kept!");
    puts("If you get it right,");
    puts("I'll shout CORRECT!\n");
    if (!checkFlag()) {
        printf("Nope!");
    }
    return 0;
}