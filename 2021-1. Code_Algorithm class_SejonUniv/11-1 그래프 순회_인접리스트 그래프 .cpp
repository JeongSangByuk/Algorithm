#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct edge {
	int p;
	int q;
	// f : fresh 간선, t : 트리 간선, b : 후향 간선
	char label;
}edge;

typedef struct incidence {
	// 몇번째 간선인지 저장
	int edge;
	struct incidence* next;
}inc;

typedef struct vertex {
	inc* inc;
	int v;
	int isVisited;
}vertex;

vertex* vert;
edge* edges;
int n, m;
int queue[1000];

void insertEdge(int a, int b);
void buildIncList(int a, int b, int index);
void Dfs(int v);
void Bfs(int v);
void Bfs2(int v);

int main(void) {

	int a, b;

	int s, v = 0;

	scanf("%d %d %d", &n, &m, &s);

	vert = (vertex*)malloc(n * sizeof(vertex));
	edges = (edge*)malloc(m * sizeof(edge));

	//vertex 초기화
	for (int i = 0; i < n; i++) {
		vert[i].v = i + 1;
		inc* newInc = (inc*)malloc(sizeof(inc));
		vert[i].inc = newInc;
		vert[i].inc->edge = -1;
		vert[i].inc->next = NULL;
		vert[i].isVisited = 0;
	}

	//edge 초기화
	for (int i = 0; i < m; i++) {
		edges[i].p = -1;
		edges[i].q = -1;
		edges[i].label = 'f';
	}

	for (int i = 0; i < m; i++) {
		scanf("%d %d", &a, &b);
		insertEdge(a, b);
	}

	// 시작 index찾기
	for (int i = 0; i < n; i++) {
		if (vert[i].v == s) {
			v = i;
			break;
		}
	}

	//Dfs(v);
	Bfs2(v);

	return 0;

}

void Dfs(int v) {

	int w = 0;
	vert[v].isVisited = 1;
	printf("%d\n", vert[v].v);

	inc* p = vert[v].inc;

	while (p->next != NULL) {

		p = p->next;
		int p1 = edges[p->edge].p;
		int q1 = edges[p->edge].q;

		if (edges[p->edge].label == 'f') {

			// 반대편 vertex 구하기
			w = (p1 == v) ? q1 : p1;

			// 방문한 노드인지 아닌지
			if (vert[w].isVisited == 0) {
				edges[p->edge].label = 't';
				Dfs(w);
			}
			else {
				edges[p->edge].label = 'b';
			}
		}
	}
}

void Bfs(int v) {

	int stack[100] = { 0, };
	int tmp[100] = { 0, };
	int i = 1, v2, tmpIdx, w, j = 0;
	inc* p;

	vert[v].isVisited = 1;
	stack[0] = v;

	while (i != 0) {

		for (int j = 0; j < i; j++) {
			printf("%d\n", vert[stack[j]].v);
			tmp[j] = stack[j];
		}

		// 반복의 시작일때 i 값을 0으로 초기화한다.
		int len = i;
		i = 0;

		// stack에 있던 값들을 tmp에 저장하고 tmp를 돈다
		// 그 다음 레벨의 노드들을 stack 저장.

		for (int l = 0; l < len; l++) {

			v = tmp[l];
			p = vert[v].inc;

			while (p->next != NULL) {

				p = p->next;
				int p1 = edges[p->edge].p;
				int q1 = edges[p->edge].q;

				// 반대편 vertex 구하기
				w = (p1 == v) ? q1 : p1;

				if (edges[p->edge].label == 'f') {

					// 새로운 노드 방문
					if (vert[w].isVisited == 0) {
						edges[p->edge].label = 't';
						vert[w].isVisited = 1;
						stack[i] = w;
						i++;
					}
					else {
						edges[p->edge].label = 'c';
					}

				}
			}
		}
	}
}


void Bfs2(int v) {

	int front = 0, rear = 0;
	int pop, w;
	inc* p;

	printf("%d\n", vert[v].v);
	queue[0] = v;
	rear++;
	vert[v].isVisited = 1;

	while (front < rear) {
		pop = queue[front];
		front++;
		p = vert[pop].inc;

		while (p->next != NULL) {

			p = p->next;
			int p1 = edges[p->edge].p;
			int q1 = edges[p->edge].q;

			// 반대편 vertex 구하기
			w = (p1 == pop) ? q1 : p1;

			if (edges[p->edge].label == 'f') {

				// 새로운 노드 방문
				if (vert[w].isVisited == 0) {
					edges[p->edge].label = 't';
					vert[w].isVisited = 1;
					printf("%d\n", vert[w].v);
					queue[rear] = w;
					rear++;
				}
				else {
					edges[p->edge].label = 'c';
				}

			}
		}

	}
}

void insertEdge(int a, int b) {

	int i = 0;

	while (1) {
		// 새 간선 추가
		if (edges[i].q == -1 || edges[i].q == -1) {

			edges[i].p = a - 1;
			edges[i].q = b - 1;
			buildIncList(a, b, i);
			return;
		}
		i++;
	}

}

void buildIncList(int a, int b, int index) {

	// edges 리스트에서 index번째 간선추가

	int i, j;
	int num = 0;
	inc* p = NULL, * q = NULL, * tmp = NULL;

	inc* newInc = (inc*)malloc(sizeof(inc));
	newInc->edge = index;

	p = vert[a - 1].inc;
	q = vert[b - 1].inc;

	//vertex 값.
	i = a - 1;
	j = b - 1;

	while (p->next != NULL) {
		tmp = p;
		p = p->next;

		// 각각 반복마다 해당 edge의 vertex 값, 반대에 연결된 값 구하기.
		num = (edges[p->edge].p == i ? edges[p->edge].q : edges[p->edge].p);

		// 오름차순으로 리스트를 만들기 위해.
		if (num > j) {
			tmp->next = newInc;
			newInc->next = p;
			break;
		}
	}


	// 삽입되는 부착 간선이 리스트의 맨 끝에 위치. 위 if문을 안들감.
	if (num <= j) {
		newInc->next = NULL;
		p->next = newInc;
	}

	// 루프간선일 경우 한번만 추가.
	if (i == j)
		return;

	// 반대쪽도 추가.
	inc* newInc2 = (inc*)malloc(sizeof(inc));
	newInc2->edge = index;
	num = 0;

	while (q->next != NULL) {

		tmp = q;
		q = q->next;

		// 해당 edge의 vertex 값, 반대에 연결된 값 구하기.
		num = (edges[q->edge].p == j ? edges[q->edge].q : edges[q->edge].p);

		// 오름차순으로 리스트를 만들기 위해.
		if (num > i) {
			tmp->next = newInc2;
			newInc2->next = q;
			break;
		}
	}
	// 삽입되는 부착 간선이 리스트의 맨 끝에 위치. 위 if문을 안들감.
	if (num <= i) {
		newInc2->next = NULL;
		q->next = newInc2;
	}
}
