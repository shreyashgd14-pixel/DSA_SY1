class RestaurantTrayStack:
    def __init__(self, capacity: int = 30):
        self.capacity = capacity
        self.stack = []
        self.existing_tray_numbers = set()

    def add_tray(self, tray_number: int, condition: str, is_clean: bool):
        if len(self.stack) >= self.capacity:
            print(f"Error: Stack is full. Cannot add Tray #{tray_number}.")
            return False

        if tray_number in self.existing_tray_numbers:
            print(f"Error: Tray #{tray_number} already exists. Tray numbers must be unique.")
            return False

        if not is_clean:
            print(f"Rejected: Tray #{tray_number} is not clean. Only clean trays can be added.")
            return False

        if condition.lower() == "damaged":
            print(f"Rejected: Tray #{tray_number} is damaged.")
            return False

        tray = {
            "tray_number": tray_number,
            "condition": condition,
            "is_clean": is_clean
        }

        self.stack.append(tray)
        self.existing_tray_numbers.add(tray_number)
        print(f"Successfully added Tray #{tray_number} to the stack.")
        return True

    def remove_tray(self):
        if not self.stack:
            print("Error: Stack is empty. No tray to remove.")
            return None

        removed_tray = self.stack.pop()
        self.existing_tray_numbers.remove(removed_tray["tray_number"])
        print(f"Removed Tray #{removed_tray['tray_number']} from the top of the stack.")
        return removed_tray

    def peek_top_tray(self):
        if not self.stack:
            print("Stack is empty. No top tray available.")
            return None

        top_tray = self.stack[-1]
        print(f"Top Tray -> Tray #{top_tray['tray_number']} | Clean: {top_tray['is_clean']} | Condition: {top_tray['condition']}")
        return top_tray

    def display_stack(self):
        if not self.stack:
            print("\n Tray Stack Status ")
            print("The stack is currently empty.")
            
            return

        
        print(f"       TRAY STACK (Top to Bottom)         ")
        print(f"       Capacity: {len(self.stack)} / {self.capacity}")
        
        
        for index, tray in enumerate(reversed(self.stack)):
            position = "TOP" if index == 0 else f"Pos {len(self.stack) - index}"
            print(f"[{position:<6}] Tray #{tray['tray_number']:<4} | Status: Clean | Condition: {tray['condition']}")

        


if __name__ == "__main__":
    kitchen_stack = RestaurantTrayStack(capacity=30)

    kitchen_stack.add_tray(tray_number=101, condition="Good", is_clean=True)
    kitchen_stack.add_tray(tray_number=102, condition="Good", is_clean=True)
    kitchen_stack.add_tray(tray_number=103, condition="Damaged", is_clean=True)
    kitchen_stack.add_tray(tray_number=104, condition="Good", is_clean=False)
    kitchen_stack.add_tray(tray_number=101, condition="Good", is_clean=True)
    kitchen_stack.add_tray(tray_number=105, condition="Excellent", is_clean=True)

    kitchen_stack.display_stack()

    kitchen_stack.peek_top_tray()

    kitchen_stack.remove_tray()

    kitchen_stack.display_stack()
