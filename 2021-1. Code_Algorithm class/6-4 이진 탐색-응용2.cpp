#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include <time.h>


/// 단일 모드 배열의 최대 원소 구하기

int n;
int H[100];

int findElement();

int main() {

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", &H[i]);

	printf(" %d", findElement());
}

int findElement() {

	int mid;

	int a = 0;
	int b = n - 1;

	while (a < b) {

		mid = (a + b) / 2;

		if (H[mid] < H[mid + 1])
			a = mid + 1;
		else if (H[mid] > H[mid + 1])
			b = mid;

	}

	return H[a];

}
