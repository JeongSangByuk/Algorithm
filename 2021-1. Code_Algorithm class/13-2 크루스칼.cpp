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
	
	// 모든 간선을 w로 오름차순 정렬
	sort();

	// 모든 간선 검사.
	for (int i = 0; i < m; i++) {

		// 동일한 부모를 가르키지 않는 경우, 즉 사이클 발생 x일때만 선택
		// 동일한 부모를 가르킨다는 것 -> 간선의 두 끝 정점이 같은 그래프 안에 있는 것.
		if (!find(edges[i].in1 - 1, edges[i].in2 - 1)) {
			printf(" %d", edges[i].w);
			sum += edges[i].w;
			unionParent(edges[i].in1 - 1, edges[i].in2 - 1);
		}
	}

	printf("\n%d", sum);


}

// 부모 노드를 병합
void unionParent(int a, int b){
	a = getParent(a);
	b = getParent(b);

	// 더 숫자가 작은 부모로 병합
	if (a < b)
		set[b] = a;
	else
		set[a] = b;
}

// 부모 노드 get
int getParent(int v) {

	if (set[v] == v)
		return v;

	set[v] = getParent(set[v]);
}

// 부모가 같은지 확인
int find(int a, int b) {
	a = getParent(a);
	b = getParent(b);

	if (a == b)
		return 1;
	return 0;
}


void buildGraph() {

	// 정점, 간선, 인접행렬 선언 및 초기화
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
