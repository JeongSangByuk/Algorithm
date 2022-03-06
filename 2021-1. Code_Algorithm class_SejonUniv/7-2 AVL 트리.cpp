#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct node {
	struct node* lChild;
	struct node* rChild;
	struct node* parent;

	int key;
	int height;
}Node;

Node* root;

void searchAndFixAfterInsertion(Node* node);
int isExternal(Node* node);
int isInternal(Node* node);
void insertItem(int k);
int findElement(int k);
Node* treeSearch(Node* node, int k);
void print(Node* node);
Node* makeNode();
void expandExternal(Node* node);
int isBalanced(Node* node);
Node* restructure(Node* x, Node* y, Node* z);
void updateHeight(Node* node);
int getHeight(Node* node);

int main(void) {
	char c;
	int k;
	int isQ = 1;

	// root 만들기
	root = makeNode();

	while (isQ) {

		scanf("%c", &c);
		getchar();

		switch (c)
		{
		case 'i':
			scanf("%d", &k);
			getchar();
			insertItem(k);
			break;

		case 'd':
			scanf("%d", &k);
			getchar();
			break;

		case 's':
			scanf("%d", &k);
			getchar();
			findElement(k);
			break;

		case 'p':
			print(root);
			printf("\n");
			break;

		case 'q':
			isQ = 0;
			break;

		default:
			break;
		}

	}

	return 0;
}

Node* makeNode() {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->lChild = NULL;
	newNode->rChild = NULL;
	newNode->parent = NULL;

	newNode->key = NULL;
	newNode->height = 0;
	return newNode;
}

void print(Node* node) {
	if (isExternal(node))
		return;
	printf(" %d", node->key);
	print(node->lChild);
	print(node->rChild);
}

int findElement(int k) {

	Node* p = treeSearch(root, k);

	if (isExternal(p)) {
		printf("X\n");
	}
	else {
		printf("%d\n", p->key);
		return p->key;
	}

}

void insertItem(int k) {

	Node* p = treeSearch(root, k);

	// 중복값
	if (isInternal(p))
		return;

	p->key = k;
	expandExternal(p);
	updateHeight(p->parent);
	searchAndFixAfterInsertion(p);
}

// 외부 노드를 내부 노드로 확장시킨다.
void expandExternal(Node* node) {

	Node* left, * right;

	node->lChild = makeNode();
	node->rChild = makeNode();
	node->height = 1;

	node->lChild->parent = node;
	node->rChild->parent = node;
}

// 불균형을 찾아보고 fix한다.
void searchAndFixAfterInsertion(Node* node) {

	Node* z = NULL;
	Node* fix = NULL;

	// 불균형한 노드를 찾는다. 그 노드를 z로
	while (node) {
		if (isBalanced(node))
			node = node->parent;
		else {
			z = node;
			break;
		}
	}

	if (!node)
		return;

	// 단일 회전 or 이중 회전
	// 높이가 더큰 child가 불균형한 것은 자명
	// 결국 x가 최하단.
	Node* y, * x;
	y = (z->lChild->height) > (z->rChild->height) ? z->lChild : z->rChild;
	x = (y->lChild->height) > (y->rChild->height) ? y->lChild : y->rChild;
	fix = restructure(x, y, z);

	// fix의 부모가 null 즉, root면 루트 노드 갱신.
	if (fix->parent == NULL) {
		root = fix;
		return;
	}

	// z는 발견된 불균형 노드를 가르킴
	// 노드 비교를 통해서 fix로 변환
	if (fix->parent->lChild == z)
		fix->parent->lChild = fix;
	else
		fix->parent->rChild = fix;

	updateHeight(fix);
}

Node* restructure(Node* x, Node* y, Node* z) {

	Node* a, * b, * c;
	Node* t0, * t1, * t2, * t3;

	if (z->rChild == y) {

		a = z;
		t0 = a->lChild;

		// case 1 : 단일 회전
		if (y->rChild == x) {
			b = y;
			c = x;
			t1 = b->lChild;
			t2 = c->lChild;
			t3 = c->rChild;
		}
		// case 3 : 이중 회전
		else {
			b = x;
			c = y;
			t1 = b->lChild;
			t2 = b->rChild;
			t3 = c->rChild;
		}
		b->parent = z->parent;

	}
	else {
		c = z;
		t3 = c->rChild;

		// case 2 : 단일 회전
		if (y->lChild == x) {
			b = y;
			a = x;
			t0 = a->lChild;
			t1 = a->rChild;
			t2 = b->rChild;
		}

		// case 4 : 이중 회전
		else {
			b = x;
			a = y;
			t0 = a->lChild;
			t1 = b->lChild;
			t2 = b->rChild;
		}
		b->parent = z->parent;
	}

	a->lChild = t0;
	a->rChild = t1;
	t0->parent = a;
	t1->parent = a;

	c->lChild = t2;
	c->rChild = t3;
	t2->parent = c;
	t3->parent = c;

	b->lChild = a;
	b->rChild = c;
	a->parent = b;
	c->parent = b;

	updateHeight(a);
	updateHeight(c);
	updateHeight(b);

	return b;
}


// k == key인 노드를 찾아서 반환함. 
// 이때 external이면 external한 노드를 반환(그 것이 즉 삽입되는 위치.).
Node* treeSearch(Node* node, int k) {

	if (isExternal(node))
		return node;

	if (k == node->key) {
		return node;
	}
	else if (k < node->key) {
		return treeSearch(node->lChild, k);
	}
	else if (k > node->key) {
		return treeSearch(node->rChild, k);
	}
}

// 높이 갱신 : 노드의 높이가 바뀌면 부모 노드의 높이도 바뀐다.
void updateHeight(Node* node) {

	if (!node)
		return;

	int l = getHeight(node->lChild);
	int r = getHeight(node->rChild);

	// 부모 노드의 높이는 자식 노드의 높이 중 큰값 + 1
	int max = l > r ? 1 + l : 1 + r;

	if (getHeight(node) != max)
		node->height = max;
	updateHeight(node->parent);
}

int isBalanced(Node* node) {

	// 좌우 child 둘중 하나라도 NULL 일 경우 해당 노드는 balanced
	if (node->lChild == NULL || node->rChild == NULL)
		return 1;

	if ((node->rChild->height) - (node->lChild->height) > 1 ||
		(node->lChild->height) - (node->rChild->height) > 1)
		return 0;
	else
		return 1;

}

int getHeight(Node* node) {

	if (node == NULL)
		return 0;
	return node->height;
}

int isExternal(Node* node) {
	if (node->lChild == NULL && node->rChild == NULL)
		return 1;
	return 0;
}

int isInternal(Node* node) {

	if (node->lChild != NULL || node->rChild != NULL)
		return 1;
	return 0;
}





