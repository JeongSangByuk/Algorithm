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
	// 비재귀적
	//buildHeap();

	// 재귀적
	rBuildHeap(1);

	printHeap();

	return 0;
}

// 비재귀적 상향식 힙 생성
void buildHeap() {

	// 각각의 루트노드를 다돈다.
	for (int i = n / 2; i > 0; i--) {

		// 각각의 루트에서 다운힙.
		downHeap(i);
	}
	return;
}

// 재귀적 상향식 힙 생성
void rBuildHeap(int i) {

	if (i > n)
		return;

	rBuildHeap(2 * i);
	rBuildHeap(2 * i + 1);

	// 결국 재귀적이든 비재귀적이든 downHeap 시키는게 포인트.
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
