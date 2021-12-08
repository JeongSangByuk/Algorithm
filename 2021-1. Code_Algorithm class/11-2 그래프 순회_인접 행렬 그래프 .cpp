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

int queue[1000];

void insertEdge(int a, int b);
void Bfs(int v);
void Bfs2(int v);

int main(void) {

	int a, b;

	int s, v = 0;

	scanf("%d %d %d", &n, &m, &s);

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

	// ���� indexã��
	for (int i = 0; i < n; i++) {
		if (vert[i].v == s) {
			v = i;
			break;
		}
	}

	//Dfs(v);
	Bfs2(v);

}

void Dfs(int v) {

	vert[v].isVisited = 1;
	printf("%d\n", vert[v].v);

	for (int i = 0; i < n; i++) {
		if (ad[v][i] != -1 && vert[i].isVisited == 0)
			Dfs(i);
	}
}

void Bfs2(int v) {

	int front = 0, rear = 0;
	int pop;

	printf("%d\n", v + 1);
	queue[0] = v;
	rear++;
	vert[v].isVisited = 1;

	while (front < rear) {
		pop = queue[front];
		front++;

		for (int i = 0; i < n; i++) {
			if (ad[pop][i] != -1 && vert[i].isVisited == 0) {
				printf("%d\n", i + 1);
				queue[rear] = i;
				rear++;
				vert[i].isVisited = 1;
			}
		}

	}
}


void Bfs(int v) {

	int stack[100] = { 0, };
	int tmp[100] = { 0, };
	int i = 1, v2, tmpIdx;

	vert[v].isVisited = 1;
	stack[0] = v;

	while (i != 0) {

		for (int j = 0; j < i; j++) {
			printf("%d\n", vert[stack[j]].v);
			tmp[j] = stack[j];
		}

		// �ݺ��� �����϶� i ���� 0���� �ʱ�ȭ�Ѵ�.
		int len = i;
		i = 0;

		// stack�� �ִ� ������ tmp�� �����ϰ� tmp�� ����
		// �� ���� ������ ������ stack ����.
		for (int l = 0; l < len; l++) {

			v = tmp[l];

			for (int j = 0; j < n; j++) {

				if (ad[v][j] != -1) {

					// edge idx
					tmpIdx = ad[v][j];

					if (edges[tmpIdx].label == 'f') {

						// ������ �ݴ��� vertex, v�� �ƴ� vertex
						v2 = j;

						if (vert[v2].isVisited == 0) {
							edges[tmpIdx].label = 't';
							vert[v2].isVisited = 1;
							stack[i] = v2;
							i++;
						}
						else {
							// ��������
							edges[tmpIdx].label = 'c';
						}

					}

				}

			}


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