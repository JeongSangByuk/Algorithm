#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int n, * arr;
int sortedArray[100];
void rMergeSort(int arr[], int left, int right);
void mergeSort(int arr[]);
void merge(int arr[], int left, int mid, int right);

int main() {

	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	mergeSort(arr);

	// ���� ��� ���
	for (int i = 0; i < n; i++) {
		printf(" %d", arr[i]);
	}

	return 0;
}

void mergeSort(int arr[]) {
	rMergeSort(arr, 0, n - 1);
}

void rMergeSort(int arr[], int left, int right) {

	int mid;

	if (left < right) {
		mid = (left + right) / 2;
		rMergeSort(arr, left, mid);
		rMergeSort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}

}

void merge(int arr[], int left, int mid, int right) {

	int i = left;
	int k = left;

	int j = mid + 1;

	// ���ذ��鼭 �ϳ��� ����
	while (i <= mid && j <= right) {
		if (arr[i] <= arr[j]) {
			sortedArray[k++] = arr[i++];
		}
		else {
			sortedArray[k++] = arr[j++];
		}
	}

	// �����ִ°� �ٺ���
	while (i <= mid) {
		sortedArray[k++] = arr[i++];
	}

	// �����ִ°� �ٺ���
	while (j <= right) {
		sortedArray[k++] = arr[j++];
	}

	// ����.
	for (int t = left; t <= right; t++) {
		arr[t] = sortedArray[t];
	}

}
