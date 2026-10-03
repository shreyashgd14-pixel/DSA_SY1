class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    n = int(input("Enter data to create node (0 to stop): "))

    if n == 0:
        return None

    root = Node(n)

    print(f"Enter left of {n}:")
    root.left = create()

    print(f"Enter right of {n}:")
    root.right = create()

    return root



def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)



def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)



def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")



root = create()

print("\nPreorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)
