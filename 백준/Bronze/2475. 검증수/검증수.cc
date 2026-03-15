#include <stdio.h>
#define NUM 5

int main()
{
    int check[NUM] = {0, };
    
    int n;
    int sum = 0;
    
    for(int i = 0; i < NUM; i++){
        scanf("%d", &n);
        check[i] = n * n;
        sum += check[i];
    }
    
    printf("%d", (sum % 10));
    return 0;
}
