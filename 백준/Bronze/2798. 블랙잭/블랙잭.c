#include <stdio.h>

main() {
	int n, m, arr[100];
	int res = 0, sum = 0;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			for (int k = j + 1; k < n; k++) {
				sum = arr[i] + arr[j] + arr[k];
				if (sum <= m && res < sum)
					res = sum;
			}
	printf("%d", res);
}