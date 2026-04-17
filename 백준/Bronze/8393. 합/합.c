#include <stdio.h>
main() {
	int n, a;
	scanf("%d", &n);
	for (a = 0; n > 0; n--)
		a += n;
	printf("%d", a);
}