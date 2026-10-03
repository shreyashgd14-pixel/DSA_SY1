class Node:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.left = None
        self.right = None


class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, patient_id):
        if not self.root:
            self.root = Node(patient_id)
            return

        curr = self.root
        while True:
            if patient_id < curr.patient_id:
                if not curr.left:
                    curr.left = Node(patient_id)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(patient_id)
                    break
                curr = curr.right

    def postorder_recursive(self, node, result):
        if not node:
            return
        self.postorder_recursive(node.left, result)
        self.postorder_recursive(node.right, result)
        result.append(node.patient_id)

    def postorder_non_recursive(self, root):
        if not root:
            return []

        stack1 = [root]
        stack2 = []
        result = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr)

            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)

        while stack2:
            result.append(stack2.pop().patient_id)

        return result


hospital = PatientBST()

hospital.insert(104)
hospital.insert(102)
hospital.insert(108)
hospital.insert(101)
hospital.insert(103)

rec_result = []
hospital.postorder_recursive(hospital.root, rec_result)

non_rec_result = hospital.postorder_non_recursive(hospital.root)

print("Recursive Postorder:    ", rec_result)
print("Non-Recursive Postorder:", non_rec_result)
print("Traversal Sequences Match:", rec_result == non_rec_result)
