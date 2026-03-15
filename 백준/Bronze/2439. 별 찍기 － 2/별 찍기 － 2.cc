#include <stdio.h>
int main() {
	int a;
	scanf("%d", &a);
	for (int k = 1; k <= a; k++) {
		for (int i = 1; i <= a-k; i++){
			printf(" ");
		}
		for (int j = 1; j <= k; j++) {
			printf("*");
		}
		printf("\n");
	}	
}