#include <stdio.h>
main() {
	int a;
	scanf("%d", &a);
	if (a >= 90)
		printf("%s", "A");
	else if (a >= 80)
		printf("%s", "B");
	else if (a >= 70)
		printf("%s", "C");
	else if (a >= 60)
		printf("%s", "D");
	else
		printf("%s", "F");
}