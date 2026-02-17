# 1. Iterating over a list

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)

#2. Iterating over a string
string = "Python"
for i in string:
    print(i)

#3. Iterating over a range
# range(start, end, step) generates a sequence of numbers.

#simple range
for i in range(5):
    print(i) 

#range   with start and end (end-1)

for i in range (4, 7):
    print(i)

# Range with step
for i in range(0, 10, 3):
    print(i)