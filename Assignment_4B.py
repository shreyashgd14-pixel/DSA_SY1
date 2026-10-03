class Node:
    def __init__(self, book_id):
        self.book_id = book_id
        self.left = None
        self.right = None


class Library:
    def __init__(self):
        self.root = None

    
    def insert(self, book_id):
        new_node = Node(book_id)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if book_id < current.book_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.book_id, end=" ")
            self.inorder(root.right)

   
    def preorder(self, root):
        if root is not None:
            print(root.book_id, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Recursive Postorder Traversal
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.book_id, end=" ")



library = Library()


library.insert(50)
library.insert(30)
library.insert(70)
library.insert(20)
library.insert(40)
library.insert(60)
library.insert(80)


print("Inorder Traversal:")
library.inorder(library.root)

print("\n\nPreorder Traversal:")
library.preorder(library.root)

print("\n\nPostorder Traversal:")
library.postorder(library.root)
