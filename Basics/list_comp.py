number =[1, 2, 3, 4, 5]
square=[]
for n in number:
    square.append(n*n)
print(square)

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

numbers1 = [11, 212, 34, 45, 58]
even = [n for n in numbers if n%2==0]
print(even)

result =["Even" if n%2==0 else "Odd" for n in numbers1]
print(result)

names = ["priya", "ram", "anu"]
upperC = [name.upper() for name in names]
print(upperC)

lowerC = [name.lower() for name in names]
print(lowerC)

#Create list of squares from 1 to 10.
sq = [n*n for n in range(1, 11)]
print(f"Square: {sq}")

#Create list of even numbers from 1 to 20.
list_even = [n for n in range(1, 21) if n%2==0]
print(f"Even: {list_even}")

#Create list of odd numbers from 1 to 20.
list_odd = [n for n in range(1, 21) if n%2!=0]
print(f"Even: {list_odd}")

#Remove empty space from a list.
arr=[" Apple ", " Ball ", " Cat "]
remove_space=[name.strip() for name in arr]
print(remove_space)

#Create list of string lengths.
length=[len(name) for name in arr]
print(length)

neg=[1, -9, 2, -8, 4, -8]
updated = [n if n >= 0 else "" for n in numbers]
print(updated)

data = ["hello", "", "world", "", "python", " ", "AI"]
cleaned = [item for item in data if len(item)!=0]
print(cleaned)
