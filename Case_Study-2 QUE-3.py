class BankCustomerQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, token_no: str, name: str):
        self.queue.append({"token": token_no, "name": name})
        print(f"Enqueued: {name} ({token_no})")

    def dequeue(self):
        served = self.queue.pop(0)
        print(f"Served: {served['name']} ({served['token']})")
        return served

    def view_next(self):
        return self.queue[0]

    def display_queue(self):
        print("\n--- Bank Customer Queue ---")
        for i, c in enumerate(self.queue, start=1):
            print(f"{i}. Token: {c['token']} | Name: {c['name']}")
       



if __name__ == "__main__":
    bank = BankCustomerQueue()

    bank.enqueue("T101", "Ananya Verma")
    bank.enqueue("T102", "Rajesh Kumar")
    bank.enqueue("T103", "Suresh Gupta")

    bank.display_queue()

    nxt = bank.view_next()
    print(f"Next in line: {nxt['name']} ({nxt['token']})\n")

  
    bank.dequeue()

   
    bank.display_queue()
