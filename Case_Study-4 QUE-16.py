class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DepartmentTree:
    def __init__(self):
        self.root = None

    def postorder_recursive(self, node):
        if not node:
            return
        self.postorder_recursive(node.left)
        self.postorder_recursive(node.right)
        print(node.name)

    def postorder_non_recursive(self, root):
        if not root:
            return
        
        stack1 = [root]
        stack2 = []
        
        while stack1:
            curr = stack1.pop()
            stack2.append(curr)
            
            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)
                
        while stack2:
            node = stack2.pop()
            print(node.name)


tree = DepartmentTree()

root = Node("University")
root.left = Node("Engineering")
root.right = Node("Sciences")

root.left.left = Node("Computer Science")
root.left.right = Node("Electrical")

root.right.left = Node("Physics")
root.right.right = Node("Chemistry")

print("Postorder Traversal (Recursive):")
tree.postorder_recursive(root)

print("\nPostorder Traversal (Non-Recursive):")
tree.postorder_non_recursive(root)
