#include <stdio.h>
main() {
	int n, a, b;
	scanf("%d", &n);
	for (; n > 0; n--) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
}