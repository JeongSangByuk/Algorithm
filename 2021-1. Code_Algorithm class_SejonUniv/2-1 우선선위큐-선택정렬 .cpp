#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

// 오름 차순 정렬
int main() {

	int n, * arr, tmp;

	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = n - 1; i > 0; i--) {

		tmp = i;

		for (int j = i - 1; j >= 0; j--) {
			if (arr[tmp] < arr[j]) {
				tmp = j;
			}
		}

		int temp = arr[i];
		arr[i] = arr[tmp];
		arr[tmp] = temp;
	}

	for (int i = 0; i < n; i++) {
		printf(" %d", arr[i]);
	}




}
