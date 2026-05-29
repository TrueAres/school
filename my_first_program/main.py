orders_record = {}

input_line = input()
while input_line != "quit":
    name, food = input_line.split()
    orders_record[name] = food
    input_line = input()

sorted_orders = sorted(orders_record.items())

for name, food in sorted_orders:
    print(name, food)