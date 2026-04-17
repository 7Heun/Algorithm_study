#include <stdio.h>
main() {
	int c, n;
	double ave = 0;
	scanf("%d", &c);
	while (c--) {
		int score[1001] = { 0, }, sum = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &score[i]);
			sum += score[i];
		}
		ave = sum / n;
		double stu = 0;
		for (int i = 0; i < n; i++)
			if (score[i] > ave)
				stu++;
		printf("%.3f%%\n", stu * 100 / n);
	}
}