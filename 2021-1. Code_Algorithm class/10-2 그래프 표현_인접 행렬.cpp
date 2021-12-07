#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct edge {
	int p;
	int q;
	int weight;
}edge;

typedef struct vertex {
	int v;
}vertex;

vertex vert[6];
edge edges[21];
int ad[6][6];

void insertEdge(int a, int b, int w);
void printNodes(int n);

int main(void) {

	char c;
	int n;
	int a, b, w;

	//vertex 초기화
	for (int i = 0; i < 6; i++) {
		vert[i].v = i + 1;
	}

	//edge 초기화
	for (int i = 0; i < 21; i++) {
		edges[i].p = -1;
		edges[i].q = -1;
		edges[i].weight = 0;
	}

	// 인접 행렬 초기화
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			ad[i][j] = -1;
		}
	}

	insertEdge(1, 2, 1);
	insertEdge(1, 3, 1);
	insertEdge(1, 4, 1);
	insertEdge(1, 6, 2);
	insertEdge(2, 3, 1);
	insertEdge(3, 5, 4);
	insertEdge(5, 5, 4);
	insertEdge(5, 6, 3);

	while (1) {
		scanf("%c", &c);

		if (c == 'a') {
			scanf("%d", &n);
			printNodes(n);
			printf("\n");
		}

		else if (c == 'm') {
			scanf("%d %d %d", &a, &b, &w);
			insertEdge(a, b, w);
		}

		else if (c == 'q')
			break;

		getchar();
	}

	return 0;
}

void insertEdge(int a, int b, int w) {

	int i = 0;
	while (1) {
		if (a < 1 || b < 1 || a > 6 || b > 6) {
			printf("-1\n");
			return;
		}

		// 새 간선 추가.
		if (edges[i].weight == 0) {

			if (w == 0)
				return;

			edges[i].p = a - 1;
			edges[i].q = b - 1;
			edges[i].weight = w;
			ad[a - 1][b - 1] = i;
			ad[b - 1][a - 1] = i;
			return;
		}

		// 새 간선 추가가 아닌 경우
		else {
			int idx1 = edges[i].p;
			int idx2 = edges[i].q;

			// a와 b를 각각 끝점으로 갖는 edge존재.
			if ((vert[idx1].v == a && vert[idx2].v == b)
				|| (vert[idx2].v == a && vert[idx1].v == b)) {

				if (w != 0)
					edges[i].weight = w;

				// 가중치가 0이면 edge 삭제
				else {
					for (int y = 0; y < 6; y++) {
						for (int x = 0; x < 6; x++) {
							if (ad[x][y] == i)
								ad[x][y] = -1;
							if (ad[x][y] > i)
								ad[x][y]--;
						}
					}

					// edge 정보 초기화
					for (int j = i; j < 20; j++) {
						if (edges[j].weight == 0) {
							edges[j].p = -1;
							edges[j].q = -1;
							edges[j].weight = 0;
							break;
						}
						edges[j] = edges[j + 1];
					}
				}
				return;
			}
		}
		i++;
	}
}


void printNodes(int n) {

	if (n < 1 || n > 6) {
		printf("-1");
		return;
	}

	for (int i = 0; i < 6; i++) {
		int num = 0;
		num = ad[n - 1][i];
		if (num != -1) {
			printf(" %d %d", i + 1, edges[num].weight);
		}
	}

}

int deg(int v) {

	int cnt = 0;

	for (int i = 0; i < 6; i++) {

		if (ad[v - 1][i] != -1)
			cnt++;

	}
	return cnt;

}

void opposite(vertex v, edge e) {

	int u = e.p;
	int w = e.q;

	// vert 찾기.
	int i = 0;
	for (i = 0; i < 6; i++)
		if (vert[i].v == u)
			break;

	int j = 0;
	for (j = 0; j < 6; j++)
		if (vert[j].v == w)
			break;

	if (i == v.v)
		printf("%d\n", vert[j].v);
	else
		printf("%d\n", vert[i].v);

}