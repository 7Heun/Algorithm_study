#include <stdio.h>
main() {
	int idx = 0, j;
	int arr[9] = { 0 };
	long max = 0;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &arr[i]);
		if (arr[i] > max) {
			max = arr[i];
			idx = i + 1;
		}
	}
	printf("%d\n%d", max, idx);
}