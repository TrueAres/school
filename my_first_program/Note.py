"""
str1 = "hello world"
name = "Richard"


print(str1, ", my name is", name)

x = 12
x = 12 + 1
x = x + 1
print(x)

num1 = 17
num2 = 42
num3 = 9
greatest_num = num1
if num2 > num1:
    greatest_num = num2
if num3 > num2:
    greatest_num = num3
print(greatest_num)

import math as mm


mm.sqrt(16)


global_x=32

def function():
    x=12
    print(x)
    print(global_x)
    
function()


####### C code ###############
#int x;
#if (somthing is true)
#{
#    x = somthing;
#}

#x
##############################

if True :
    x=32

print(x)


flag = False

if flag :
    x=56
else :
    x=154 

print(x)

z=40
if z>3:
    if z<10:
        print(z)
    else:
        print("else")


print("done")

tmp = int(input("Input Temp"))

if tmp < 32:
    print("It's freezing!")
elif tmp < 61:
    print("It's chilly.")
elif tmp < 76:
    print("Nice wearher.")
else:
    print("It's hot!")

i=0 
while i < 6:
    print(i := i+1)

i = 0
while (i < 10):
	print(i)
	i += 1

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)




n = 3

for i in range(0,n):
    if i %3 == 0 and i % 5==0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else: print(i)


n=int(input())
for i in range (0,n):
    for j in range(0,i+1):
       print("*", end="")
    print()


ll = ["hello", "world", "why", "am", "I", "here"]
count = 0
for word in ll:
    for letter in word: 
        if letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y',]:
            count += 1

print(count)


while True:
    stdin = input("enter quit:")
    if stdin.lower() == "quit":
        break

stdin = ''
while stdin.lower() != "q":
    print(stdin)
    stdin = input("enter Q for quit:")

    


# Read input and split input into tokens
tokens = input().split()

sequence_list = []
for token in tokens:
    sequence_list.append(int(token))

print(f"Sequence: {sequence_list}")


for i in range(1, len(sequence_list) - 1):
    prev = sequence_list[i - 1]
    current = sequence_list[i]
    next = sequence_list[i + 1]

    if current < prev and current < next:
        print("Dunk:", prev, current, next)
         
        
favorite_food = {}


while True:
    entry = input().split()

    if entry[0].lower() == "quit":
        break
    key = entry[0]
    value = entry[1]

    favorite_food[key] = value

print("Favorite food:")
print(favorite_food)

orders_record = {}

input_line = input()
while input_line != "quit":
    name, food = input_line.split()
    orders_record[name] = food
    input_line = input()

sorted_orders = sorted(orders_record.items())

for name, food in sorted_orders:
    print(name, food)

email = input("Enter your email: ")
str = email.find(".")
str2 =email.find("@")
str3 = email.find(".", str2)
address = email[str3+1:]
first = email[:str]
last = email[str + 1:str2]
domain = email[str2+1:str3]
print(f"{first} {last} {domain} {address}")


import math
def area(s):
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
a=(int(input("")))
b=(int(input("")))
c=(int(input("")))
s=(a+b+c)/2
print(area(s))

import math

def hero_f(a,b,c):
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return A
x = hero_f(1,2,3)
print(x)

"""

def count_down(count:int)-> None:
    print(count)
    if count ==0: return
    count_down(count-1)
print("Count down") 
count_down(10)
print("blast off")