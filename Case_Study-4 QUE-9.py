class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    def __init__(self):
        self.root = None

    def get_postfix(self, node, result=None):
        if result is None:
            result = []
        if not node:
            return result
        
        self.get_postfix(node.left, result)
        self.get_postfix(node.right, result)
        result.append(str(node.value))
        
        return result




tree = ExpressionTree()
root = Node('*')

root.left = Node('+')
root.left.left = Node('A')
root.left.right = Node('B')

root.right = Node('-')
root.right.left = Node('C')
root.right.right = Node('D')

postfix_list = tree.get_postfix(root)
postfix_expression = " ".join(postfix_list)

print("Postfix Expression:", postfix_expression)
