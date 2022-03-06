#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include <time.h>
int* arr, n;
int findElement(int k);


int main() {

	int k;

	scanf("%d %d", &n, &k);

	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	printf(" %d", findElement(k));
}

int findElement(int k) {

	int left, right, mid;
	left = 0;
	right = n - 1;

	while (1) {

		//printf("%d %d\n", left, right);
		if (left > right) {

			if (k >= 0 && arr[right] <= k) {

				if (left == n)
					return n;

				return left;
			}
			else if (k <= 0 && arr[left] >= k) {
				return left;
			}

			break;
		}

		mid = (left + right) / 2;

		if (k == arr[mid]) {
			return mid;
		}

		else if (k < arr[mid]) {
			right = mid - 1;
		}

		else if (k > arr[mid]) {
			left = mid + 1;
		}
	}
}
