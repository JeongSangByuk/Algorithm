#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {

	struct Node* prev;
	struct Node* next;
	char key;

}node;

typedef struct list {
	struct Node* head;
	struct Node* tail;
}list;

void add(list* list, int n, char value);
void deleteNode(list* list, int n);
node* getNodeByPosition(list* list, int position);
int getSize(list* list);
void get(list* list, int n);
void printAll(list* list);
node* makeNode();



int main() {

	list* nodeList = (list*)malloc(sizeof(list));

	nodeList->head = makeNode();
	nodeList->tail = makeNode();

	nodeList->head->next = nodeList->tail;
	nodeList->tail->prev = nodeList->head;

	int num, n;
	char c;
	scanf("%d", &num);


	for (int i = 0; i < num; i++) {

		char input;
		getchar();
		scanf("%c", &input);

		switch (input)
		{
		case 'A':
			scanf("%d ", &n);
			scanf("%c", &c);

			add(nodeList, n, c);
			break;

		case 'D':
			scanf("%d", &n);
			deleteNode(nodeList, n);
			break;

		case 'G':
			scanf("%d", &n);
			get(nodeList, n);
			break;

		case 'P':
			printAll(nodeList);
			break;

		default:
			break;
		}

	}


}

void add(list* list, int n, char value) {

	if (getSize(list) < n - 1 || n < 1) {
		printf("invalid position\n");
		return;
	}

	node* a = makeNode();
	a->key = value;

	node* nodeByN = getNodeByPosition(list, n - 1);

	a->prev = nodeByN;
	a->next = nodeByN->next;
	nodeByN->next->prev = a;
	nodeByN->next = a;
}

void deleteNode(list* list, int n) {

	if (getSize(list) < n || getSize(list) < 1 || n < 1) {
		printf("invalid position\n");
		return;
	}

	node* nodeByN = getNodeByPosition(list, n);

	nodeByN->prev->next = nodeByN->next;
	nodeByN->next->prev = nodeByN->prev;
}

node* getNodeByPosition(list* list, int position) {

	node* p = list->head;

	int i = 0;
	while (1) {

		if (i == position) {
			return p;
		}

		i++;
		p = p->next;
	}


}

int getSize(list* list) {

	int i = 0;
	node* p = list->head->next;

	while (p != list->tail) {
		i++;
		p = p->next;
	}

	return i;
}

void get(list* list, int n) {
	int i = 1;
	node* p = list->head->next;

	if (getSize(list) < n || n < 1) {
		printf("invalid position\n");
		return;
	}

	while (p != list->tail) {

		if (i == n) {
			printf("%c\n", p->key);
			return;
		}

		p = p->next;
		i++;
	}

}

void printAll(list* list) {
	node* p = list->head->next;

	while (p != list->tail) {
		printf("%c", p->key);
		p = p->next;
	}

	printf("\n");
}


node* makeNode() {
	node* newNode = (node*)malloc(sizeof(node));
	newNode->next = NULL;
	newNode->prev = NULL;
	return newNode;
}