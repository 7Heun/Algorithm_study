#include <stdio.h>

main() {
	int a[8];
	int asc = 1, des = 1;
	for (int i = 0; i < 8; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < 8; i++) {
		if (a[i] != i + 1) {
			asc = 0;
			break;
		}
	}
	for (int i = 0; i < 8; i++){
		if (a[i] != 8 - i) {
			des = 0;
			break;
		}
	}
	if (asc == 1)
		printf("ascending");
	else if (des == 1)
		printf("descending");
	else
		printf("mixed");
}