#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct edge {
	int p;
	int q;
	int weight;
}edge;

typedef struct incidence {
	// 간선 리스트 중 몇번째 간선인지
	int edge;
	struct incidence* next;
}inc;

typedef struct vertex {
	inc* inc;
	int v;
}vertex;

vertex vert[6];
edge edges[21];

void insertEdge(int a, int b, int w);
void buildIncList(int a, int b, int index);
void deleteIncList(int a, int b, int index);
void printNodes(int n);
int deg(int n);

int main(void) {

	char c;
	int n;
	int a, b, w;

	// vertex 초기화
	for (int i = 0; i < 6; i++) {
		vert[i].v = i + 1;
		inc* newinc = (inc*)malloc(sizeof(inc));
		vert[i].inc = newinc;
		vert[i].inc->edge = -1;
		vert[i].inc->next = NULL;
	}

	//edge 초기화
	for (int i = 0; i < 21; i++) {
		edges[i].p = -1;
		edges[i].q = -1;
		edges[i].weight = 0;
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

		if (c == 'd') {
			scanf("%d", &n);
			printf("%d\n", deg(n));
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
			buildIncList(a, b, i);
			return;
		}

		// 새 간선 추가가 아닌 경우
		else {
			int idx1 = edges[i].p;
			int idx2 = edges[i].q;

			// a와 b를 각각 끝점으로 갖는 edge존재.
			if ((vert[idx1].v == a && vert[idx2].v == b) ||
				(vert[idx2].v == a && vert[idx1].v == b)) {

				if (w != 0)
					edges[i].weight = w;

				// 가중치가 0이면 edge 삭제
				else {
					deleteIncList(a, b, i);

					// edge 리스트 update
					for (int j = i + 1; j < 21; j++) {

						// edges 리스트에서 유효값이 끝난 경우
						if (edges[j].weight == 0) {
							edges[j - 1].p = -1;
							edges[j - 1].q = -1;
							edges[j - 1].weight = 0;
							break;
						}

						edges[j - 1].weight = edges[j].weight;
						edges[j - 1].p = edges[j].p;
						edges[j - 1].q = edges[j].q;
					}
				}
				return;
			}
		}

		i++;
	}
}

void buildIncList(int a, int b, int index) {

	// edges 리스트에서 index번째 간선 추가

	int aVert, bVert;
	int num = 0;

	// p와 q는 간선에 부착된 vertex의 inc 포인터
	inc* p = NULL, * q = NULL, * tmp = NULL;

	inc* newInc = (inc*)malloc(sizeof(inc));
	newInc->edge = index;

	// 간선의 부착 vertex 구하기.
	for (aVert = 0; aVert < 6; aVert++) {
		if (vert[aVert].v == a)
			break;
	}
	p = vert[aVert].inc;

	// 간선의 부착 vertex 구하기.
	for (bVert = 0; bVert < 6; bVert++) {
		if (vert[bVert].v == b)
			break;
	}
	q = vert[bVert].inc;

	while (p->next != NULL) {

		// 이전 노드 임시 저장.
		tmp = p;
		p = p->next;

		// 오름순으로 inc 리스트를 유지하기위해
		// 해당 edge의 vertex 값, 반대에 연결된 vert값 구하기.
		if (edges[p->edge].p == aVert)
			num = edges[p->edge].q;
		else
			num = edges[p->edge].p;

		// 오름차순으로 리스트를 만들기 위해.
		if (bVert < num) {
			tmp->next = newInc;
			newInc->next = p;
			break;
		}
	}

	// 삽입되는 부착 간선이 리스트의 맨 끝에 위치. 위 if문을 안들감.
	if (num <= bVert) {
		newInc->next = NULL;
		p->next = newInc;
	}

	// 루프간선일 경우 한번만 추가.
	if (aVert == bVert)
		return;

	// 반대쪽 vert의 inc에도 추가.
	inc* newInc2 = (inc*)malloc(sizeof(inc));
	newInc2->edge = index;
	num = 0;

	while (q->next != NULL) {
		tmp = q;
		q = q->next;

		// 해당 edge의 vertex 값, 반대에 연결된 vert값 구하기.
		if (edges[q->edge].p == bVert)
			num = edges[q->edge].q;
		else
			num = edges[q->edge].p;

		// 오름차순으로 리스트를 만들기 위해.
		if (num > aVert) {
			tmp->next = newInc2;
			newInc2->next = q;
			break;
		}
	}

	// 삽입되는 부착 간선이 리스트의 맨 끝에 위치. 위 if문을 안들감.
	if (num <= aVert) {
		newInc2->next = NULL;
		q->next = newInc2;
	}

}

void deleteIncList(int a, int b, int index) {

	// index는 edge 리스트에서 삭제하는 간선 index

	inc* tmp = NULL;

	for (int i = 0; i < 6; i++) {

		inc* p = vert[i].inc;

		while (p->next != NULL) {

			// 이전 노드 미리 저장.
			tmp = p;
			p = p->next;

			// 삭제하는 edge의 index를 비교해서 맞을 경우.
			if (p->edge == index) {
				tmp->next = p->next;
				free(p);
				p = tmp;
			}

			// 삭제 이후 모든 간선 -1 씩해서 update
			else if (p->edge > index)
				(p->edge)--;
		}
	}
}

void printNodes(int n) {

	if (n < 1 || n > 6) {
		printf("-1");
		return;
	}

	// vert 찾기.
	int i = 0;
	for (i = 0; i < 6; i++)
		if (vert[i].v == n)
			break;

	inc* p = vert[i].inc;

	while (p->next != NULL) {
		p = p->next;

		if (edges[p->edge].p == i)
			printf(" %d", edges[p->edge].q + 1);

		else if (edges[p->edge].q == i)
			printf(" %d", edges[p->edge].p + 1);

		printf(" %d", edges[p->edge].weight);
	}

}

// 실습 외 추가 메소드 

int deg(int n) {

	int count = 0;

	// vert 찾기.
	int i = 0;
	for (i = 0; i < 6; i++)
		if (vert[i].v == n)
			break;

	inc* p = vert[i].inc;

	while (p->next != NULL) {
		count++;
		p = p->next;
	}
	return count++;
}

void opposite(vertex v, edge e) {

	inc* p = v.inc;

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

int areAdjacent(int v, int w) {

	int min, a, b;

	if (deg(v) < deg(w))
		min = v;
	else
		min = w;

	// vert 찾기.
	int i = 0;
	for (i = 0; i < 6; i++)
		if (vert[i].v == min)
			break;

	inc* p = vert[i].inc;

	while (p->next != NULL) {

		p = p->next;

		int idx1 = edges[p->edge].p;
		int idx2 = edges[p->edge].q;

		// a와 b를 각각 끝점으로 갖는 edge존재.
		if ((vert[idx1].v == v && vert[idx2].v == w) ||
			(vert[idx2].v == v && vert[idx1].v == w)) {
			return 1;
		}
	}
	return 0;
}



