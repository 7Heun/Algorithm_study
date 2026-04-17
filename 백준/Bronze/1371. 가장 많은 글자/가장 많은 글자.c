#include <stdio.h>
#include <string.h>

main() {
	char s[5001];
	int count[26] = { 0 };
	int max = 0;
	while (gets(s)) {
		for (int i = 0; i < strlen(s); i++)
			if (s[i] >= 'a' && s[i] <= 'z')
				count[s[i] - 'a']++;
	}
		for (int i = 0; i < 26; i++)
			if (count[i] > max)
				max = count[i];
		for (int i = 0; i < 26; i++)
			if (count[i] == max)
				printf("%c", i + 'a');
	return 0;
}