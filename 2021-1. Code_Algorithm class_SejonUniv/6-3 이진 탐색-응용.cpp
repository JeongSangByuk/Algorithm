#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

int a, b, n;
char str[100];
int i = 0;

int findElement() {

	int mid;

	while (1) {

		if (a >= b) {
			return a;
		}

		mid = (a + b) / 2;

		if (str[i] == 'N') {
			b = mid;
		}
		else if (str[i] == 'Y') {
			a = mid + 1;
		}
		i++;
	}
}


int main() {

	scanf("%d %d %d", &a, &b, &n);

	scanf("%s", str);

	printf(" %d", findElement());

	return 0;
}