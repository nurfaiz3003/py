## Practicing OOP
class Train():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

train = Train(3)

people = ["Faiz", "Ron", "Harry", "Ujang"]
for person in people:
    if train.add_passenger(person):
        print(f"Added {person} successfully.")
    else:
        print(f"{person} failed to add. No Available Seat.")

print("\n Registered Passenger:")
for person in train.passengers:
    print(f"- {person}")