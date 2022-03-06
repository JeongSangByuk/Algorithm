#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>

// ���÷��� Ʈ��

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
void leftRotate(Node* x, Node* y);
void rightRotate(Node* x, Node* y);
void splay(Node* node);
int isRoot(Node* node);

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

void splay(Node* node) {

    if (isRoot(node)) {
        root = node;
        return;
    }

    // parent�� �θ��� zig or zag �� �ѹ���
    if (isRoot(node->parent)) {

        if (node == root->lChild)
            rightRotate(node, root);
        else
            leftRotate(node, root);
        root = node;
        return;
    }

    // �θ��� �θ����
    Node* x = node;
    Node* p = node->parent;
    Node* g = p->parent;

    // zig-zig ȸ��
    if (node == g->lChild->lChild) {
        rightRotate(p, g);
        rightRotate(x, p);
    }

    // zig-zig ȸ��
    else if (node == g->rChild->rChild) {
        leftRotate(p, g);
        leftRotate(x, p);
    }

    // zig-zag ȸ��
    else if (node == g->rChild->lChild) {
        rightRotate(x, p);
        leftRotate(x, g);
    }

    // zig-zag ȸ��
    else if (node == g->lChild->rChild) {
        leftRotate(x, p);
        rightRotate(x, g);
    }

    splay(node);
}

// zig ȸ��
void leftRotate(Node* x, Node* y) {

    y->rChild = x->lChild;
    x->lChild->parent = y;
    x->parent = y->parent;

    if (y->parent != NULL) {
        if (y == y->parent->lChild)
            y->parent->lChild = x;
        else
            y->parent->rChild = x;
    }

    x->lChild = y;
    y->parent = x;
}

// zag ȸ��
void rightRotate(Node* x, Node* y) {

    y->lChild = x->rChild;
    x->rChild->parent = y;
    x->parent = y->parent;

    if (y->parent != NULL) {
        if (y == y->parent->lChild)
            y->parent->lChild = x;
        else
            y->parent->rChild = x;
    }
    x->rChild = y;
    y->parent = x;

}

void insertItem(int k) {

    Node* p = treeSearch(root, k);

    // internal�� ��� => �ߺ��� ��.
    // exteranl ��尡 ��ȯ�ȴ�.
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

    splay(p);
    printf("root : %d\n", root->key);
}

void removeElement(int k) {

    Node* p = treeSearch(root, k);
    Node* tmp = p;

    if (isExternal(p)) {
        printf("X\n");
        return;
    }

    int e = p->key;

    //left�� �ΰ�
    Node* z = p->lChild;
    Node* zs;

    // �ڽ��� exteranl�� ��带 z��
    if (!isExternal(z))
        z = p->rChild;

    //case 1 => �ڽ� �� �ϳ��� external ���
    if (isExternal(z)) {
        zs = reduceExternal(z);
    }

    // case 2 => �ڽ� �� �� internal ���
    else {
        // y�� ���� ��ȸ ����ڷεд�.
        Node* y = inOrderSucc(p);

        // ���� ��ȸ ������� left child
        // reduce external �ϱ� ���ؼ�
        z = y->lChild;
        p->key = y->key;
        zs = reduceExternal(z);
    }
    printf("%d\n", e);

    splay(zs->parent);
}

// exteranl ��忡�� ����, �θ� ������ ����.
Node* reduceExternal(Node* z) {
    Node* w = z->parent;
    Node* zs = sibling(z);

    // root �� ���. �� root ����.
    if (w->parent == NULL) {
        //renew Root
        root = zs;
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

    if (isExternal(p)) {
        printf("X\n");
        splay(p->parent);
    }
    else {
        printf("%d\n", p->key);
        splay(p);
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

int isRoot(Node* node) {
    if (node->parent == NULL)
        return 1;
    else return 0;
}