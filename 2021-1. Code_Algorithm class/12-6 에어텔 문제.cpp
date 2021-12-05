#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int n;
int* A, * H;

// 분할 통치
int rAirtel(int d) {

	if (d == 0)
		return 0;

	int minCost = 100000;
	int cost;

	for (int k = 0; k < d; k++) {
		cost = rAirtel(k) + H[k] + A[d - k];
		if (minCost > cost)
			minCost = cost;
	}
	return minCost;
}

// DP : 재귀 X
int airtel(int n) {

	int cost;

	// m배열은 도시0에서 d로가는 최소비용을 저장.
	int* m = (int*)malloc(sizeof(int) * n);
	m[0] = 0;

	for (int d = 1; d < n; d++) {
		m[d] = 100000;

		for (int k = 0; k < d; k++) {
			cost = m[k] + H[k] + A[d - k];
			if (m[d] > cost)
				m[d] = cost;
		}
	}

	return m[n - 1];
}

int main() {

	scanf("%d", &n);
	A = (int*)malloc(sizeof(int) * n);
	H = (int*)malloc(sizeof(int) * n);

	for (int i = 1; i < n; i++) {
		scanf("%d", &A[i]);
	}
	A[0] = 0;

	for (int i = 1; i < n - 1; i++) {
		scanf("%d", &H[i]);
	}
	H[0] = 0;
	H[n - 1] = 0;

	// 분할 통치
	//printf("%d", rAirtel(n-1));

	// dp
	printf("%d", airtel(n));

	return 0;
}

