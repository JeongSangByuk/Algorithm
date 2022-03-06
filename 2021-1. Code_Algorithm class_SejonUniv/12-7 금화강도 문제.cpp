#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int arr[4][4];

int n = 4;
int max = 100000;

int min(int a, int b) {

	if (a < b)
		return a;
	return b;

}

// 분할 통치
int minGold(int i, int j) {

	if((i == 0) && (j == 0))
		return arr[0][0];

	int minRight = max;
	int minDown = max;
	int cost;

	for (int k = j - 1; k >= 0; k--) {
		cost = minGold(i, k) + arr[i][j];

		minRight = min(minRight, cost);
	}

	for (int k = i - 1; k >= 0; k--) {
		cost = minGold(k,j) + arr[i][j];
		minDown = min(minDown, cost);
	}

	return min(minRight, minDown);
}

// DP
int minGold2() {

	int m[4][4];
	int minRight, minDown,cost;

	m[0][0] = arr[0][0];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {

			if ((i == 0) && (j == 0))
				continue;

			minRight = max;
			minDown = max;

			for (int k = j - 1; k >= 0; k--) {
				cost = m[i][k] + arr[i][j];
				minRight = min(minRight, cost);
			}

			for (int k = i - 1; k >= 0; k--) {
				cost = m[k][j] + arr[i][j];
				minDown = min(minDown, cost);
			}

			m[i][j] = min(minRight, minDown);
		}
	}

	return m[n - 1][n - 1];
}

int main() {

	arr[0][0] = 1;
	arr[0][1] = 3;
	arr[0][2] = 7;
	arr[0][3] = 12;

	arr[1][0] = 6;
	arr[1][1] = 2;
	arr[1][2] = 3;
	arr[1][3] = 4;
	
	arr[2][0] = 11;
	arr[2][1] = 4;
	arr[2][2] = 6;
	arr[2][3] = 8;

	arr[3][0] = 20;
	arr[3][1] = 8;
	arr[3][2] = 8;
	arr[3][3] = 11;

	printf("%d\n", minGold(n - 1, n - 1));
	printf("%d", minGold2());

	return 0;
}

