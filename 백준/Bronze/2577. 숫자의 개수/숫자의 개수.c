#include <stdio.h>
main() {
	int a, b, c, num = 0;
	int res = 1;
	int arr[10] = { 0, };
	scanf("%d %d %d", &a, &b, &c);
	res = a * b * c;
	for (int i = 0; res > 0; i++) {
		num = res % 10;
		arr[num] += 1;
		res /= 10;
	}
	for (int i = 0; i < 10; i++)
		printf("%d\n", arr[i]);
}