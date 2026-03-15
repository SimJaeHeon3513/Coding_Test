#include <stdio.h>

int d(int x){
    int sum = x;
    
    while(x != 0){
    	sum += x % 10;
    	x /= 10;
	}
    return sum;
}

int main(){
	
	int check[10001] = {};
	
	for(int i = 1; i < 10001; i++){
		int num = d(i);
		if(num < 10001){
			check[num] = 1;
		}
	}
	
	for(int i = 1; i < 10001; i++){
		if(check[i] != 1){
			printf("%d\n", i);
		}
	}
}