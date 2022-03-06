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
void detectStronglyConnection(int v);

int main(void) {

	buildGraph();

	// ������ �� ��ο� dfs
	detectStronglyConnection(0);

	int q = 0;

	for (int i = 0; i < n; i++) {

		if (graph.vertices[i].isVisited == 0) {
			printf("not strongly connected\n");
			q = 1;
			break;
		}
	}

	if(q == 0)
		printf("strongly connected\n");

	return 0;
}

// dfs �̿�
void detectStronglyConnection(int v) {

	graph.vertices[v].isVisited = 1;

	for (int i = 0; i < n; i++) {

		if (graph.ad[v][i] != -1 && graph.vertices[i].isVisited == 0) {
			detectStronglyConnection(i);
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
	graph.ad[oriVertIdx][desVertIdx] = 1;
}

// �̸��� ���� vertext �迭���� �ε��� ��ȯ = index()
int getVertexIndexByName(char name) {

	for (int i = 0; i < n; i++) {
		if (graph.vertices[i].name == name)
			return i;
	}
}




