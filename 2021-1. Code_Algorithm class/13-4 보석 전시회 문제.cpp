#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int n, k;
int* arr, * g;

void sort() {
	int tmp;

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
}

int main() {

	scanf("%d %d", &n, &k);
	arr = (int*)malloc(sizeof(int) * n);


	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	sort();

	int max = arr[n - 1];

	int* arr2 = (int*)malloc(sizeof(int) * max);
	g = (int*)malloc(sizeof(int) * max);


	int tmp = 0;
	for (int i = 0; i < max; i++) {
		g[i] = 0;
		if (arr[tmp] - 1 == i) {
			arr2[i] = arr[tmp];
			tmp++;
		}
		else {
			arr2[i] = -1;
		}
	}

	for (int i = 0; i < max; i++) {
		printf(" %d", arr2[i]);
	}

	int count = 0;
	int isQ = 0;
	for (int i = 0; i < max; i++) {

		if (isQ == 1)
			break;

		if (arr2[i] > max) {
			break;
		}

		if (arr2[i] != -1 && g[arr2[i] - 1] == 0) {

			// 경비 배치
			for (int x = 0; x < 2*k + 1; x++) {

				if (arr2[i] + x > max) {
					isQ = 1;
					break;
				}

				g[arr2[i] + x - 1] = 1;
			}
			count++;
		}

	}

	printf("\n");
	for (int i = 0; i < max; i++) {
		printf(" %d", g[i]);
	}

	printf("\n%d", count);

	return 0;
}

