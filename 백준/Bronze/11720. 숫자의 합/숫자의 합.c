#include <stdio.h>
main() {
	char a[101];
	int n, sum = 0;
	scanf("%d", &n);
	scanf("%s", &a);
	for (int i = 0; i < n; i++)
		sum += a[i] - '0';
	printf("%d\n", sum);
}