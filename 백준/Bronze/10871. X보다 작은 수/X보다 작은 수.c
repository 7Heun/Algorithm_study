#include <stdio.h>
main() {
	int n, x, input;
	scanf("%d %d", &n, &x);
	while(n--) {
		scanf("%d", &input);
		if (input < x)
			printf("%d ", input);
	}
}