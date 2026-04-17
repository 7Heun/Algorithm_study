#include <stdio.h>
main() {
	int n, *arr;
	long min = 1000001, max = -1000001;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (int j = 0; j < n; j++) {
		if (arr[j] < min)
			min = arr[j];
		if (arr[j] > max)
			max = arr[j];
	}
	printf("%d %d", min, max);
}