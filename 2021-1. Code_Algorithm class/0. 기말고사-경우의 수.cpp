#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

int n, k;
int* arr;
int* result;

int m = 8001;
int cnt = 0;

int findElement(int k);
void initBucketArray();
int getNextBucet(int v, int i);
void insertItem(int k);

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

	int n;

	scanf("%d", &n);

	arr = (int*)malloc(sizeof(int) * n);
	result = (int*)malloc(sizeof(int) * m);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	initBucketArray();
	int tmp;

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < n; j++) {

			for (int x = 0; x < n; x++) {

				for (int y = 0; y < n; y++) {

					tmp = arr[i] + arr[j] +
						arr[x] + arr[y];

					insertItem(tmp);
				}
			}
		}
	}

	printf("%d", cnt);

	return 0;
}

int h(int x) {
	return x % m;
}

void insertItem(int k) {

	if (result[k] == 0) {
		result[k] = k;
		cnt++;
	}
}

int getNextBucet(int v, int i) {
	return ((v + i) % m);
}

void initBucketArray() {
	for (int i = 0; i < m; i++) {
		result[i] = 0;
	}
}

int findElement(int k) {
	int v = h(k);
	int i = 0;

	while (i < m) {
		int b = getNextBucet(v, i);

		if (result[b] == 0) {
			// 없는경우.
			return -1;
		}

		else if (result[b] == k) {
			printf("%d ", b);
			return k;
		}

		else
			i++;
	}
	return -1;

}

