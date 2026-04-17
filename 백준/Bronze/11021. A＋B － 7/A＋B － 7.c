#include <stdio.h>
main() {
	int t, a, b;
	scanf("%d", &t);
	for (int i = 1; t > 0; t-- && i++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i, a + b);
	}
}