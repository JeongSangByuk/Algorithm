#pragma warning(disable:4996)
#include<stdio.h>

void printHeap();
void buildHeap();
void downHeap(int idx, int last);
void inPlaceHeapSort();

int n;
int H[100];

int main() {

	char m;
	int key;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%d", &H[i]);
	}
	inPlaceHeapSort();
	printHeap();

	return 0;
}


void printHeap() {
	for (int i = 1; i < n + 1; i++)
		printf(" %d", H[i]);
	printf("\n");
}

void inPlaceHeapSort() {

	buildHeap();

	for (int i = n; i > 1; i--) {
		int tmp = H[1];
		H[1] = H[i];
		H[i] = tmp;
		downHeap(1, i - 1);
	}

}

void downHeap(int idx, int last) {

	int left = 2 * idx;
	int right = 2 * idx + 1;

	if (left > last)
		return;

	// left child
	int biggerIdx = left;

	// right child�� �������, right child�� �˻�.
	if (right <= last) {
		//left,right ���� �� ū��
		if (H[right] > H[biggerIdx])
			biggerIdx = right;
	}

	if (H[idx] >= H[biggerIdx])
		return;

	int temp = H[biggerIdx];
	H[biggerIdx] = H[idx];
	H[idx] = temp;

	downHeap(biggerIdx, last);
}

// ������� ����� �� ����
void buildHeap() {

	// ������ ��Ʈ��带 �� ���ٰ� �����ϸ�ȴ�.
	for (int i = n / 2; i > 0; i--) {
		// ������ ��Ʈ���� �ٿ����Ѵٰ� ����.
		downHeap(i, n);
	}
	return;
}
