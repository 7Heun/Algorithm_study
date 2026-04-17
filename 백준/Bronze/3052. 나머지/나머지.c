#include <stdio.h>
main() {
	int arr[42] = { 0, }, n, a;
	for (int i = 0; i < 10; i++) {
		scanf("%d", &n);
		arr[n % 42] = 1;
	}
	a = 0;
	for (int i = 0; i < 42; i++)
		a += arr[i];
	printf("%d\n", a);
}