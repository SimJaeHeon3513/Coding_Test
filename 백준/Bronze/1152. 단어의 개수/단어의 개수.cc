#include <stdio.h>
#include <string.h>

int main(){
	char sen[1000001];
	int count = 0;
	scanf("%[^\n]s", sen);
	
	int length = strlen(sen);
	
	if(length == 1){
		if(sen[0] == 32){
			printf("0\n");
			return 0;
		}
	}
	for(int i = 1; i < length; i++){
		if(sen[i] == 32){
			count++;
		} 
	}
	
	if(sen[length-1] == 32){
		count -= 1;
	}
	
	printf("%d\n", count+1);
	
}