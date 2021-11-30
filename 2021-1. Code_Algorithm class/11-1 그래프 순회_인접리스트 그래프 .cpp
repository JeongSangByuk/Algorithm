#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct edge {
	int p;
	int q;
	// f : fresh ����, t : Ʈ�� ����, b : ���� ����
	char label;
}edge;

typedef struct incidence {
	// ���° �������� ����
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

	//vertex �ʱ�ȭ
	for (int i = 0; i < n; i++) {
		vert[i].v = i + 1;
		inc* newInc = (inc*)malloc(sizeof(inc));
		vert[i].inc = newInc;
		vert[i].inc->edge = -1;
		vert[i].inc->next = NULL;
		vert[i].isVisited = 0;
	}

	//edge �ʱ�ȭ
	for (int i = 0; i < m; i++) {
		edges[i].p = -1;
		edges[i].q = -1;
		edges[i].label = 'f';
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

			// �ݴ��� vertex ���ϱ�
			w = (p1 == v) ? q1 : p1;

			// �湮�� ������� �ƴ���
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

		// �ݺ��� �����϶� i ���� 0���� �ʱ�ȭ�Ѵ�.
		int len = i;
		i = 0;

		// stack�� �ִ� ������ tmp�� �����ϰ� tmp�� ����
		// �� ���� ������ ������ stack ����.

		for (int l = 0; l < len; l++) {

			v = tmp[l];
			p = vert[v].inc;

			while (p->next != NULL) {

				p = p->next;
				int p1 = edges[p->edge].p;
				int q1 = edges[p->edge].q;

				// �ݴ��� vertex ���ϱ�
				w = (p1 == v) ? q1 : p1;

				if (edges[p->edge].label == 'f') {

					// ���ο� ��� �湮
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

			// �ݴ��� vertex ���ϱ�
			w = (p1 == pop) ? q1 : p1;

			if (edges[p->edge].label == 'f') {

				// ���ο� ��� �湮
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
		// �� ���� �߰�
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

	// edges ����Ʈ���� index��° �����߰�

	int i, j;
	int num = 0;
	inc* p = NULL, * q = NULL, * tmp = NULL;

	inc* newInc = (inc*)malloc(sizeof(inc));
	newInc->edge = index;

	p = vert[a - 1].inc;
	q = vert[b - 1].inc;

	//vertex ��.
	i = a - 1;
	j = b - 1;

	while (p->next != NULL) {
		tmp = p;
		p = p->next;

		// ���� �ݺ����� �ش� edge�� vertex ��, �ݴ뿡 ����� �� ���ϱ�.
		num = (edges[p->edge].p == i ? edges[p->edge].q : edges[p->edge].p);

		// ������������ ����Ʈ�� ����� ����.
		if (num > j) {
			tmp->next = newInc;
			newInc->next = p;
			break;
		}
	}


	// ���ԵǴ� ���� ������ ����Ʈ�� �� ���� ��ġ. �� if���� �ȵ鰨.
	if (num <= j) {
		newInc->next = NULL;
		p->next = newInc;
	}

	// ���������� ��� �ѹ��� �߰�.
	if (i == j)
		return;

	// �ݴ��ʵ� �߰�.
	inc* newInc2 = (inc*)malloc(sizeof(inc));
	newInc2->edge = index;
	num = 0;

	while (q->next != NULL) {

		tmp = q;
		q = q->next;

		// �ش� edge�� vertex ��, �ݴ뿡 ����� �� ���ϱ�.
		num = (edges[q->edge].p == j ? edges[q->edge].q : edges[q->edge].p);

		// ������������ ����Ʈ�� ����� ����.
		if (num > i) {
			tmp->next = newInc2;
			newInc2->next = q;
			break;
		}
	}
	// ���ԵǴ� ���� ������ ����Ʈ�� �� ���� ��ġ. �� if���� �ȵ鰨.
	if (num <= i) {
		newInc2->next = NULL;
		q->next = newInc2;
	}
}
