class StudentNode:
    
    def __init__(self, roll_no, name, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.marks = marks
        self.left = None
        self.right = None

    def __str__(self):
        return f"Roll No: {self.roll_no:<5} | Name: {self.name:<15} | Course: {self.course:<10} | Marks: {self.marks:.1f}"


class StudentBST:
   
    def __init__(self):
        self.root = None

   
    def insert(self, roll_no, name, course, marks) -> None:
        
        new_student = StudentNode(roll_no, name, course, marks)
        if self.root is None:
            self.root = new_student
            print(f"Added record for {name} (Roll No: {roll_no}).")
            return

        curr = self.root
        while True:
            if roll_no < curr.roll_no:
                if curr.left is None:
                    curr.left = new_student
                    print(f"Added record for {name} (Roll No: {roll_no}).")
                    break
                curr = curr.left
            elif roll_no > curr.roll_no:
                if curr.right is None:
                    curr.right = new_student
                    print(f"Added record for {name} (Roll No: {roll_no}).")
                    break
                curr = curr.right
            else:
                print(f"Error: Roll No {roll_no} already exists!")
                break

    def search(self, roll_no: int) -> StudentNode | None:
        """Searches for a student by Roll Number in O(log N) time."""
        curr = self.root
        while curr:
            if curr.roll_no == roll_no:
                return curr
            elif roll_no < curr.roll_no:
                curr = curr.left
            else:
                curr = curr.right
        return None

 
    def display_in_order(self, node: StudentNode = None, is_root: bool = True) -> None:
        """Displays all student records sorted by Roll Number."""
        if is_root:
            print(f"\n{'=' * 65}")
            print("         STUDENT ADMISSION DIRECTORY (Sorted by Roll No)")
            print(f"{'=' * 65}")
            node = self.root

        if node:
            self.display_in_order(node.left, False)
            print(node)
            self.display_in_order(node.right, False)

        if is_root:
            print(f"{'=' * 65}")



if __name__ == "__main__":
    admission_system = StudentBST()

  
    admission_system.insert(105, "Rahul Sharma", "Computer Sci", 88.5)
    admission_system.insert(102, "Priya Patel", "Electronics", 92.0)
    admission_system.insert(108, "Aman Gupta", "Mechanical", 79.0)
    admission_system.insert(101, "Sanya Verma", "Civil", 85.0)
    admission_system.insert(104, "Rohan Das", "Computer Sci", 91.5)


    admission_system.display_in_order()

    
    search_id = 104
    print(f"\nSearching for Roll No: {search_id}...")
    result = admission_system.search(search_id)
    if result:
        print(f"Record Found -> {result}")
    else:
        print("Record Not Found!")
