
class WordNode:
    def __init__(self, word_id):
        self.data = word_id
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word_id):
        
        if self.root is None:
            self.root = WordNode(word_id)
        else:
            self._insert_recursive(self.root, word_id)

    def _insert_recursive(self, node, word_id):
        if word_id < node.data:
            if node.left is None:
                node.left = WordNode(word_id)
            else:
                self._insert_recursive(node.left, word_id)
        elif word_id > node.data:
            if node.right is None:
                node.right = WordNode(word_id)
            else:
                self._insert_recursive(node.right, word_id)
                
def preorder(temp):
    if temp is not None:
        print(temp.data, end=" ")
        preorder(temp.left)
        preorder(temp.right)

def inorder(temp):
    if temp is not None:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)        

def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")
        
tree = BinarySearchTree()
x = list(map(int, input("Enter your values with spaces ").split()))
for value in x:
    tree.insert(value)

print(f"\nPreorder Traversal: {x}")
preorder(tree.root)
print(f"\nInorder Traversal: {x}")
inorder(tree.root)
print(f"\nPostorder Traversal: {x}")
postorder(tree.root)            
