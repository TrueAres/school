class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    """ Your code goes here """
    def print_attributes(self):
        return "Length: " + self.length + ", width: " + self.width




rectangle1 = Rectangle()
rectangle1.length = int(input())
rectangle1.width = int(input())

rectangle2 = Rectangle()
rectangle2.length = int(input())
rectangle2.width = int(input())

rectangle1.print_attributes(input())
rectangle2.print_attributes(input())