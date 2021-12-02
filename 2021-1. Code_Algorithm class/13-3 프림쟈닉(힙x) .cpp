#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

typedef struct vertex {
	int name;
	// d : �Ÿ�
	int d;
}vert;

typedef struct edge {
	int w;
	int in1, in2;
}edge;

typedef struct heap {

	// ���� idx
	int e;

	// �Ÿ�
	int key;
}Heap;

vert* vertices;
edge* edges;
Heap* H;	// �ּ���
int** ad;
int n, m;
int heapN;

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

void sort() {

	int tmp;
	// sorting
	for (int i = heapN - 1; i > 0; i--) {

		tmp = i;

		for (int j = i - 1; j >= 0; j--) {
			if (H[tmp].key < H[j].key) {
				tmp = j;
			}
		}

		Heap temp = H[i];
		H[i] = H[tmp];
		H[tmp] = temp;
	}

}

void PrimJarnik() {

	int sum = 0;

	// ���� ������ vert idx 0��
	// �Ÿ��� 0�� �����⶧����
	vertices[0].d = 0;

	// �� ����
	H = (Heap*)malloc(sizeof(Heap) * (n));

	for (int i = 0; i < n; i++) {
		H[i].key = vertices[i].d;
		H[i].e = vertices[i].name - 1;
	}

	while (heapN > 0) {


		sort();

		int u = H[0].e;
		printf(" %d", vertices[u].name);

		sum += H[0].key;

		//removeMin
		for (int i = 0; i < heapN - 1; i++) {
			H[i] = H[i + 1];
		}
		heapN--;

		for (int i = 0; i < n; i++) {

			// ���� �������� �����ϴ� ���� �� �˻�.
			if (ad[u][i] == -1)
				continue;

			// �� �����鿡 ���� �Ÿ� �� update
			// ���� �ش� ������ �ִ°�? && ����ġ�� �� ������??
			if ((findHeapLocate(i) != -1) && (findWeight(u, i) < vertices[i].d)) {

				// ���� �󺧸�, ����
				vertices[i].d = findWeight(u, i);
				replaceKey(i, vertices[i].d);

			}
		}
	}

	printf("\n%d", sum);

}

void buildGraph() {

	// ����, ����, ������� ���� �� �ʱ�ȭ
	vertices = (vert*)malloc(sizeof(vert) * n);
	edges = (edge*)malloc(sizeof(edge) * m);
	ad = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++) {
		ad[i] = (int*)malloc(sizeof(int) * n);
		for (int j = 0; j < n; j++)
			ad[i][j] = -1; // �ʱ�ȭ
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

		// ���� ��Ŀ� ����ġ�� ����.
		ad[v1 - 1][v2 - 1] = w;
		ad[v2 - 1][v1 - 1] = w;
	}

	// �� ���� ����
	heapN = n;
}


void printHeap() {

	for (int i = 1; i <= heapN; i++)
		printf(" %d", H[i].key);
	printf("\n");
}

int findWeight(int a, int b) {

	// ���� ��� ���� w �����߱� ������
	return ad[a][b];
}

// �ش� ������ ���� �ִ� ��ġ ��ȯ
int findHeapLocate(int a) {
	for (int i = 0; i < heapN; i++) {
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

	// ���� e�� Ű�� k�� �����ϰ� �� ���� e�� ��ġ�� ����
	int in = findHeapLocate(e);
	H[in].key = key;
}

