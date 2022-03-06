#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// 인접 행렬 버전
typedef struct vertex {
	char name;
	int inDegree;	// 진입차수
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

int* topologicalSort();
int dequeue(int* front);
void enqueue(int* rear, int v);
int isEmpty(int front, int rear);
int getVertexIndexByName(char name);
void insertDirectedEdge(char ori, char des);
void insertVertex(char name, int i);
void buildGraph();

int main(void) {

	buildGraph();
	topOrder = topologicalSort();

	if (topOrder[0] == 0)
		printf("0");

	else {
		for (int i = 1; i < n + 1; i++) {
			printf(" %c", graph.vertices[topOrder[i]].name);
		}
	}

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
}

void insertVertex(char name, int i) {

	graph.vertices[i].name = name;
	graph.vertices[i].inDegree = 0;
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

int isEmpty(int front, int rear) {
	if (front == rear)
		return 1;
	else
		return 0;
}

void enqueue(int* rear, int v) {
	Q[(*rear)++] = v;
}

int dequeue(int* front) {
	return Q[(*front)++];
}

int* topologicalSort() {

	// 각 정점들의 진입차수를 기록하는 in 배열
	int* in = (int*)malloc(sizeof(int) * n);

	// 각 정점들을 위상 정렬해서 나타내는 topOrder
	// 사이클 존재 유무를 저장하기 위해 0번째 인덱스는 비운다.
	topOrder = (int*)malloc(sizeof(int) * (n + 1));

	// 정점들의 대기열 : Q
	Q = (int*)malloc(sizeof(int) * (n + 1));

	int front = 0;
	int rear = 0;

	for (int i = 0; i < n; i++) {

		in[i] = graph.vertices[i].inDegree;

		// 우선 진입차수가 0인 vert의 index부터 넣는다.
		if (in[i] == 0) {
			enqueue(&rear, i);
		}
	}

	// 위상 순위
	int t = 1;

	while (!isEmpty(front, rear)) {

		// 큐에서 뺀 다음 넣어주기 때문에, 빈다면 넣을게 없는 것.
		int u = dequeue(&front);
		topOrder[t] = u;
		t++;

		for (int i = 0; i < n; i++) {
			if (graph.ad[u][i] != -1) {

				int des = i;

				// 정점의 진입차수 -1
				in[des]--;

				// 진입차수가 0이라면 enqueue
				if (in[des] == 0) {
					enqueue(&rear, des);
				}
			}
		}
	}

	// 아직 위상 순위가 매겨지지않은 정점이 존재
	// 즉 DAG가 아닌 경우,
	// n개를 방문하기 전에 큐가 비어버린것.
	// 즉 진입차수가 0인게 없어서, 큐에 삽입할게 없는 상태.
	if (t <= n)
		topOrder[0] = 0;
	else
		topOrder[0] = 1;

	return topOrder;
}



