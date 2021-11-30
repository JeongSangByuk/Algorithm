#pragma warning(disable:4996)
#include<stdio.h>

void downHeap(int idx);
void printHeap();
void buildHeap();
void rBuildHeap(int i);

int n;
int H[100];

int main() {

	char m;
	int key;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%d", &H[i]);
	}
	// �������
	//buildHeap();

	// �����
	rBuildHeap(1);

	printHeap();

	return 0;
}

// ������� ����� �� ����
void buildHeap() {

	// ������ ��Ʈ��带 �ٵ���.
	for (int i = n / 2; i > 0; i--) {

		// ������ ��Ʈ���� �ٿ���.
		downHeap(i);
	}
	return;
}

// ����� ����� �� ����
void rBuildHeap(int i) {

	if (i > n)
		return;

	rBuildHeap(2 * i);
	rBuildHeap(2 * i + 1);

	// �ᱹ ������̵� ��������̵� downHeap ��Ű�°� ����Ʈ.
	downHeap(i);
	return;
}

void printHeap() {
	for (int i = 1; i < n + 1; i++)
		printf(" %d", H[i]);
	printf("\n");
}

void downHeap(int idx) {

	int left = 2 * idx;
	int right = 2 * idx + 1;

	//external node -> ������ ����ϰ�� downheap��.
	if (left > n && right > n)
		return;

	// left child
	int biggerIdx = left;

	// right child�� �������, right child�� �˻�.
	if (right <= n) {
		//left,right ���� �� ū��
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
