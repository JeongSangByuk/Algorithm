#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int key;
	struct Node* next;
}Node;

int m;
Node* arr;

void insertItem(int k);
int h(int x);
void initBucketArray();
void printElement();
int removeElement(int k);
int findElement(int k);

int main() {

	char c = '0';
	int k;
	scanf("%d", &m);
	getchar();
	arr = (Node*)malloc(sizeof(Node) * m);
	initBucketArray();

	while (c != 'e') {

		scanf("%c", &c);
		getchar();

		switch (c) {

		case 'i':
			scanf("%d", &k);
			insertItem(k);
			getchar();
			break;

		case 'd':
			scanf("%d", &k);
			printf("%d\n", removeElement(k));
			getchar();
			break;

		case 's':
			scanf("%d", &k);
			printf("%d\n", findElement(k));
			getchar();
			break;

		case 'p':
			printElement();
			break;

		default:
			break;
		}

	}
}

int h(int x) {
	return x % m;
}

void initBucketArray() {
	for (int i = 0; i < m; i++) {
		arr[i].key = i;
		arr[i].next = NULL;
	}
}

void insertItem(int k) {

	int value = h(k);
	Node* t = (Node*)malloc(sizeof(Node));
	t->key = k;
	t->next = NULL;

	// 있는지 검사
	if (arr[value].next == NULL) {
		arr[value].next = t;
	}
	else {
		t->next = arr[value].next;
		arr[value].next = t;
	}
}

void printElement() {
	Node* t = NULL;

	for (int i = 0; i < m; i++) {

		if (arr[i].next == NULL)
			continue;
		t = arr[i].next;

		while (t != NULL) {
			printf(" %d", t->key);
			t = t->next;
		}
	}
	printf("\n");

}

int findElement(int k) {

	int value = h(k);
	int count = 1;

	Node* t = arr[value].next;

	while (t != NULL) {
		if (t->key == k) {
			return count;
		}
		count++;
		t = t->next;
	}

	return 0;
}

int removeElement(int k) {

	int value = h(k);
	int count = 1;

	Node* t = arr[value].next;
	Node* temp = NULL;

	while (t != NULL) {
		if (t->key == k) {
			break;
		}
		count++;
		// temp에 이전값 저장.
		temp = t;
		t = t->next;
	}

	if (t == NULL)
		return 0;

	// 맨처음 원소 삭제일 경우
	if (temp == NULL)
		arr[value].next = t->next;
	else
		temp->next = t->next;

	return count;

}


