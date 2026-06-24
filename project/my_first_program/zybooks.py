class Passenger:
    def __init__(self, num_checked_bags, travel_time, seat): 
        self.num_checked_bags = num_checked_bags
        self.travel_time = travel_time
        self.seat = seat

    def lost_checked_bag(self):
        self.num_checked_bags -= 1

    def print_data(self):
        print(f"Passenger data: {self.num_checked_bags} checked bags, {self.travel_time} hours travel time, seat {self.seat}")

num_checked_bags1 = int(input())
travel_time1 = int(input())
seat1 = input()

""" Your code goes here """
passenger1 = Passenger(num_checked_bags1, travel_time1, seat1)


print(f"Passenfer data: {passenger1.num_checked_bags} checked bags, {passenger1.travel_time} hours travel time, seat {passenger1.seat}")
passenger1.lost_checked_bag()
print(f"Passenfer data: {passenger1.num_checked_bags} checked bags, {passenger1.travel_time} hours travel time, seat {passenger1.seat}")
