#include <stdio.h>
#pragma warning(disable:4996)

int main() {
	int a;
	scanf("%d", &a);
	
	int b = a;
	int count = 0;

	while (1) {
		a = (a / 10 + a % 10) % 10 + a % 10 * 10;
		count++;
		if (a == b)
		{
			printf("%d", count);
			break;
		}
	}
}