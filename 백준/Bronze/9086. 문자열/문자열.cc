#include <stdio.h>
#include <string.h>

int main(){
    int T;
    char word[1000];
    char f, l;
    scanf("%d", &T);
    
    for(int i = 0; i < T; i++){
        scanf("%s", word);
        int len = strlen(word);
        f = word[0];
        l = word[len-1];
        
        printf("%c%c\n", f, l);
    }
}