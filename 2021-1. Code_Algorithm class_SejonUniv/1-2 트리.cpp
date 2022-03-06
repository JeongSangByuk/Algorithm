#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node
{
	struct Node* left;
	struct Node* right;
	int key;
}node;

node* makeNode(int value);

node* result = NULL;

void addNode(int n1, int n2) {
	if (n1 != 0) {
		result->left = makeNode(n1);
	}

	if (n2 != 0) {
		result->right = makeNode(n2);
	}
}

void findNode(node* p, int n) {

	if (p->key == n) {
		result = p;
	}
	else if (p->key != n) {

		if (p->left != NULL) {
			findNode(p->left, n);
		}
		if (p->right != NULL) {
			findNode(p->right, n);
		}
	}
}

node* makeRoot(int n1, int n2, int n3) {
	node* p1 = makeNode(n1);
	node* p2 = makeNode(n2);
	node* p3 = makeNode(n3);

	p1->left = p2;
	p1->right = p3;
	return p1;
}

node* makeNode(int value) {
	node* newNode = (node*)malloc(sizeof(node));

	if (value == 0)
		return NULL;

	newNode->key = value;
	newNode->left = NULL;
	newNode->right = NULL;

	return newNode;
}

void printNodes(node* root, char* str) {

	int len = strlen(str);
	node* temp = root;
	for (int i = 0; i < len + 1; i++) {
		printf(" %d", temp->key);

		if (*(str + i) == 'R') {
			temp = temp->right;
		}
		else if (*(str + i) == 'L') {
			temp = temp->left;
		}
		else {
			printf("\n");
			return;
		}
	}
	printf("\n");
}


int main()
{

	int count;
	int n1, n2, n3;
	node* root = NULL;

	scanf("%d", &count);

	for (int i = 0; i < count; i++) {
		scanf("%d", &n1);
		scanf("%d", &n2);
		scanf("%d", &n3);

		if (i == 0) {
			root = makeRoot(n1, n2, n3);
		}
		else {
			findNode(root, n1);
			addNode(n2, n3);
		}

	}


	scanf("%d", &count);
	getchar();

	char str[101];

	for (int i = 0; i < count; i++) {
		scanf("%s", str);
		printNodes(root, str);
		getchar();
	}

	return 0;
}



