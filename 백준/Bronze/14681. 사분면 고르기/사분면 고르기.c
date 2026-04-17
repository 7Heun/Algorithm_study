#include <stdio.h>
main() {
	int a, b;
	scanf("%d\n%d", &a, &b);
	if (a > 0)
		printf("%d", (b > 0) ? 1 : 4);
	else if (a < 0) 
	printf("%d", (b > 0) ? 2 : 3);
}