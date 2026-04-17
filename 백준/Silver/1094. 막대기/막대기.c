#include <stdio.h>
main() {
	int x, stick = 0;
	scanf("%d", &x);
	while (x > 0) {
		if (x & 1)
			stick++;
		x >>= 1;
	}
	printf("%d\n", stick);
}