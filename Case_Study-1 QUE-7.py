class ParkingGarage:
    def __init__(self):
        self.capacity = 10
        self.stack = []

  
    def park_vehicle(self, vehicle_type, registration_no):
        if len(self.stack) >= self.capacity:
            print("Parking Garage is Full!")
            return

        if vehicle_type not in ["Car", "Bike"]:
            print("Only Car and Bike are allowed!")
            return

       
        for vehicle in self.stack:
            if vehicle["registration_no"] == registration_no:
                print("Vehicle registration number already exists!")
                return

        vehicle = {
            "type": vehicle_type,
            "registration_no": registration_no
        }

        self.stack.append(vehicle)
        print("Vehicle parked successfully.")

    def exit_vehicle(self):
        if len(self.stack) == 0:
            print("Parking Garage is Empty!")
            return

        vehicle = self.stack.pop()
        print("Vehicle exited:")
        print("Type:", vehicle["type"])
        print("Registration No:", vehicle["registration_no"])

    def top_vehicle(self):
        if len(self.stack) == 0:
            print("Parking Garage is Empty!")
            return

        vehicle = self.stack[-1]
        print("Top Parked Vehicle:")
        print("Type:", vehicle["type"])
        print("Registration No:", vehicle["registration_no"])

    def display(self):
        if len(self.stack) == 0:
            print("Parking Garage is Empty!")
            return

        print("\nParked Vehicles:")
        for i in range(len(self.stack) - 1, -1, -1):
            vehicle = self.stack[i]
            print(
                "Type:", vehicle["type"],
                "| Registration No:", vehicle["registration_no"]
            )


garage = ParkingGarage()

while True:
    print("\n--- Parking Garage ---")
    print("1. Park Vehicle")
    print("2. Exit Vehicle")
    print("3. Top Vehicle")
    print("4. Display Parked Vehicles")
    print("5. Exit Program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vehicle_type = input("Enter vehicle type (Car/Bike): ")
        registration_no = input("Enter registration number: ")
        garage.park_vehicle(vehicle_type, registration_no)

    elif choice == 2:
        garage.exit_vehicle()

    elif choice == 3:
        garage.top_vehicle()

    elif choice == 4:
        garage.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
