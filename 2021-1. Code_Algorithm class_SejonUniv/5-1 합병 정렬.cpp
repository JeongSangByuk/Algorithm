#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

// 연결 리스트 노드 구조체
typedef struct NODE {
	int data;
	struct NODE* next;
}Node;

// 분할한 노드 임시 저장 구조체
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

	// left는 시작부터
	left = node;

	ptr = node;

	// right를 찾는다.
	for (int i = 0; i < mid - 1; i++) {
		ptr = ptr->next;
	}

	right = ptr->next;

	// 이걸 NULL로 초기화하기위해서 mid-1 까지,
	// left의 next를 null로, 즉 partition한다.
	ptr->next = NULL;

	result.left = left;
	result.right = right;

	return result;
}

Node* merge(Node* left, Node* right) {

	Node* result = NULL;

	//만약 둘중 하나가 빈 노드일경우 유효한 노드 바로 반환
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


// 이 메소드의 k는 개수
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
		// 정확한 개수를 위해.
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
