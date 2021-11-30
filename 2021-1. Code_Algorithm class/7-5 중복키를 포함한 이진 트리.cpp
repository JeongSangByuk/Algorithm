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

	//root �����
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

	// �ߺ��� ���� �ִ��� �˻�.
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

		//left�� �ΰ�
		Node* z = p->lChild;

		// �ڽ��� exteranl�� ��带 z��
		if (!isExternal(z))
			z = p->rChild;

		//case 1 => �ڽ� �� �ϳ��� external ���
		if (isExternal(z)) {
			p = reduceExternal(z);
		}

		// case 2 => �ڽ� �� �� internal ���
		else {
			// y�� ���� ��ȸ ����ڷεд�.
			Node* y = inOrderSucc(p);

			// ���� ��ȸ ������� left child
			// reduce external �ϱ� ���ؼ�
			z = y->lChild;
			p->key = y->key;
			reduceExternal(z);
		}

		p = treeSearch(p, k);
	}
	printf("%d\n", e);
}

// exteranl ��忡�� ����, �θ� ������ ����.
Node* reduceExternal(Node* z) {
	Node* w = z->parent;
	Node* zs = sibling(z);

	// root �� ���. �� root ����.
	if (w->parent == NULL) {
		//renew Root
		root = zs;
		zs->parent = NULL;
		return zs;
	}

	// �����Ǵ� �θ� ����� �θ���
	// zs�� ����.
	Node* g = w->parent;
	zs->parent = g;

	// ���� �Ǵ� �θ�밡 left child���� ���
	if (w == g->lChild)
		g->lChild = zs;
	else if (w == g->rChild)
		g->rChild = zs;

	return zs;
}

// ������� get
Node* sibling(Node* w) {

	if (w->parent == NULL)
		return NULL;

	if (w->parent->lChild == w)
		return w->parent->rChild;
	else
		return w->parent->lChild;
}

// Ư�� internal ����� ������ȸ ����ڸ� ����.
Node* inOrderSucc(Node* w) {

	// �켱 ������ child�� �� ��,
	w = w->rChild;

	// No inorder successor
	if (isExternal(w))
		return NULL;

	// ���� ���� ���
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
		// right child���� �ߺ����� ���� ���� �ڸ���.
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