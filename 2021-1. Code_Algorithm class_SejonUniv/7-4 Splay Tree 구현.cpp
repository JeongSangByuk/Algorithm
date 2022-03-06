#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>

// 스플래쉬 트리

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

    //root 만들기
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

    // parent가 부모라면 zig or zag 중 한번만
    if (isRoot(node->parent)) {

        if (node == root->lChild)
            rightRotate(node, root);
        else
            leftRotate(node, root);
        root = node;
        return;
    }

    // 부모의 부모까지
    Node* x = node;
    Node* p = node->parent;
    Node* g = p->parent;

    // zig-zig 회전
    if (node == g->lChild->lChild) {
        rightRotate(p, g);
        rightRotate(x, p);
    }

    // zig-zig 회전
    else if (node == g->rChild->rChild) {
        leftRotate(p, g);
        leftRotate(x, p);
    }

    // zig-zag 회전
    else if (node == g->rChild->lChild) {
        rightRotate(x, p);
        leftRotate(x, g);
    }

    // zig-zag 회전
    else if (node == g->lChild->rChild) {
        leftRotate(x, p);
        rightRotate(x, g);
    }

    splay(node);
}

// zig 회전
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

// zag 회전
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

    // internal일 경우 => 중복된 값.
    // exteranl 노드가 반환된다.
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

    //left로 두고
    Node* z = p->lChild;
    Node* zs;

    // 자식중 exteranl인 노드를 z로
    if (!isExternal(z))
        z = p->rChild;

    //case 1 => 자식 중 하나가 external 노드
    if (isExternal(z)) {
        zs = reduceExternal(z);
    }

    // case 2 => 자식 둘 다 internal 노드
    else {
        // y를 중위 순회 계승자로둔다.
        Node* y = inOrderSucc(p);

        // 중위 순회 계승자의 left child
        // reduce external 하기 위해서
        z = y->lChild;
        p->key = y->key;
        zs = reduceExternal(z);
    }
    printf("%d\n", e);

    splay(zs->parent);
}

// exteranl 노드에서 삭제, 부모 노드까지 삭제.
Node* reduceExternal(Node* z) {
    Node* w = z->parent;
    Node* zs = sibling(z);

    // root 일 경우. 즉 root 삭제.
    if (w->parent == NULL) {
        //renew Root
        root = zs;
        return zs;
    }

    // 삭제되는 부모 노드의 부모노드
    // zs와 연결.
    Node* g = w->parent;
    zs->parent = g;

    // 삭제 되는 부모노가 left child였을 경우
    if (w == g->lChild)
        g->lChild = zs;
    else if (w == g->rChild)
        g->rChild = zs;

    return zs;
}

// 형제노드 get
Node* sibling(Node* w) {

    if (w->parent == NULL)
        return NULL;

    if (w->parent->lChild == w)
        return w->parent->rChild;
    else
        return w->parent->lChild;
}

// 특정 internal 노드의 중위순회 계승자를 구함.
Node* inOrderSucc(Node* w) {

    // 우선 오른쪽 child로 간 후,
    w = w->rChild;

    // No inorder successor
    if (isExternal(w))
        return NULL;

    // 가장 왼쪽 노드
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