#include <stdio.h>
main() {
	int n, tmp = 0, ten, one, sum = 0, cnt = 0;
	scanf("%d", &n);
	tmp = n;
	while (1) {
		ten = (tmp < 10) ? 0 : tmp / 10;
		one = tmp % 10;
		sum = ten + one;
		tmp = one * 10 + sum % 10;
		cnt++;
		if (tmp == n)
			break;
	}
	printf("%d", cnt);
}