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


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return None
        else:
            self.top -= 1
            return self.stack.pop()



def preorder(root):
    s = Stack()

    while root is not None or s.top != -1:

        while root is not None:
            print(root.data, end=" ")
            s.push(root)
            root = root.left

        root = s.pop()
        root = root.right


def inorder(root):
    s = Stack()

    while root is not None or s.top != -1:

        while root is not None:
            s.push(root)
            root = root.left

        root = s.pop()
        print(root.data, end=" ")
        root = root.right


def postorder(root):
    s1 = Stack()
    s2 = Stack()

    if root is None:
        return

    s1.push(root)

    while s1.top != -1:
        temp = s1.pop()
        s2.push(temp)

        if temp.left is not None:
            s1.push(temp.left)

        if temp.right is not None:
            s1.push(temp.right)

    while s2.top != -1:
        temp = s2.pop()
        print(temp.data, end=" ")



root = create()

print("\nPreorder traversal is:")
preorder(root)

print("\nInorder traversal is:")
inorder(root)

print("\nPostorder traversal is:")
postorder(root)
