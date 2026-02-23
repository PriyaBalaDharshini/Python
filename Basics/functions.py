def square(num):
    return num * num

result = square(5)
print(result)   # Output: 25


def power (base, exponent=3): #double star ** operator in Python is used for exponentiation
    return base ** exponent
print(power(4))
print(power(4, 2))

# *args - for variable number of positional arguments

def add_num(*args):
    return sum(args)
print(add_num(1, 2, 3, 4, 5, 6, 9))

# **kwargs (for variable number of keyword arguments)

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Priya", age=30, is_married=True)