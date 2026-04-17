#include <stdio.h>
main() {
	int h, m;
	scanf("%d %d", &h, &m);
	if ((m -= 45) < 0) {
		m += 60;
		if (--h<0) h += 24;
	}
	printf("%d %d", h, m);
}