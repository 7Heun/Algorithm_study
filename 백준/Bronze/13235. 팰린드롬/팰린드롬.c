#include <stdio.h>
#include <string.h>

int is_palindrome(char arr[], int len) {	
	for (int i = 0; i < len / 2; i++)
		if (arr[i] != arr[len - i - 1])
			return 0;
	return 1;
}

main() {
	char s[21];
	scanf("%s", s);
	is_palindrome(s, strlen(s)) == 0 ? printf("false\n") : printf("true\n");
}