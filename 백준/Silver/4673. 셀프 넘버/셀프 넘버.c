#include <stdio.h>

int num(int n) {
	int sum = n;
	for (; n > 0; n /= 10)
		sum += n % 10;
	return sum;
}

main() {
	int arr[10001], i, check;
	for (i = 1; i < 10001; i++) {
		check = num(i);
		if (check < 10001)
			arr[check] = 1;
	}
	for (i = 1; i < 10001; i++)
		if (arr[i] != 1)
			printf("%d\n", i);
	return 0;
}