#include <stdio.h>

int reverse(int n) {
	int res = n / 100;
	n = n % 100;
	res += n / 10 * 10;
	n = n % 10;
	res += n * 100;
	return res;
}

main() {
	int a, b;
	scanf("%d %d", &a, &b);
	a = reverse(a);
	b = reverse(b);
	printf("%d", (a > b ? a : b));
}