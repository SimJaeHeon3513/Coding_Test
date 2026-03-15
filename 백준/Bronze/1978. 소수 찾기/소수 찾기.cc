#include <stdio.h>

int main() {
    int N, num;
    int count = 0;
    
    scanf("%d", &N);
    int i;
    while(N--){
        
        scanf("%d", &num);
        for(i = 2; i < num; i++){
            if((num % i == 0)){
                break;
            }
        }
        if(i == num){
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}