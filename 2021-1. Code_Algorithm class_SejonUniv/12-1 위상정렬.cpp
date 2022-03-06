#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct edge {
	// ������ ����� vert�� index
	int oriVertIdx;
	int desVertIdx;
}edge;

typedef struct incidence {
	int edge;
	struct incidence* next;
}inc;

typedef struct vertex {
	char name;
	int inDegree;	// ��������
	inc* outEdges;
	inc* inEdges;
}vertex;

typedef struct Graph {
	vertex* vertices;
	edge* edges;
}Graph;

Graph graph;
int n, m; // n : ���� ��, m : ���� ��
int* topOrder;
int* Q;

int* topologicalSort();
int dequeue(int* front);
void enqueue(int* rear, int v);
int isEmpty(int front, int rear);
void addFirst(inc* H, int i);
int getVertexIndexByName(char name);
void insertDirectedEdge(char ori, char des, int i);
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

	for (int i = 0; i < n; i++) {
		getchar();
		scanf("%c", &tmpVertex);
		insertVertex(tmpVertex, i);
	}

	// ����
	scanf("%d", &m);
	graph.edges = (edge*)malloc(sizeof(edge) * m);

	for (int i = 0; i < m; i++) {
		getchar();
		scanf("%c %c", &ori, &des);
		insertDirectedEdge(ori, des, i);
	}
}

void insertVertex(char name, int i) {

	graph.vertices[i].name = name;
	graph.vertices[i].outEdges = (inc*)malloc(sizeof(inc));
	graph.vertices[i].inEdges = (inc*)malloc(sizeof(inc));

	// in�ϴ� vert�� out�ϴ� vert�� ���� �߰�.
	graph.vertices[i].outEdges->next = NULL;
	graph.vertices[i].inEdges->next = NULL;
	graph.vertices[i].inDegree = 0;
}

// i = edges���� �ش� ������ index
void insertDirectedEdge(char ori, char des, int i) {
	//���� ���� ����
	int oriVertIdx = getVertexIndexByName(ori);
	int desVertIdx = getVertexIndexByName(des);
	graph.edges[i].oriVertIdx = oriVertIdx;
	graph.edges[i].desVertIdx = desVertIdx;
	addFirst(graph.vertices[oriVertIdx].outEdges, i);
	addFirst(graph.vertices[desVertIdx].inEdges, i);

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

void addFirst(inc* H, int i) {

	// ù��� ��ġ�� ��� ����.
	inc* node = (inc*)malloc(sizeof(inc));
	node->edge = i;
	node->next = H->next;
	H->next = node;
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

		inc* p = graph.vertices[u].outEdges;

		while (p->next != NULL) {
			p = p->next;

			int des = graph.edges[p->edge].desVertIdx;

			// ������ �������� -1
			in[des]--;

			// ���������� 0�̶�� enqueue
			if (in[des] == 0) {
				enqueue(&rear, des);
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



