#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

typedef struct vertex {
	int name;
	// d : 거리
	int d;
}vert;

typedef struct edge {
	int w;
	int in1, in2;
}edge;

typedef struct heap {

	// 정점 idx
	int e;

	// 거리
	int key;
}Heap;

vert* vertices;
edge* edges;
Heap* H;	// 최소힙
int** ad;
int n, m;
int heapN;

void downHeap(int i);
void upHeap(int i);
void insertHeap(int index, int e, int key);
void removeMin();
void initHeap();
void replaceKey(int e, int key);
void buildGraph();
int findHeapLocate(int z);
int findWeight(int u, int z);
int findEdge(int u, int z);
void PrimJarnik();
void printHeap();

void main() {

	scanf("%d %d", &n, &m);

	buildGraph();
	PrimJarnik();
}

void PrimJarnik() {

	int sum = 0;

	// 시작 지점을 vert idx 0로
	// 거리가 0이 나오기때문에
	vertices[0].d = 0;

	// 힙 생성
	H = (Heap*)malloc(sizeof(Heap) * (n + 1));
	initHeap();

	while (heapN > 0) {

		int u = H[1].e;
		printf(" %d", vertices[u].name);

		sum += H[1].key;
		//printHeap();
		removeMin();

		for (int i = 0; i < n; i++) {

			// 현재 정점에서 시작하는 간선 다 검사.
			if (ad[u][i] == -1)
				continue;

			// 각 정점들에 대한 거리 값 update
			// 힙에 해당 정점이 있는가? && 가중치가 더 작은가??
			if ((findHeapLocate(i) != -1) && (findWeight(u, i) < vertices[i].d)) {

				// 정점 라벨링, 연결
				vertices[i].d = findWeight(u, i);
				replaceKey(i, vertices[i].d);
			}
		}
	}

	printf("\n%d", sum);

}

void buildGraph() {

	// 정점, 간선, 인접행렬 선언 및 초기화
	vertices = (vert*)malloc(sizeof(vert) * n);
	edges = (edge*)malloc(sizeof(edge) * m);
	ad = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++) {
		ad[i] = (int*)malloc(sizeof(int) * n);
		for (int j = 0; j < n; j++)
			ad[i][j] = -1; // 초기화
	}

	for (int i = 0; i < n; i++) {
		vertices[i].name = i + 1;
		vertices[i].d = 100000;
	}

	for (int i = 0; i < m; i++) {
		int v1, v2, w;

		scanf("%d %d %d", &v1, &v2, &w);

		edges[i].w = w;
		edges[i].in1 = v1;
		edges[i].in2 = v2;

		// 인접 행렬에 가중치를 저장.
		ad[v1 - 1][v2 - 1] = w;
		ad[v2 - 1][v1 - 1] = w;
	}

	// 힙 원소 개수
	heapN = n;
}


void printHeap() {

	for (int i = 1; i <= heapN; i++)
		printf(" %d", H[i].key);
	printf("\n");
}

int findWeight(int a, int b) {

	// 인접 행렬 값에 w 저장했기 때문에
	return ad[a][b];
}

// 해당 정점이 힙에 있는 위치 반환
int findHeapLocate(int a) {
	for (int i = 1; i <= heapN; i++) {
		if (H[i].e == a)
			return i;
	}
	return -1;
}

int findEdge(int a, int b) {
	for (int i = 0; i < m; i++) {
		if ((edges[i].in1 == a + 1 && edges[i].in2 == b + 1) ||
			(edges[i].in1 == b + 1 && edges[i].in2 == a + 1)) {
			return i;
		}
	}
	return -1;
}

void replaceKey(int e, int key) {

	// 원소 e의 키를 k로 변경하고 힙 내의 e의 위치를 갱신
	int in = findHeapLocate(e);
	H[in].key = key;
	upHeap(in);
}

void initHeap() {

	int e, key;

	for (int i = 0; i < n; i++) {
		e = i;	// 정점 index
		key = vertices[i].d;
		insertHeap(i + 1, e, key);
	}
}

void insertHeap(int index, int e, int key) {

	H[index].e = e;
	H[index].key = key;
	upHeap(index);

}

void upHeap(int i) {

	Heap tmp;

	if (i == 1)
		return;

	if (H[i].key >= H[i / 2].key)
		return;

	tmp = H[i];
	H[i] = H[i / 2];
	H[i / 2] = tmp;

	upHeap(i / 2);
}

void downHeap(int i) {

	int smaller = 0;
	Heap tmp;

	if (heapN < 2 * i)
		return;

	// smaller 찾기
	smaller = 2 * i;
	if (2 * i + 1 <= heapN) {
		if (H[2 * i + 1].key < H[smaller].key)
			smaller = 2 * i + 1;
	}

	if (H[i].key <= H[smaller].key)
		return;

	tmp = H[i];
	H[i] = H[smaller];
	H[smaller] = tmp;
	downHeap(smaller);

}

void removeMin() {

	H[1] = H[heapN--];
	downHeap(1);
}
