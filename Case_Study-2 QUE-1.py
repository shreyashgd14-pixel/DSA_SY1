class RailwayTicketQueue:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.queue = []
        self.ticket_ids = set()

    def enqueue(self, ticket_id: str, name: str, is_confirmed: bool):
        if not is_confirmed:
            print(f"Error: '{name}' is not confirmed.")
            return
        if ticket_id in self.ticket_ids:
            print(f"Error: Ticket ID '{ticket_id}' already exists.")
            return
        if len(self.queue) >= self.capacity:
            print(f"Error: Queue is full (Max: {self.capacity}).")
            return

        passenger = {"id": ticket_id, "name": name}
        self.queue.append(passenger)
        self.ticket_ids.add(ticket_id)
        print(f"Enqueued: {name} ({ticket_id})")

    def dequeue(self):
        if not self.queue:
            print("Error: Queue is empty.")
            return None
        
        served = self.queue.pop(0)
        self.ticket_ids.remove(served["id"])
        print(f"Served: {served['name']} ({served['id']})")
        return served

    def front(self):
        if not self.queue:
            print("Error: Queue is empty.")
            return None
        return self.queue[0]

    def display_queue(self):
        print("\n--- Railway Ticket Queue ---")
        if not self.queue:
            print("Queue is empty.")
            return
        for i, p in enumerate(self.queue, start=1):
            print(f"{i}. ID: {p['id']} | Name: {p['name']}")
     


if __name__ == "__main__":
    q = RailwayTicketQueue(capacity=50)

   
    q.enqueue("T1001", "Aarav Sharma", True)
    q.enqueue("T1002", "Priya Patel", True)

      

    q.display_queue()

    first = q.front()
    if first:
        print(f"Front Passenger: {first['name']}\n")

  
    q.dequeue()
    q.display_queue()
