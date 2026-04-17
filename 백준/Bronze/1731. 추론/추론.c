#include <stdio.h>

main() {
	int n, p[50], q;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &p[i]);
	if (p[1] - p[0] == p[2] - p[1])
		printf("%d", p[n - 1] + (p[1] - p[0]));
	else
		printf("%d", p[n - 1] * (p[1] / p[0]));
}