#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// 인접 행렬 버전
typedef struct vertex {
	char name;
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
int* Q;

int getVertexIndexByName(char name);
void insertDirectedEdge(char ori, char des);
void insertVertex(char name, int i);
void buildGraph();
void FloydWarshall();
void insertDirectedEdgeWithIdx(char ori, char des);

int main(void) {

	buildGraph();

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf(" %d", graph.ad[i][j]);
		}
		printf("\n");
	}

	FloydWarshall();

	printf("\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf(" %d", graph.ad[i][j]);
		}
		printf("\n");
	}

	return 0;
}

void FloydWarshall() {

	// 플로이드 와샬 알고리즘의 핵심은 거쳐가는 노드를 기준으로!

	// k = 거쳐가는 노드
	for (int k = 0; k < n; k++) {

		// i = 출발 노드
		for (int i = 0; i < n; i++) {

			if (i == k)
				continue;

			// j = 도착 노드
			for (int j = 0; j < n; j++) {

				if (j == i || j == k)
					continue;

				if (graph.ad[i][k] != -1 && graph.ad[k][j] != -1 && graph.ad[i][j] == -1) {
					insertDirectedEdgeWithIdx(i, j);
				}
			}
		}
	}
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
}

void insertVertex(char name, int i) {

	graph.vertices[i].name = name;
	graph.vertices[i].isVisited = 0;
}

void insertDirectedEdge(char ori, char des) {
	//방향 간선 삽입
	int oriVertIdx = getVertexIndexByName(ori);
	int desVertIdx = getVertexIndexByName(des);
	graph.ad[oriVertIdx][desVertIdx] = 0;
}

void insertDirectedEdgeWithIdx(char ori, char des) {
	//방향 간선 삽입
	graph.ad[ori][des] = 0;
}


// 이름에 따른 vertext 배열에서 인덱스 반환 = index()
int getVertexIndexByName(char name) {

	for (int i = 0; i < n; i++) {
		if (graph.vertices[i].name == name)
			return i;
	}
}




