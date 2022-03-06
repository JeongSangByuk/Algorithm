#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int n, k;

int main() {

	int N[40][40];

	for (int i = 0; i < 40; i++)
		N[0][i] = 0;

	for (int i = 0; i < 40; i++)
		N[i][0] = 1;

	for (int i = 0; i < 40; i++) {
		for (int j = 0; j < 40; j++) {

			if (i < 1 || j < 1)
				continue;

			N[i][j] = N[i - 1][j] + N[i - 1][j - 1];
		}
	}

	scanf("%d %d", &n, &k);

	printf("%d", N[n][k]);

	return 0;
}

