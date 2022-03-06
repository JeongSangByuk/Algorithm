#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

//#include <iostream>
//using namespace std;
int findElement(int k);
void initBucketArray();
int getNextBucet(int v, int vv, int i);
int insertItem(int k);
int h2(int x);
int h(int x);

int n, m, q, * arr;

int main() {

	char c = '0';
	int k;
	scanf("%d %d %d", &m, &n, &q);
	getchar();
	arr = (int*)malloc(sizeof(int) * m);
	initBucketArray();

	while (c != 'e') {

		scanf("%c", &c);
		getchar();

		switch (c) {

		case 'i':
			scanf("%d", &k);
			printf("%d\n", insertItem(k));
			getchar();
			break;

		case 's':
			scanf("%d", &k);
			printf("%d\n", findElement(k));
			getchar();
			break;

		case 'p':
		case 'e':
			for (int i = 0; i < m; i++) {
				printf(" %d", arr[i]);
			}
			printf("\n");
			break;

		default:
			break;
		}


	}

}

int h(int x) {
	return x % m;
}

int h2(int x) {
	return q - (x % q);
}

int insertItem(int k) {
	int v = h(k);
	int i = 0;

	int vv = h2(k);


	while (i < m) {
		int b = getNextBucet(v, vv, i);

		if (arr[b] == 0) {
			arr[b] = k;
			return b;
		}
		else
			i++;
		printf("C");
	}
}

int getNextBucet(int v, int vv, int i) {
	return ((v + (i * vv)) % m);
}

void initBucketArray() {
	for (int i = 0; i < m; i++) {
		arr[i] = 0;
	}
}

int findElement(int k) {
	int v = h(k);
	int i = 0;
	int vv = h2(k);

	while (i < m) {
		int b = getNextBucet(v, vv, i);

		if (arr[b] == 0) {
			// 없는경우.
			return -1;
		}

		else if (arr[b] == k) {
			printf("%d ", b);
			return k;
		}

		else
			i++;
	}
	return -1;

}

