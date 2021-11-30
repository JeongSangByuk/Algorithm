#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include <time.h>

void inPlaceQuickSort(int left, int right);
int inPlacePartition(int left, int right, int k);
int findPivot(int left, int right);

int* arr;

int main(void)
{

	int n;


	scanf("%d", &n);

	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	inPlaceQuickSort(0, n - 1);

	for (int i = 0; i < n; i++)
		printf(" %d", arr[i]);

	return 0;

}

void inPlaceQuickSort(int left, int right) {

	if (left >= right)
		return;

	int k = findPivot(left, right);
	int pivot = inPlacePartition(left, right, k);
	inPlaceQuickSort(left, pivot - 1);
	inPlaceQuickSort(pivot + 1, right);
}

int inPlacePartition(int left, int right, int k) {

	//pivot의 값
	int p = arr[k];

	//hide pivot
	int tmp = arr[k];
	arr[k] = arr[right];
	arr[right] = tmp;

	int i = left;
	int j = right - 1;

	while (i <= j) {

		while (i <= j && arr[i] <= p)
			i = i + 1;
		while (i <= j && arr[j] >= p)
			j = j - 1;

		if (i < j) {
			int tmp2 = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp2;
		}
	}

	// pivot 바꿔치기.
	int tmp3 = arr[i];
	arr[i] = arr[right];
	arr[right] = tmp3;

	return i;
}

int findPivot(int left, int right) {
	return ((rand() % (right - left + 1)) + left);
}