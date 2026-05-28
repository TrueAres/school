result = 0
user_input = int(input())
while user_input > -1:
    if user_input %2 == 0:
        print("miss")
        user_input = int(input())
    if user_input % 2 != 0:
        print("hit")
        result += 1
    user_input = int(input())
    
        
print(f"Result is {result}")