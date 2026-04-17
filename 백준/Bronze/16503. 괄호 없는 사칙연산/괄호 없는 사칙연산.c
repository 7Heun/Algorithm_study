#include <stdio.h>

int calculate(int a, char o, int b) {
	int res = 0;
	switch(o) {
	case '+':
		res = a + b;
		break;
	case '-':
		res = a - b;
		break;
	case '*':
		res = a * b;
		break;
	case '/':
		res = a / b;
		break;
	}
	return res;
}

main() {
	int k1, k2, k3;
	char o1, o2;
	int result1 = 0, result2 = 0, tmp;
	scanf("%d %c %d %c %d", &k1, &o1, &k2, &o2, &k3);
	result1 = calculate(calculate(k1, o1, k2), o2, k3);
	result2 = calculate(k1, o1, calculate(k2, o2, k3));
	if (result1 < result2)
		printf("%d\n%d\n", result1, result2);
	else
		printf("%d\n%d\n", result2, result1);
}