#include <stdio.h>
#pragma warning(disable:4996) 
int main() {
	int n = 0, subject = 0, sum = 0, count = 0;
	double avg = 0;
	int score[1001];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		
		int sum = 0, count = 0;
		double avg = 0;
		scanf("%d", &subject);

		for (int j = 0; j < subject; j++) {

			scanf("%d", &score[j]);
			sum += score[j];
		}

		avg = ((double)sum / subject);

		for (int k = 0; k < subject; k++) {

			if (score[k] > avg) {
				count++;
			}
		}

		printf("%.3lf%%\n", ((double)count / subject) * 100);
	}
}