#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>

typedef struct node {
	struct node* lChild;
	struct node* rChild;
	struct node* parent;
	int key;
}Node;

Node* root;

int isExternal(Node* node);
int isInternal(Node* node);
void insertItem(int k);
int findElement(int k);
Node* treeSearch(Node* node, int k);
void print(Node* node);
Node* sibling(Node* w);
Node* inOrderSucc(Node* w);
void removeElement(int k);
Node* reduceExternal(Node* z);

int main() {

	char c;
	int isQ = 1;
	int k;

	//root 만들기
	root = (Node*)malloc(sizeof(Node));
	root->parent = NULL;
	root->lChild = NULL;
	root->rChild = NULL;

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

}

void insertItem(int k) {

	Node* p = treeSearch(root, k);

	// 중복된 값이 있는지 검사.
	while (isInternal(p)) {
		p = treeSearch(p->rChild, k);
	}

	Node* left = (Node*)malloc(sizeof(Node));
	Node* right = (Node*)malloc(sizeof(Node));

	p->key = k;
	p->lChild = left;
	p->rChild = right;
	left->parent = p;
	right->parent = p;
	left->lChild = NULL;
	left->rChild = NULL;
	right->lChild = NULL;
	right->rChild = NULL;
}

void removeElement(int k) {

	Node* p = treeSearch(root, k);

	if (isExternal(p)) {
		printf("X\n");
		return;
	}
	int e = p->key;

	while (isInternal(p)) {

		//left로 두고
		Node* z = p->lChild;

		// 자식중 exteranl인 노드를 z로
		if (!isExternal(z))
			z = p->rChild;

		//case 1 => 자식 중 하나가 external 노드
		if (isExternal(z)) {
			p = reduceExternal(z);
		}

		// case 2 => 자식 둘 다 internal 노드
		else {
			// y를 중위 순회 계승자로둔다.
			Node* y = inOrderSucc(p);

			// 중위 순회 계승자의 left child
			// reduce external 하기 위해서
			z = y->lChild;
			p->key = y->key;
			reduceExternal(z);
		}

		p = treeSearch(p, k);
	}
	printf("%d\n", e);
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

// 형제노드 get
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

void print(Node* node) {

	if (isExternal(node))
		return;

	printf(" %d", node->key);
	print(node->lChild);
	print(node->rChild);
}

int findElement(int k) {

	Node* p = treeSearch(root, k);

	if (isExternal(p))
		printf("X\n");
	else {
		printf("%d\n", p->key);
		return p->key;
	}

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

Node** findAllElement(int k) {
	int i = 0;
	Node *result[100];

	Node* w = treeSearch(root, k);

	while (isInternal(w)) {
		result[i] = w;
		i++;
		// right child에만 중복값이 있을 것은 자명함.
		w = treeSearch(w->rChild, k);
	}

	return result;
}

Node* treeSearch(Node* node, int k) {

	if (isExternal(node))
		return node;

	if (k == node->key) {
		return node;
	}
	else if (k < node->key)
		return treeSearch(node->lChild, k);
	else if (k > node->key)
		return treeSearch(node->rChild, k);

}