#ValueError:

try:
    num =int("abc")
except ValueError:
    print("Cannot convert string to integer.")
    
#KeyError
try:
    data={"name":"Priya"}
    print(data["age"])
except KeyError:
    print("Key not found in dictionary.")
    
#TypeError
try:
    res=123+"abc"
    print(res)
except TypeError:
    print("Cannot add string and integer.")
    
try:
    num =int(input("Enter a number"))
    res=10/num
    print("Result:", res)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by Zero.")
finally:
    print("Execution finished. Cleaning up resources...")
