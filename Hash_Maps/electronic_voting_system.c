#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 128

typedef struct VOTE{
    char name[10];
    int votes;
}VOTE;  

typedef struct ENTRY{
    char name[12];
    int votes;
} ENTRY;

ENTRY table[TABLE_SIZE] = {0};

int hash(char * s){
    int sum = 0;
    for(int i = 0; i < strlen(s); i++){
        sum += s[i];
    }
    return sum % TABLE_SIZE;
}



void add_vote(const char *name, int count) {
    unsigned int idx = hash(name);
    
    while (table[idx].name[0] != '\0') {
        if (strcmp(table[idx].name, name) == 0) {
            table[idx].votes += count;
            return;
        }
        idx = (idx + 1) % TABLE_SIZE;
    }
    

    strcpy(table[idx].name, name);
    table[idx].votes = count;
}



int main(){
    int n;
    scanf("%d", &n);
}