class TrayStack:
    def __init__(self, capacity=30):
        self.capacity = capacity
        self.stack = []

    def push(self, tray_num, is_clean, is_damaged):
        if len(self.stack) >= self.capacity:
            print(f"Failed: Stack is full (max {self.capacity}).")
            return

        if any(tray == tray_num for tray in self.stack):
            print(f"Failed: Tray {tray_num} already exists.")
            return

        if not is_clean:
            print(f"Rejected: Tray {tray_num} is dirty.")
            return

        if is_damaged:
            print(f"Rejected: Tray {tray_num} is damaged.")
            return

        self.stack.append(tray_num)
        print(f"Added Tray {tray_num}")

    def pop(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        removed = self.stack.pop()
        print(f"Removed Tray {removed}")
        return removed

    def peek(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        print(f"Top Tray: {self.stack[-1]}")
        return self.stack[-1]

    def display(self):
        if not self.stack:
            print("Stack is empty.")
            return
       
        for tray in reversed(self.stack):
            print(f"Tray {tray} ")
     



if __name__ == "__main__":
    trays = TrayStack()

    
    trays.push(101, is_clean=True, is_damaged=False)  
    trays.push(102, is_clean=True, is_damaged=False)   
    trays.push(103, is_clean=False, is_damaged=False)  
    trays.push(104, is_clean=True, is_damaged=True)   
    trays.push(101, is_clean=True, is_damaged=False)   

    trays.display()
    trays.peek()
    trays.pop()
    trays.display()
