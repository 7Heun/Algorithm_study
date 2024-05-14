#include <stdio.h>
#include <string.h>
main() {
	int n;
	char arr[81];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int score = 0, add = 1;
		scanf("%s", arr);
		for (int j = 0; j < strlen(arr); j++) {
			if (arr[j] == 'O') {
				score += add;
				add++;
			}
			else
				add = 1;
		}
		printf("%d\n", score);
	}
}