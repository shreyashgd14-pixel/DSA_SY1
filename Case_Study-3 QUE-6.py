class Node:
    def __init__(self, passenger_id):
        self.passenger_id = passenger_id
        self.next = None


class RailwayWaitingList:
    def __init__(self):
        self.head = None

    def insert(self, passenger_id):
        new_node = Node(passenger_id)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, passenger_id):
        if self.head.passenger_id == passenger_id:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.passenger_id == passenger_id:
                curr.next = curr.next.next
                return
            curr = curr.next

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.passenger_id))
            curr = curr.next
        print(" -> ".join(elements))


waiting_list = RailwayWaitingList()

waiting_list.insert(201)
waiting_list.insert(202)
waiting_list.insert(203)

print("Initial List:")
waiting_list.display()

print("\nInserting Passenger 204...")
waiting_list.insert(204)
waiting_list.display()

print("\nDeleting Passenger 202...")
waiting_list.delete(202)

print("\nUpdated Waiting List:")
waiting_list.display()
