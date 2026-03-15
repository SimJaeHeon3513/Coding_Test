#include <stdio.h>

int main(){
	int count;
	int max = 0;
	scanf("%d", &count);
	int score[count];
	float avg = 0;
	
	for(int i = 0; i < count; i++){
		scanf("%d", &score[i]);
		if(max < score[i]){
			max = score[i];
		}
	}
	
	for(int i = 0; i < count; i++){
		avg += (float)score[i] / max * 100;
	}
	
	printf("%lf\n", avg / count);
	
	
	
	
}