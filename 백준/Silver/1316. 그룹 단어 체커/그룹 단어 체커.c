#include <stdio.h>
#include <string.h>
int check(char arr[]) {
	for (int i = 0; i < strlen(arr); i++) {
		for (int j = 0; j < strlen(arr); j++) {
			if (arr[i] == arr[j])
				if (j - i > 1)
					if (arr[j - 1] != arr[j])
						return 0;
		}
	}
	return 1;
}
main() {
	int n, sum = 0;
	char arr[100];
	scanf("%d", &n);
	while (n--) {
		scanf("%s", arr);
		sum += check(arr);
	}
	printf("%d\n", sum);
}