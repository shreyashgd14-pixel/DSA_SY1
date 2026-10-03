class Node:
    def __init__(self, roll_no):
        self.roll_no = roll_no
        self.next = None


class AttendanceList:
    def __init__(self):
        self.head = None

    def insert(self, roll_no):
        new_node = Node(roll_no)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, roll_no):
        if self.head.roll_no == roll_no:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.roll_no == roll_no:
                curr.next = curr.next.next
                return
            curr = curr.next

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.roll_no))
            curr = curr.next
        print(" -> ".join(elements))


attendance = AttendanceList()

attendance.insert(21)
attendance.insert(22)
attendance.insert(23)
attendance.insert(24)

print("Initial Attendance:")
attendance.display()

print("\nDeleting Roll Number 21...")
attendance.delete(21)

print("\nInserting Roll Number 25...")
attendance.insert(25)

print("\nFinal Attendance List:")
attendance.display()
