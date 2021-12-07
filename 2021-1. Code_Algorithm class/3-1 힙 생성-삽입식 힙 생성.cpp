#pragma warning(disable:4996)
#include<stdio.h>

int removeMax();
int removeMax();
void insertItem(int key);
void upHeap(int idx);
void downHeap(int idx);
void printHeap();

int n=0;
int H[100];

// 최대 힙
int main() {

	int isQ = 0;
	char m;
	int key;

	while (isQ != 1) {
		scanf("%c", &m);
		getchar();

		switch (m)
		{
		case 'i':
			scanf(" %d", &key);
			insertItem(key);
			getchar();
			break;

		case 'd':
			printf("%d\n", removeMax()); ;
			break;

		case 'p':
			printHeap();
			break;

		case 'q':
			isQ = 1;
			break;

		default:
			break;
		}
	}

	return 0;
}

void printHeap() {
	for (int i = 1; i < n + 1; i++)
		printf(" %d", H[i]);
	printf("\n");
}

int removeMax() {

	int rootKey = H[1];
	H[1] = H[n];
	n--;
	downHeap(1);
	return rootKey;
}

void insertItem(int key) {
	n++;
	H[n] = key;
	upHeap(n);
	printf("0\n");
}

void upHeap(int idx) {

	if (idx == 1)
		return;

	if (H[idx / 2] >= H[idx])
		return;

	int tmp = H[idx];
	H[idx] = H[idx / 2];
	H[idx / 2] = tmp;

	upHeap(idx / 2);
}

void downHeap(int idx) {

	int left = 2 * idx;
	int right = 2 * idx + 1;

	//external node -> 마지막 노드일경우 downheap끝.
	if (left > n && right > n)
		return;

	// left child
	int biggerIdx = left;

	// right child가 있을경우, right child도 검사.
	if (right <= n) {
		//left,right 뭐가 더 큰지
		if (H[right] > H[biggerIdx])
			biggerIdx = right;
	}

	if (H[idx] >= H[biggerIdx])
		return;

	int temp = H[biggerIdx];
	H[biggerIdx] = H[idx];
	H[idx] = temp;

	downHeap(biggerIdx);
}
