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
	int k;
	int isQ = 1;

	// root 만들기
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

void print(Node* node) {
	if (isExternal(node))
		return;
	printf(" %d", node->key);
	print(node->lChild);
	print(node->rChild);
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

Node* inOrderSucc(Node* w) {

	// 일단 오른쪽 child로 간후,
	w = w->rChild;

	// No inorder successor
	if (isExternal(w))
		return NULL;

	// 가장 왼쪽노드.
	while (isInternal(w->lChild))
		w = w->lChild;
	return w;
	
}

void removeElement(int k) {

	Node* p = treeSearch(root, k);

	if (isExternal(p)) {
		printf("X\n");
		return ;
	}

	int e = p->key;

	// left로 두고
	Node* z = p->lChild;
	// external 이면 right로
	if (!isExternal(z))
		z = p->rChild;

	//case 1 => 자식 중 하나가 external 노드
	if (isExternal(z)) {
		reduceExternal(z);
	}
	//case 2 => 자식 둘 다 internal 노드
	else {
		Node* y = inOrderSucc(p);
		z = y->lChild;
		p->key = y->key;
		reduceExternal(z);
	}
	printf("%d\n",e);
}

//external 없앤다. 즉 부모노드까지ㅡ
Node* reduceExternal(Node* z) {
	Node* w = z->parent;
	Node* zs = sibling(z);

	if (w->parent == NULL) {
		//renew Root
		root = zs;
		return zs;
	}

	Node* g = w->parent;
	zs->parent = g;

	if (w == g->lChild)
		g->lChild = zs;
	else if (w == g->rChild)
		g->rChild = zs;

	return zs;

}

void insertItem(int k) {

	Node *p = treeSearch(root, k);

	if (isInternal(p))
		return;

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


