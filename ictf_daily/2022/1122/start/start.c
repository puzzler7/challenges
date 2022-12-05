#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char user_type[] = "nonadmin";
char flag[128];

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    char name[64];
    FILE* file = fopen("./flag.txt", "r");
    fscanf(file, "%s", flag);

    printf("What's your name? ");
    fgets(name, 2*sizeof(name), stdin);
    for (int i = 0; i < sizeof(name); i++) {
        if (name[i] == '\n') {
            name[i] = '\0';
            break;
        }
    }
    if (strcmp(user_type, "admin")) {
        printf("Hi %s! It doesn't look like you're an admin. Try again later!\n", name);
    } else {
        puts(flag);
    }
    return 0;
}