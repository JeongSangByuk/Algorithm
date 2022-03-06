#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// ���� ��� ����
typedef struct vertex {
	char name;
	int inDegree;	// ��������
}vertex;

typedef struct Graph {
	vertex* vertices;

	// ���� ���
	int** ad;
}Graph;

Graph graph;
int n, m; // n : ���� ��, m : ���� ��
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

	// ����
	scanf("%d", &n);
	graph.vertices = (vertex*)malloc(sizeof(vertex) * n);

	// ������� �ʱ�ȭ
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

	// ����
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
	//���� ���� ����
	int oriVertIdx = getVertexIndexByName(ori);
	int desVertIdx = getVertexIndexByName(des);
	graph.ad[oriVertIdx][desVertIdx] = 1;

	// �������� ++
	graph.vertices[desVertIdx].inDegree++;
}

// �̸��� ���� vertext �迭���� �ε��� ��ȯ = index()
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

	// �� �������� ���������� ����ϴ� in �迭
	int* in = (int*)malloc(sizeof(int) * n);

	// �� �������� ���� �����ؼ� ��Ÿ���� topOrder
	// ����Ŭ ���� ������ �����ϱ� ���� 0��° �ε����� ����.
	topOrder = (int*)malloc(sizeof(int) * (n + 1));

	// �������� ��⿭ : Q
	Q = (int*)malloc(sizeof(int) * (n + 1));

	int front = 0;
	int rear = 0;

	for (int i = 0; i < n; i++) {

		in[i] = graph.vertices[i].inDegree;

		// �켱 ���������� 0�� vert�� index���� �ִ´�.
		if (in[i] == 0) {
			enqueue(&rear, i);
		}
	}

	// ���� ����
	int t = 1;

	while (!isEmpty(front, rear)) {

		// ť���� �� ���� �־��ֱ� ������, ��ٸ� ������ ���� ��.
		int u = dequeue(&front);
		topOrder[t] = u;
		t++;

		for (int i = 0; i < n; i++) {
			if (graph.ad[u][i] != -1) {

				int des = i;

				// ������ �������� -1
				in[des]--;

				// ���������� 0�̶�� enqueue
				if (in[des] == 0) {
					enqueue(&rear, des);
				}
			}
		}
	}

	// ���� ���� ������ �Ű��������� ������ ����
	// �� DAG�� �ƴ� ���,
	// n���� �湮�ϱ� ���� ť�� ��������.
	// �� ���������� 0�ΰ� ���, ť�� �����Ұ� ���� ����.
	if (t <= n)
		topOrder[0] = 0;
	else
		topOrder[0] = 1;

	return topOrder;
}



