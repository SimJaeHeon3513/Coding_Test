#include <stdio.h>

int main(){
    int n, sum = 0;
    scanf("%d", &n);
    int num[n];
    
    for(int i = 0; i < n; i++){
    	scanf("%1d", &num[i]);
    	sum += num[i];
	}
	
	printf("%d", sum);
    
}