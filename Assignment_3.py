class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None

    def create(self):
        n = int(input("Enter no of nodes:"))
        if n<=0:
            print("Enter valid number of nodes.")
            return
        for n in range(1,n+1):
            val=input(f"Enter data for node{n}:")
            self.insert(val)

    def insert(self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def show(self):
        if self.head==None:
            print("Nothing to print...")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next

obj = LL()
obj.create()

obj.show()
