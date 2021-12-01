#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// 인접 행렬 버전
typedef struct vertex {
	char name;
	int inDegree;	// 진입차수
	int isVisited;
}vertex;

typedef struct Graph {
	vertex* vertices;

	// 인접 행렬
	int** ad;
}Graph;

Graph graph;
int n, m; // n : 정점 수, m : 간선 수
int* topOrder;
int num;

int* topologicalSort();
int getVertexIndexByName(char name);
void insertDirectedEdge(char ori, char des);
void insertVertex(char name, int i);
void buildGraph();
void print();

int main(void) {

	buildGraph();
	topologicalSort();
	int q = 0;
	for (int i = 0; i < n; i++) {
		if (topOrder[i] == -1) {
			printf("0");
			q = 1;
			break;
		}
	}
	if(q == 0)
		print();


	return 0;
}

void buildGraph() {

	char tmpVertex, ori, des;

	// 정점
	scanf("%d", &n);
	graph.vertices = (vertex*)malloc(sizeof(vertex) * n);

	// 인접행렬 초기화
	graph.ad = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < n; i++) {
		graph.ad[i] = (int*)malloc(sizeof(int) * n);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			graph.ad[i][j] = -1;
	}

	for (int i = 0; i < n; i++) {
		getchar();
		scanf("%c", &tmpVertex);
		insertVertex(tmpVertex, i);
	}

	// 간선
	scanf("%d", &m);

	for (int i = 0; i < m; i++) {
		getchar();
		scanf("%c %c", &ori, &des);
		insertDirectedEdge(ori, des);
	}

	num = n - 1;
}

void print() {
	for (int i = 0; i < n; i++) {
		printf(" %c", graph.vertices[topOrder[i]].name);
	}
	printf("\n\n");
}

void insertVertex(char name, int i) {

	graph.vertices[i].name = name;
	graph.vertices[i].inDegree = 0;
	graph.vertices[i].isVisited = 0;

}

void insertDirectedEdge(char ori, char des) {
	//방향 간선 삽입
	int oriVertIdx = getVertexIndexByName(ori);
	int desVertIdx = getVertexIndexByName(des);
	graph.ad[oriVertIdx][desVertIdx] = 1;

	// 진입차수 ++
	graph.vertices[desVertIdx].inDegree++;
}

// 이름에 따른 vertext 배열에서 인덱스 반환 = index()
int getVertexIndexByName(char name) {

	for (int i = 0; i < n; i++) {
		if (graph.vertices[i].name == name)
			return i;
	}
}

void rTopologicalSortDfs(int v) {

	graph.vertices[v].isVisited = 1;

	for (int i = 0; i < n; i++) {
	
		if (graph.ad[v][i] != -1 && graph.vertices[i].isVisited == 0) {
			rTopologicalSortDfs(i);
		}
	}
	topOrder[num--] = v;
}

int* topologicalSort() {

	// 각 정점들을 위상 정렬해서 나타내는 topOrder
	// 사이클 존재 유무를 저장하기 위해 0번째 인덱스는 비운다.
	topOrder = (int*)malloc(sizeof(int) * (n));

	// topOrder 초기화
	for (int i = 0; i < n; i++)
		topOrder[i] = -1;

	for (int i = 0; i < n; i++) {

		// 진입 차수 0인 정점만
		if (graph.vertices[i].isVisited == 0 && graph.vertices[i].inDegree == 0) {
			rTopologicalSortDfs(i);
		}
	}

	return topOrder;
}



