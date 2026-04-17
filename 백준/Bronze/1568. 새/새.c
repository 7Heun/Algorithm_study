#include <stdio.h>

main() {
	int n, k = 1, sec = 0;
	scanf("%d", &n);
	while (n > 0) {
		if (n >= k) {
			n -= k;
			k++;
			sec += 1;
		}
		else {
			k = 1;
		}
	}
	printf("%d", sec);
}