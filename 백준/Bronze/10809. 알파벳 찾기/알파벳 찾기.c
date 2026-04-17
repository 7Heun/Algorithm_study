#include <stdio.h>

main() {
	char s[101];
	char* p = &s;
	int check[26];
	for (int i = 0; i < 26; i++)
		check[i] = -1;
	scanf("%s", p);
	for (int i = 0; *p != '\0'; i++, p++) {
		if (check[*p - 'a'] != -1)
			continue;
		check[*p - 'a'] = i;
	}
	for (int i = 0; i < 26; i++)
		printf("%d ", check[i]);
}