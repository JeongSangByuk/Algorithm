#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// ���� ����Ʈ ��� ����ü
typedef struct NODE {
	int data;
	struct NODE* next;
}Node;

// ������ ��� �ӽ� ���� ����ü
typedef struct TEMP_NODES {
	Node* left;
	Node* right;
}TempNodes;

int n;
void printNodes(Node* head);
Node* addNode(int k, Node* preNode);
void mergeSort(Node** node, int k);
TempNodes partition(Node* node, int mid);
Node* merge(Node* left, Node* right);

int main() {

	int tmp;
	Node* head = (Node*)malloc(sizeof(Node));
	Node* tmpNode;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {

		scanf("%d", &tmp);

		//head
		if (i == 0) {
			head->data = tmp;
			head->next = NULL;
			tmpNode = head;
			continue;
		}

		tmpNode = addNode(tmp, tmpNode);
	}
	mergeSort(&head, n);
	printNodes(head);


	return 0;
}

TempNodes partition(Node* node, int mid) {

	Node* ptr;
	Node* left, * right;

	TempNodes result;

	// left�� ���ۺ���
	left = node;

	ptr = node;

	// right�� ã�´�.
	for (int i = 0; i < mid - 1; i++) {
		ptr = ptr->next;
	}

	right = ptr->next;

	// �̰� NULL�� �ʱ�ȭ�ϱ����ؼ� mid-1 ����,
	// left�� next�� null��, �� partition�Ѵ�.
	ptr->next = NULL;

	result.left = left;
	result.right = right;

	return result;
}

Node* merge(Node* left, Node* right) {

	Node* result = NULL;

	//���� ���� �ϳ��� �� ����ϰ�� ��ȿ�� ��� �ٷ� ��ȯ
	if (left == NULL)
		return right;
	else if (right == NULL)
		return left;

	if (left->data < right->data) {
		result = left;
		result->next = merge(left->next, right);
	}
	else {
		result = right;
		result->next = merge(left, right->next);
	}

	return result;
}


// �� �޼ҵ��� k�� ����
void mergeSort(Node** node, int k) {

	int mid;
	Node* left = NULL;
	Node* right = NULL;
	TempNodes tempNodes;

	if (k > 1 && *node != NULL) {

		mid = k / 2;

		tempNodes = partition(*node, mid);
		left = tempNodes.left;
		right = tempNodes.right;

		mergeSort(&left, mid);
		// ��Ȯ�� ������ ����.
		mergeSort(&right, (int)((k / 2.0) + 0.5));
		*node = merge(left, right);
	}

}

Node* addNode(int k, Node* preNode) {

	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = k;
	newNode->next = NULL;

	preNode->next = newNode;
	return newNode;
}

void printNodes(Node* head) {

	Node* tmp = head;

	while (tmp != NULL) {
		printf(" %d", tmp->data);
		tmp = tmp->next;
	}

}
