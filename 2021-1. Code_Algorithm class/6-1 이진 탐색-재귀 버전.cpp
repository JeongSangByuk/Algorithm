#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include <time.h>
int* arr, n;
int findElement(int k);
int rFindElement(int k, int left, int right);


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
	return rFindElement(k, 0, n - 1);
}

int rFindElement(int k, int left, int right) {

	int mid;

	// if NoSuchKey
	if (left > right) {

		if (arr[right] <= k && k >= 0)
			return right;
		else if (arr[left] >= k && k < 0) {

			if (left == 0)
				return -1;
			return left;
		}
		return -1;
	}

	mid = (left + right) / 2;

	if (k == arr[mid])
		return mid;
	else if (k < arr[mid])
		return rFindElement(k, left, mid - 1);
	else if (k > arr[mid])
		return rFindElement(k, mid + 1, right);
}