#include <stdio.h>

int main(){
    
    int a;
    
    scanf("%d\n", &a);
    int num[a] = {};
    for(int i = 0; i < a; i++){
        scanf("%d", &num[i]);
    }
    int max = num[0];
    int min = num[0];
    for(int i = 0; i < a; i++){
        if(max < num[i]){
            max = num[i];
        }
        if(min > num[i]){
            min = num[i];
        }
    }
    
    printf("%d %d", min, max);
    
    
}