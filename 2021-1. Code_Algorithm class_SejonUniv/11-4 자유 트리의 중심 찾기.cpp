#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct edge {
	int p;
	int q;
	char label;
}edge;

typedef struct vertex {
	int v;
	int isVisited;
}vertex;

vertex* vert;
edge* edges;
int** ad;
int n, m;
void removeLeaves(int v,int p);
void findCenter();

void insertEdge(int a, int b);

int main(void) {

	int a, b;

	int s, v = 0, w = 0;

	scanf("%d %d", &n, &m);

	vert = (vertex*)malloc(n * sizeof(vertex));
	edges = (edge*)malloc(m * sizeof(edge));
	ad = (int**)malloc(n * sizeof(int*));
	for (int i = 0; i < n; i++)
		ad[i] = (int*)malloc(n * sizeof(int));

	//vertex �ʱ�ȭ
	for (int i = 0; i < n; i++) {
		vert[i].v = i + 1;
		vert[i].isVisited = 0;
	}

	//edge �ʱ�ȭ
	for (int i = 0; i < m; i++) {
		edges[i].p = -1;
		edges[i].q = -1;
		edges[i].label = 'f';
	}

	// ���� ��� �ʱ�ȭ
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			ad[i][j] = -1;
		}
	}

	for (int i = 0; i < m; i++) {
		scanf("%d %d", &a, &b);
		insertEdge(a, b);
	}

	findCenter();
	//// ���� indexã��
	//for (int i = 0; i < n; i++) {
	//	if (vert[i].v == s) {
	//		v = i;
	//		break;
	//	}
	//}
}

void Dfs(int v) {

	vert[v].isVisited = 1;
	printf("%d\n", vert[v].v);

	for (int i = 0; i < n; i++) {
		if (ad[v][i] != -1 && vert[i].isVisited == 0)
			Dfs(i);
	}
}

int getVertexCount() {
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (vert[i].v != -1)
			count++;
	}
	return count;
}

int getVertexCount(int v) {
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (ad[v][i] != -1)
			count++;
	}
	return count;
}

int getFirstVertex() {
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (vert[i].v != -1)
			return i;
	}
}

void printVertex() {
	for (int i = 0; i < n; i++) {
		printf(" %d", vert[i].v);
	}
	printf("\n");
}

void findCenter() {
	int p;
	int k = -1;
	while (getVertexCount() > 2) {

		// ������ external ���� ����
		k = getFirstVertex();
		printf("%d\n", k);
		removeLeaves(k, -1);

		// ���� ��尡 external ���� ����
		if (getVertexCount(k) <= 1) {
			vert[k].v = -1;
			vert[k].isVisited = 1;
			// ¥�� �Ѱ� �̝�
			for (int x = 0; x < n; x++) {
				ad[x][k] = -1;
				ad[k][x] = -1;
			}
		}
		printVertex();
	}

	// �� ���������� ��Ƴ��� ��尡 �ᱹ �߽� ���
	for (int i = 0; i < n; i++) {
		if (vert[i].v != -1)
			printf(" %d", vert[i].v);
	}

}

void removeLeaves(int v, int p) {

	int c = 0;

	for (int i = 0; i < n; i++) {

		//  p != i : �θ� ������ ������ x
		if (ad[v][i] != -1 && vert[i].v != -1 && p != i) {

			c++;
			removeLeaves(i, v); 
		}
	}
	
	// �ᱹ ������ �ϳ��� ����� ���� ����.
	if (c == 0 && p != NULL) {
		vert[v].v = -1;
		for (int x = 0; x < n; x++) {
			ad[x][v] = -1;
			ad[v][x] = -1;
		}
	}

}

void insertEdge(int a, int b) {

	int i = 0;
	while (1) {
		if (edges[i].p == -1) {

			edges[i].p = a - 1;
			edges[i].q = b - 1;

			ad[a - 1][b - 1] = i;
			ad[b - 1][a - 1] = i;
			return;
		}
		i++;
	}
}
