#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

typedef struct node {
	int data;

	struct node* left;
	struct node* right;
	struct node* queueLink;

}node;

typedef struct queue {
	struct node* front;
}queue;


void addNode(node* root, int data) {

	// newNode�� ���Ӱ� ������ ����̴�. �Ʒ��� ������ ����� ��� �ʵ带 �ʱ�ȭ ���ִ� �۾��̴�. 
	node* newNode = (node*)malloc(sizeof(node));
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->data = data;
	newNode->queueLink = NULL;

	//queue�� ������ ��带 �����ϱ� ���� ������ 
	node* p = root->queueLink;
	if (root->queueLink == NULL) {
		//���� root��� ���Խ� �ʵ� ��
		root->queueLink = root;
		root->data = data;
	}
	else {
		if (p->left == NULL) {
			//��� ����
			p->left = newNode;
			if (root->right == NULL) {
				//���� root ����� ���� ������ ä������ ������ �������� quelink��
				root->queueLink = root;
			}
			else {
				//queue ������ ���� ������ �̵� 
				while (p->queueLink != NULL) {
					p = p->queueLink;
				}
				// queue�� ����
				p->queueLink = newNode;
			}

		}
		else {
			if (root->right == NULL) {
				//���� root ����� ���� ������ ä������ ������ �������� quelink��
				root->right = newNode;
				root->queueLink = p->left;
				root->queueLink->queueLink = newNode;
			}
			else {
				//������ ��Ʈ ���� 
				p->right = newNode;
				//queue ������ ���� ������ �̵�
				while (p->queueLink != NULL) {
					p = p->queueLink;
				}
				//queue ����
				p->queueLink = newNode;
				//���� �� �����ؾ��� ����� ���� ���� 
				root->queueLink = root->queueLink->queueLink;
			}
		}
	}
}

int add(node* root) {
	if (root->left == NULL && root->right == NULL) {
		return root->data;
	}
	else {
		if (root->left != NULL && root->right != NULL) {
			return root->data + add(root->left) + add(root->right);
		}
		else if (root->left != NULL && root->right == NULL) {
			return root->data + add(root->left);
		}
		else if (root->left == NULL && root->right != NULL) {
			return root->data + add(root->right);
		}
	}
}

int max(int a, int b) {

	if (a > b)
		return a;
	return b;

}

int isInternal(node* node) {

	if (node->left != NULL || node->right != NULL)
		return 1;
	return 0;
}

int isExternal(node* node) {

	if (node->left == NULL && node->right == NULL)
		return 1;
	return 0;
}

int max1(node *node) {


	//printf("%d\n", node->data);

	// external node
	if (isExternal(node)) {
		return node->data;
	}
	int tmp = node->data + max(max1(node->left), max1(node->right));
	return tmp;
}

int max2(node* node) {
	if (isInternal(node) && isExternal(node->left) && isExternal(node->right)) {
		return node->data + node->left->data + node->right->data;
	}

	int a = max2(node->left);
	int b = max2(node->right);
	int c = max1(node->left) + max1(node->right);
	int m;

	if (a >= b && a >= c)
		m = a;
	else if (b >= c && b >= a)
		m = b;
	else if (c >= a && c > b)
		m = c;

	return node->data + m;
}

void preOrder(node* root) {
	if (root != NULL) {
		printf("%d\n", root->data);
		preOrder(root->left);
		preOrder(root->right);
	}
}

int main() {

	node* root = (node*)malloc(sizeof(node));
	root->left = NULL;
	root->right = NULL;
	root->queueLink = NULL;

	addNode(root, 36);
	addNode(root, 21);
	addNode(root, 6);
	addNode(root, 15);
	addNode(root, 30);
	addNode(root, 11);
	addNode(root, 10);
	addNode(root, 10);
	addNode(root, 19);
	addNode(root, 20);
	addNode(root, 14);
	addNode(root, 5);
	addNode(root, 9);
	addNode(root, 2);
	addNode(root, 7);

	//preOrder(root);
	printf("%d", max2(root));

	return 0;
}


