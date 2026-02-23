name="Priya"

age=30

height=150.45

is_married=True

skills = ["Python", "FastAPI"]

print(type(name))
print(type(age))
print(type(height))
print(type(is_married))
print(type(skills))


#string to other types
num ='123'
num1=int(num)
num2=float(num)
num3=bool(num)
num4=list(num)

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))


#int to other types - list, dict not possible and same applies for float, boolean to other types.
age = 30
age1=float(age)
age2=str(age)
age3=bool(age)

print(type(age1))
print(type(age2))
print(type(age3))

# bool(0)        # False
# bool("")       # False
# bool([])       # False
# bool(None)     # False


#List to other types
numbers = [1, 2, 3]
set1=set(numbers)
tuple1=tuple(numbers)
str1=str(numbers)
bool1=bool(numbers)

print(set1, tuple1, str1, bool1)
print(type(set1))
print(type(tuple1))
print(type(str1))
print(type(bool1))


test = "45"
test1=int(test)
print(test1)
print(type(test1))

numb=100
numb1=str(numb)
print(numb1)
print(type(numb1))

zero=0
zero1=bool(zero)
print(zero1)
print(type(zero1))

arr=[1, 2, 3]
arr1=set(arr)
print(arr1)
print(type(arr1))

is_t=True
is_t1=int(is_t)
print(is_t1)
print(type(is_t1))



a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (gives decimal)
print(a // b)  # Floor division (whole number only)
print(a % b)   # Modulo (remainder)
print(a ** b)  # Exponent (10 to the power of 3)