#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

typedef struct vertex {
	int name;
}vert;

typedef struct edge {
	int w;
	int in1, in2;
}edge;

vert* vertices;
edge* edges;
edge* parents;
int* set;
int n, m;

void unionParent(int a, int b);
int getParent(int v);
int find(int a, int b);
void buildGraph();
void sort();
void Kruskal();

void main() {

	scanf("%d %d", &n, &m);

	buildGraph();
	Kruskal();
}

void Kruskal() {

	set = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		set[i] = i;

	int sum = 0;
	
	// ��� ������ w�� �������� ����
	sort();

	// ��� ���� �˻�.
	for (int i = 0; i < m; i++) {

		// ������ �θ� ����Ű�� �ʴ� ���, �� ����Ŭ �߻� x�϶��� ����
		// ������ �θ� ����Ų�ٴ� �� -> ������ �� �� ������ ���� �׷��� �ȿ� �ִ� ��.
		if (!find(edges[i].in1 - 1, edges[i].in2 - 1)) {
			printf(" %d", edges[i].w);
			sum += edges[i].w;
			unionParent(edges[i].in1 - 1, edges[i].in2 - 1);
		}
	}

	printf("\n%d", sum);


}

// �θ� ��带 ����
void unionParent(int a, int b){
	a = getParent(a);
	b = getParent(b);

	// �� ���ڰ� ���� �θ�� ����
	if (a < b)
		set[b] = a;
	else
		set[a] = b;
}

// �θ� ��� get
int getParent(int v) {

	if (set[v] == v)
		return v;

	set[v] = getParent(set[v]);
}

// �θ� ������ Ȯ��
int find(int a, int b) {
	a = getParent(a);
	b = getParent(b);

	if (a == b)
		return 1;
	return 0;
}


void buildGraph() {

	// ����, ����, ������� ���� �� �ʱ�ȭ
	vertices = (vert*)malloc(sizeof(vert) * n);
	edges = (edge*)malloc(sizeof(edge) * m);

	for (int i = 0; i < n; i++) {
		vertices[i].name = i + 1;
	}

	for (int i = 0; i < m; i++) {
		int v1, v2, w;

		scanf("%d %d %d", &v1, &v2, &w);

		edges[i].w = w;
		edges[i].in1 = v1;
		edges[i].in2 = v2;
	}
}

void sort() {

	int tmp;
	// sorting
	for (int i = m - 1; i > 0; i--) {

		tmp = i;

		for (int j = i - 1; j >= 0; j--) {
			if (edges[tmp].w < edges[j].w) {
				tmp = j;
			}
		}

		edge temp = edges[i];
		edges[i] = edges[tmp];
		edges[tmp] = temp;
	}

}
