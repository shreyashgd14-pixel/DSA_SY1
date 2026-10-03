class Node:
    def __init__(self, book_id):
        self.book_id = book_id
        self.left = None
        self.right = None


class LibraryBST:
    def __init__(self):
        self.root = None

    def insert(self, book_id):
        if not self.root:
            self.root = Node(book_id)
            return

        curr = self.root
        while True:
            if book_id < curr.book_id:
                if not curr.left:
                    curr.left = Node(book_id)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(book_id)
                    break
                curr = curr.right

    def preorder(self, node):
        if not node:
            return
        print(node.book_id, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)


library = LibraryBST()

library.insert(104)
library.insert(102)
library.insert(108)
library.insert(101)
library.insert(103)

print("Preorder Traversal of Book IDs:")
library.preorder(library.root)
print()
