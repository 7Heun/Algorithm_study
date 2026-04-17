#include <stdio.h>

main() {
	int check[30] = { 0, };
	for (int i = 0; i < 28; i++) {
		int n;
		scanf("%d", &n);
		check[n - 1] = 1;
	}
	for (int i = 0; i < 30; i++)
		if (check[i] == 0)
			printf("%d\n", i + 1);
}