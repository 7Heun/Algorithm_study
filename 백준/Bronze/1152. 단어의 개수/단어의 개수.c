#include<stdio.h>
#include <string.h>
main() {
	char sen[1000000];
	int word = 0;
	scanf("%[^\n]s", sen);
	for (int i = 0; i < strlen(sen); i++)
		if (sen[i] == ' ')
			word++;
	if (sen[0] == ' ')
		word -= 1;
	if (sen[strlen(sen) - 1] == ' ')
		word -= 1;
	printf("%d", word+1);
}