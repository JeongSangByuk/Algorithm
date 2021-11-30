#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

int main() {

	int n, * arr, tmp;

	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 1; i < n; i++) {

		int tmp = arr[i];
		int j = i - 1;

		while ((j >= 0) && (arr[j] >= tmp)) {
			//한칸씩 뒤로 밀기.
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = tmp;

	}

	for (int i = 0; i < n; i++) {
		printf(" %d", arr[i]);
	}




}
