// code is mainly taken from geeksforgeeks just for practising purposes.

#include <bits/stdc++.h>

using namespace std;

struct node {
    int key;
    struct node *left, *right;
};

// utility function to create new BST node
struct node* newNode(int item){
    struct node* temp = (struct node*) malloc(sizeof(struct node));
    temp->key = item;  // putting the value of item parameter inside the key field of temp instance of struct node
    temp->left = temp->right = NULL;
    return temp;
}

// inorder: left, root, right
void inorder(struct node* root)
{
    if (root != NULL) {
        inorder(root->left);
        cout << root->key;
        inorder(root->right);
    }
}

// preorder: root, left, right
void preorder(struct node* root)
{
    if (root != NULL) {
        cout << root->key;
        preorder(root->left);
        preorder(root->right);
    }
}

// postorder: left, right, root
void postorder(struct node* root)
{
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        cout << root->key;
    }
}

// insert a new funtion in BST
struct node* insert(struct node* node, int key)
{
    if (node == NULL){
        return newNode(key);
    }

    if (key < node->key){
        node->left = insert(node->left, key);
    }
    else{
        node->right = insert(node->right, key);
    }

    return node;
}

//minimum key value 
struct node* minValNode(struct node* node)
{
    struct node* current = node;
    while(current && current->left != NULL){    // cause min value would be in left
        current = current->left;
    }
    return current;
}

//maximum key value 
struct node* maxValNode(struct node* node)
{
    struct node* current = node;
    while(current && current->right != NULL){    //because max value would be in right
        current = current->right;
    }
    return current;
}


// Driver Code
int main()
{
    /* Let us create following BST
            50
        /     \
        30     70
        / \ / \
    20 40 60 80 */
    struct node* root = NULL;
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);
    root = insert(root, 60);
    root = insert(root, 80);
 
    cout << "Inorder traversal of the given tree \n";
    inorder(root); 
    cout<<endl;
    return 0;
}
 
// This code is contributed by shivanisinghss2110