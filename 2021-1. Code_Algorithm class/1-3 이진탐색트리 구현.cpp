#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct Node {

	struct  Node* left;
	struct  Node* right;
	int data;
}Node;

Node* addNode(Node* node,int k) {

	if (node == NULL) {
		node = (Node*)malloc(sizeof(Node));
		node->left = NULL;
		node->right = NULL;
		node-> data = k;
		return node;
	}

	if (node->data > k) {
		node->left = addNode(node->left, k);
	}
	else {
		node->right = addNode(node->right, k);
	}

	return node;

}

void prePrint(Node* root) // 트리 출력하기 : 전위 순회  
{
	if (root)
	{
		printf("%d ", root->data);
		prePrint(root->left);
		prePrint(root->right);
	}
}


int main() {

	Node* root = NULL;
	root = addNode(root, 36);
	root = addNode(root, 21);
	root = addNode(root, 6);
	root = addNode(root, 15);
	root = addNode(root, 30);
	root = addNode(root, 11);
	root = addNode(root, 10);
	root = addNode(root, 10);
	root = addNode(root, 19);
	root = addNode(root, 20);
	root = addNode(root, 14);
	root = addNode(root, 5);
	root = addNode(root, 9);
	root = addNode(root, 2);
	root = addNode(root, 7);

	prePrint(root);

	return 0;
}


