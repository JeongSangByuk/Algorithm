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

int start, end;
int stack[1000] = { 0, };
int stackEnd = 0;

int parent[1000] = { 0, };

int queue[1000];

void insertEdge(int a, int b);
void Bfs(int v);
void Bfs2(int start, int end);
void Dfs(int start, int end);

int main(void) {

	int a, b;

	int s, v = 0, w = 0;

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

	//// ���� indexã��
	//for (int i = 0; i < n; i++) {
	//	if (vert[i].v == s) {
	//		v = i;
	//		break;
	//	}
	//}

	printf("start : ");
	scanf("%d", &start);

	printf("end : ");
	scanf("%d", &end);


	// ���� indexã��
	for (int i = 0; i < n; i++) {
		if (vert[i].v == start) {
			v = i;
			break;
		}
	}

	// �� indexã��
	for (int j = 0; j < n; j++) {
		if (vert[j].v == end) {
			w = j;
			break;
		}
	}

	//Dfs(v,w);
	//for (int i = 0; i < stackEnd; i++)
	//	printf(" %d", stack[i]);

	Bfs2(v,w);

}

int q = 0;

// dfs ���ã��
void Dfs(int start, int end) {

	int tmp;
	vert[start].isVisited = 1;

	stack[stackEnd++] = vert[start].v;

	for (int i = 0; i < stackEnd; i++)
		printf(" %d", stack[i]);
	printf("\n");

	if (start == end) {
		q = 1;
		return;
	}

	for (int i = 0; i < n; i++) {
		if (ad[start][i] != -1 && vert[i].isVisited == 0 && q == 0) {
			Dfs(i,end);
		}
	}

	// �ǳ����� �ôµ� ���� ��ã�� ����̴�. stack--
	if (q == 0)
		stackEnd--;
}

// BFS�� ���� �ִ� ���
void Bfs2(int start, int end) {

	int front = 0, rear = 0;
	int pop,tmp;

	stack[stackEnd++] = vert[start].v;

	queue[0] = start;
	rear++;
	vert[start].isVisited = 1;

	tmp = 0;

	while (front < rear) {
		pop = queue[front++];

		for (int i = 0; i < n; i++) {
			if (ad[pop][i] != -1 && vert[i].isVisited == 0) {

				queue[rear] = i;
				rear++;
				vert[i].isVisited = 1;

				// �θ� �迭�� �θ� index ����
				parent[++tmp] = front - 1;

				//break�ϱ�����
				if (end == i) {
					rear = -1;
					break;
				}

			}
		}
	}

	int result = tmp,k=0;
	int arr[100] = { 0, };

	while (result!=start) {
		arr[k++] = vert[result].v;
		result = parent[result];
	}

	printf(" %d", vert[start].v);

	for (int t = k - 1; t >= 0; t--)
		printf(" %d", arr[t]);
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