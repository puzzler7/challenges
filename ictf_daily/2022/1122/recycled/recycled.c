#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Employee {
    char user[50];
    char pass[50];
    struct Employee* next;
} emp;

emp* users = NULL;
emp* currentUser = NULL;
char dead;

void enterEmployee(emp* a) {
    printf("Username: ");
    fgets(a->user, sizeof(a->user), stdin);
    printf("Password: ");
    fgets(a->pass, sizeof(a->pass), stdin);
    if (strtok(a->user, "\n") != NULL) {
        strcpy(a->user, strtok(a->user, "\n"));
    } else {
        a->user[0] = ' ';
    }
    if (strtok(a->pass, "\n") != NULL) {
        strcpy(a->pass, strtok(a->pass, "\n"));
    } else {
        a->pass[0] = ' ';
    }
    strcpy(a->pass, strtok(a->pass, "\n"));
    printf("\n");
}

emp* findUser(emp* a) {
    emp* curr = users;
    while (curr != NULL) {
        if (strcmp(a->user, curr->user)){
            curr = curr->next;
        } else {
            break;
        }
    }
    return curr;
}

emp* findUserBefore(emp* a) {
    if (!strcmp(a->user, users->user)) {
        return NULL;
    }
    emp* curr = users;
    int found = 0;
    while (curr->next != NULL) {
        if (strcmp(a->user, curr->next->user)){
            curr = curr->next;
        } else {
            found = 1;
            break;
        }
    }
    if (!found) {
        curr = NULL;
    }
    return curr;
}

void login() {
    emp* a = malloc(sizeof(emp));
    enterEmployee(a);
    int success = 1;
    if (!strncmp(a->user, "admin", 5)){
        success = 0;
        printf("Cannot login as admin from this location!\n");
    }
    emp* dbUser = findUser(a);
    if (dbUser == NULL || strcmp(dbUser->pass, a->pass)) {
        success = 0;
        printf("Invalid Credentials.\n");
    }
    if (success) {
        currentUser = dbUser;
        printf("Login success!\n");
    }
    free(a);
}

void createAcc() {
    emp* a = malloc(sizeof(emp));
    enterEmployee(a);
    emp* tail = users;
    while (tail->next != NULL) {
        tail = tail->next;
    }
    tail->next = a;
    a->next = NULL;
    printf("Account creation success! Please login as your new account.\n");
}

void deleteUser() {
    emp* a = malloc(sizeof(emp));
    enterEmployee(a);
    emp* dbUser = findUserBefore(a);
    if (dbUser == NULL) {
        printf("Could not delete user, either because user is admin or does not exist!\n");
    } else if (strcmp(dbUser->next->user, a->user)) {
        printf("Invalid Credentials.\n");
    }
    else {
        emp* delUser = dbUser->next;
        dbUser->next = dbUser->next->next;
        printf("User %s successfully deleted!\n", delUser->user);
        free(delUser);
    }
    free(a);
}

void getFlag(){
    if (currentUser == NULL || strncmp(currentUser->user, "admin", 5)) {
        printf("Only admins can access this!\n");
        return;
    }
    FILE* f = fopen("flag.txt", "r");
    char flag[50];
    fscanf(f, "%s", flag);
    printf("Flag: %s\n", flag);
    fclose(f);
    exit(0);
}

void menu() {
    printf("\n================================================================================\n");
    if (currentUser != NULL) {
        printf("Hello %s!\n", currentUser->user);
        printf("Welcome back to the Recycling Plant!\n");
        printf("1: Change User\n");
    } else {
        printf("Welcome to the Recycling Plant!\n");
        printf("1: Login\n");
    }
    printf("2: Create Account\n");
    printf("3: Delete User\n");
    printf("4: Get Flag\n\n>>> ");
    unsigned int choice;
    scanf("%d%c", &choice, &dead);
    if (choice == 1) {
        login();
    } else if (choice == 2) {
        createAcc();
    } else if (choice == 3) {
        deleteUser();
    } else if (choice == 4) {
        getFlag();
    } else {
        printf("Invalid choice.\n");
    }
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    users = malloc(sizeof(emp));
    strcpy(users->user, "username");
    strcpy(users->pass, "password");
    users->next = NULL;
    while(1) {
        menu();
    }
}