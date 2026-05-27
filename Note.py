str1 = "hello world"
name = "Richard"


#print(str1, ", my name is", name)

x = 12
x = 12 + 1
x = x + 1
#print(x)

num1 = 17
num2 = 42
num3 = 9
greatest_num = num1
if num2 > num1:
    greatest_num = num2
if num3 > num2:
    greatest_num = num3
#print(greatest_num)

import math as mm


mm.sqrt(16)


global_x=32

def function():
    x=12
    print(x)
    print(global_x)
    
#function()


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

#print(x)


flag = False

if flag :
    x=56
else :
    x=154 

#print(x)

z=40
#if z>3:
#    if z<10:
#        print(z)
#    else:
#        print("else")


#print("done")

#tmp = int(input("Input Temp"))

#if tmp < 32:
#    print("It's freezing!")
#elif tmp < 61:
#    print("It's chilly.")
#elif tmp < 76:
#    print("Nice wearher.")
#else:
#    print("It's hot!")

#i=0 
#while i < 6:
#    print(i := i+1)

#i = 0
#while (i < 10):
#	print(i)
#	i += 1

#fruits = ["apple", "banana", "cherry"]
#for fruit in fruits:
#    print(fruit)




#n = 3_000_000

#for i in range(0,n):
#    if i %3 == 0 and i % 5==0:
#        print("fizzbuzz")
#    elif i % 3 == 0:
#        print("fizz")
#    elif i % 5 == 0:
#        print("buzz")
#    else: print(i)


n=int(input())
for i in range (0,n):
    for j in range(0,i+1):
        print("*", end="")
    print()
