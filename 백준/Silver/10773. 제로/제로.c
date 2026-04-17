#include <stdio.h>

main() {
	int k, tmp, i = 0, sum = 0;
	scanf("%d", &k);
	int* arr = (int*)malloc(sizeof(int) * (k + 1));
	while(k--) {
		scanf("%d", &tmp);
		if (tmp == 0)
			arr[i--];
		else
			arr[i++] = tmp;
	}
	for (int j = 0; j < i; j++)
		sum += arr[j];
	printf("%d", sum);
	free(arr);
}