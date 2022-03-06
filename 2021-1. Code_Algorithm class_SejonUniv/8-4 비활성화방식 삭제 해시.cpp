#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

//#include <iostream>
//using namespace std;
int findElement(int k);
void initBucketArray();
int getNextBucet(int v, int i);
int insertItem(int k);
int removeElement(int k);

typedef struct Node {
	int key;
	char isActive;
}Node;

int n, m;
Node* arr;

int main() {

	char c = '0';
	int k;
	scanf("%d %d", &m, &n);
	getchar();
	arr = (Node*)malloc(sizeof(Node) * m);
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

		case 'd':
			scanf("%d", &k);
			printf("%d\n", removeElement(k));
			getchar();
			break;

		case 's':
			scanf("%d", &k);
			printf("%d\n", findElement(k));
			getchar();
			break;

		case 'p':
			for (int i = 0; i < m; i++) {
				if(arr[i].isActive == 1)
					printf(" %d", arr[i].key);
			}
			printf("\n");

		default:
			break;
		}


	}

}

int h(int x) {
	return x % m;
}

int insertItem(int k) {
	int v = h(k);
	int i = 0;

	while (i < m) {
		int b = getNextBucet(v, i);
		
		// inActive 상태일때만, 삽입 후 active 상태로
		if (arr[b].key == 0 || arr[b].isActive == 0) {
			arr[b].key = k;
			arr[b].isActive = 1;
			return b;
		}
		else
			i++;
		printf("C");
	}
}

int removeElement(int k) {

	int v = h(k);
	int i = 0;

	while (i < m) {
		int b = getNextBucet(v, i);

		// isEmpty
		if (arr[b].key == 0) {
			// 없는경우.
			return -1;
		}

		// acitve 상태일때만, 삭제 = inActive 상태로
		else if (arr[b].key == k && arr[b].isActive == 1) {
			arr[b].isActive = 0;
			return k;
		}

		else
			i++;
	}
	return -1;

}

int getNextBucet(int v, int i) {
	return ((v + i) % m);
}

void initBucketArray() {
	for (int i = 0; i < m; i++) {
		arr[i].key = 0;
		arr[i].isActive = 0;
	}
}

int findElement(int k) {
	int v = h(k);
	int i = 0;

	while (i < m) {
		int b = getNextBucet(v, i);

		// isEmpty
		if (arr[b].key == 0) {
			// 없는경우.
			return -1;
		}

		else if ( arr[b].key == k && arr[b].isActive == 1) {
			printf("%d ", b);
			return k;
		}

		else
			i++;
	}
	return -1;

}

