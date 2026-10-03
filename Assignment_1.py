class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0] * 5

    def insert(self, x):
        if self.top == 4:
            print("Stack is overflow....")
            return

        self.top = self.top + 1
        self.ST[self.top] = x

    def delete(self):
        if self.top == -1:
            print("Stack is underflow....")
            return

        y = self.ST[self.top]
        self.top = self.top - 1
        return y

    def display(self):
        if self.top == -1:
            print("Nothing to print")
            return

        for i in range(self.top, -1, -1):
            print(self.ST[i])


s = Stack()

s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)

s.display()

x = s.delete()
print("Deleted:", x)

s.display()


#This is the code given by sir , check it and make it correct
class Queue :
    def __init__(self):
        self.top=-1
        self.ST=-1
        self.QT=[0]*5 #Queue size is fixed to 5 , not more than 5 elements are possible
    

    def insert(self,x):
        if self.top==6:
            print("Stack is overflow....")
            return
        self.top=self.top+1

        self.ST[self.top]=x


    def delete(self):
        if self.top==-1:
            print("Nothing to  print..")
            return
        else:
            y=self.ST[self.top]

        self.top=self.ST 
        return y
       
    
    def display(self):
        if self.F==-1:
            print("Nothing to print")
            return
        for i in range(self.F,self.R+1):
            print(self.QT[i])

q=Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.insert(50)
q.insert(60)

q.display()

q.delete()
q.delete()

q.display()
