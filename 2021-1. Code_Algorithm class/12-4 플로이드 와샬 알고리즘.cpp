#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// ���� ��� ����
typedef struct vertex {
	char name;
	int isVisited;
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

	// �÷��̵� �ͼ� �˰����� �ٽ��� ���İ��� ��带 ��������!

	// k = ���İ��� ���
	for (int k = 0; k < n; k++) {

		// i = ��� ���
		for (int i = 0; i < n; i++) {

			if (i == k)
				continue;

			// j = ���� ���
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
	graph.vertices[i].isVisited = 0;
}

void insertDirectedEdge(char ori, char des) {
	//���� ���� ����
	int oriVertIdx = getVertexIndexByName(ori);
	int desVertIdx = getVertexIndexByName(des);
	graph.ad[oriVertIdx][desVertIdx] = 0;
}

void insertDirectedEdgeWithIdx(char ori, char des) {
	//���� ���� ����
	graph.ad[ori][des] = 0;
}


// �̸��� ���� vertext �迭���� �ε��� ��ȯ = index()
int getVertexIndexByName(char name) {

	for (int i = 0; i < n; i++) {
		if (graph.vertices[i].name == name)
			return i;
	}
}




