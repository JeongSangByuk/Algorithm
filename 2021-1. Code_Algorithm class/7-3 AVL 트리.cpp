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
int isExternal(Node* node);
int isInternal(Node* node);
void insertItem(int k);
int findElement(int k);
Node* treeSearch(Node* node, int k);
void print(Node* node);
Node* makeNode();
void expandExternal(Node* node);
int isBalanced(Node* node);
void searchAndFixAfterInsertion(Node* node);
Node* searchAndFixAfterRemoval(Node* node);
Node* restructure(Node* x, Node* y, Node* z);
void updateHeight(Node* node);
int getHeight(Node* node);
Node* sibling(Node* w);
Node* inOrderSucc(Node* w);
int isRoot(Node* node);
Node* reduceExternal(Node* z);
void removeElement(int k);

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
			removeElement(k);
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

void removeElement(int k) {

	Node* p = treeSearch(root, k);

	if (isExternal(p)) {
		printf("X\n");
		return;
	}

	int e = p->key;

	// left child로 두고
	Node* z = p->lChild;
	// 자식중 exteranl인 노드를 z로
	if (!isExternal(z))
		z = p->rChild;

	// 미리 zs 저장
	Node* zs = sibling(z);

	//case 1 => 자식 중 하나가 external 노드
	if (isExternal(z)) {
		reduceExternal(z);
	}
	//case 2 => 자식 둘 다 internal 노드
	else {
		// y를 중위 순회 계승자로둔다.
		Node* y = inOrderSucc(p);

		// 중위 순회 계승자의 left child
		// reduce external 하기 위해서
		z = y->lChild;
		p->key = y->key;
		reduceExternal(z);
	}

	if (zs->parent == NULL) {
		// 삭제된 노드가 root 일 경우, root renew
		root = zs;
		return;
	}

	updateHeight(zs->parent);

	printf("%d\n", e);

	root = searchAndFixAfterRemoval(zs->parent);
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

// exteranl 노드에서 삭제, 부모 노드까지 삭제.
Node* reduceExternal(Node* z) {
	Node* w = z->parent;
	Node* zs = sibling(z);

	// root 일 경우. 즉 root 삭제.
	if (w->parent == NULL) {
		//renew Root
		root = zs;
		zs->parent = NULL;
		return zs;
	}

	// 삭제되는 부모 노드의 부모노드
	// zs와 연결.
	Node* g = w->parent;
	zs->parent = g;

	// 삭제 되는 부모노가 left child였을 경우
	if (w == g->lChild)
		g->lChild = zs;
	else if (w == g->rChild)
		g->rChild = zs;

	return zs;
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

Node* searchAndFixAfterRemoval(Node* node) {

	Node* z = NULL;
	Node* fix = NULL;

	// 불균형한 노드를 찾는다.
	while (node) {
		if (isBalanced(node))
			node = node->parent;
		else {
			// z를 불균형한 노드로
			z = node;
			break;
		}
	}

	// root일 경우
	if (!node)
		return root;

	// 개조 시작. z가 불균형한 노드, 즉 최상위 노드
	// 개조는 즉 x, y, z를 정하는 과정.
	Node* y, * x;

	// y를 정할 때, 큰 child가 불균형한 것은 자명.
	y = (z->lChild->height) > (z->rChild->height) ? z->lChild : z->rChild;

	if (y->lChild->height > y->rChild->height)
		x = y->lChild;
	else if (y->lChild->height < y->rChild->height)
		x = y->rChild;

	// child의 크기가 같은 경우,
	// 둘 중 y와 같은 쪽의 자식을 x로 선택.
	else {
		if (y == y->parent->lChild)
			x = y->lChild;
		else
			x = y->rChild;
	}

	fix = restructure(x, y, z);

	// fix의 부모가 null 즉, root면 루트 노드 갱신.
	if (fix->parent == NULL) {
		return fix;
	}

	// z는 발견된 불균형 노드를 가르킴
	// 노드 비교를 통해서 fix로 변환
	if (fix->parent->lChild == z)
		fix->parent->lChild = fix;
	else
		fix->parent->rChild = fix;

	updateHeight(fix);

	// 삭제 후 1회의 개조만으로는 높이균형 속성을
	// 전역적으로 복구하지 못할 수 있기때문에, 재귀적 반복. => root에서 return
	return searchAndFixAfterRemoval(fix);
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

// 형제 노드 구하기.
Node* sibling(Node* w) {

	if (w->parent == NULL)
		return NULL;

	if (w->parent->lChild == w)
		return w->parent->rChild;
	else
		return w->parent->lChild;
}

// 특정 internal 노드의 중위순회 계승자를 구함.
Node* inOrderSucc(Node* w) {

	// 우선 오른쪽 child로 간 후,
	w = w->rChild;

	// No inorder successor
	if (isExternal(w))
		return NULL;

	// 가장 왼쪽 노드
	while (isInternal(w->lChild))
		w = w->lChild;
	return w;

}

int isRoot(Node* node) {
	if (node->parent == NULL)
		return 1;
	else return 0;
}





