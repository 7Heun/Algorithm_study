#include <stdio.h>
main() {
	int n, m = 0;
	float score[1000] = { 0, }, sum = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%f", &score[i]);
		if (score[i] > m)
			m = score[i];
	}
	for (int i = 0; i < n; i++) {
		score[i] = score[i] * 100 / m;
		sum += score[i];
	}
	printf("%.2f\n", sum / n);
}