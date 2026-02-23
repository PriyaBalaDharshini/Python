Type conversion:
There are two types:

1. Implicit (automatic by Python)
2. Explicit (you convert manually)

Four Primary Built-in Collection Data Types

1. List
   a. use []
   b. ordered 1. Insertion order is preserved: When you add elements, Python remembers the sequence. Printing or iterating will 2. always follow that same order unless you deliberately change it.
   Index-based operations: Each element has a fixed position (index). You can insert, delete, or access items based on their index
   c. changable (Mutable)
   d. Allow duplicate value

Key Features:
Indexing → numbers[0]
Negative indexing → numbers[-1]
Slicing → numbers[0:2]
Can store mixed types
Dynamic size (can grow/shrink)

Common Methods:
append()
insert()
remove()
pop()  
 sort()
reverse()
count()
index()

2. Dictionary
   a. uses {}
   b. Store values in key pair
   c. Mutable
   d. Keys must be unique
   e. does not allow duplicate keys (Keys must be unique, Values can be duplicated)
   e.g.:
   d = {"a": 1, "b": 2, "a": 3}
   print(d) # {'a': 3, 'b': 2}

3. Tuples
   a. Uses ()
   b. Ordered
   c. Immutable
   d. Allow duplicates
   e. Heterogeneous

   Common Methods:
   Tuple methods: count(), index()
   Useful built-ins: len(), max(), min(), sum()
   Conversions: tuple(), list()

Lists and tuples share many properties: both are ordered, can store mixed data types, allow duplicates, and support indexing/slicing. The big difference lies in mutability—lists are mutable, tuples are immutable

Use Cases
Lists (Mutable)
a. Storing items that change over time (shopping cart, to-do list).
b. Collections where you need frequent insertions, deletions, or updates.
c. Iterating and modifying data dynamically.

Tuples (Immutable)
a. Representing fixed data like coordinates (x, y), RGB colors (255, 0, 0).

4. Sets
   a. Uses {}
   b. Unordered: Elements don’t have a fixed position or index.
   c. Unique values only: Duplicates are automatically removed.
   d. Mutable
   e. No indexing/slicing: Unlike lists or tuples, you can’t access elements by position.

for loop:
syntax:
for variable in sequence: # code block

Function:
A function is a reusable block of code that performs a specific task.
Defined using def:

String Operations
Strings are
a. Immutable
b. Ordered
c. Indexed

List Comprehension
This is basically a shortcut way to write loops that create lists.

    Basic Syntax
    [new_value for item in iterable]
    [n * n for n in numbers]

    [item for item in iterable if condition]
    [n for n in numbers if n % 2 == 0]

    [value_if_true if condition else value_if_false for item in iterable]
    [n if n > 0 else 0 for n in numbers]

    Why use list comprehension?
    1. Cleaner
    2. Faster execution
    3. More Pythonic
    4. Improves readability for simple transformations


Exception Handling with try and except
    Prevents the program from crashing when an error occurs
    The finally Block:
      Runs cleanup code no matter what happens (error or no error)
         a. ValueError: Wrong type of value given - int("abc")
         b. KeyError: Accessing a dictionary key that doesn’t exist - my_dict["missing_key"]
         c. TypeError: Using an operation on the wrong type - "abc" + 123

File Handling:
   syntax:
   file = open("filename.txt", "mode")

   "r"	Read (default). File must exist: open("file.txt", "r")
   "w"	Write. Creates new file or overwrites existing: open("file.txt", "w")
   "a"	Append. Adds new content at the end: open("file.txt", "a")
   "r+"	Read and write. File must exist: open("file.txt", "r+")
   "w+"	Write and read. Overwrites file: open("file.txt", "w+")


Object-Oriented Programming:
Organize code into reusable structures called classes and objects
   Class: Blueprint for creating objects.
   Object: Instance of a class with its own data and behavior.

   OOP helps structure large programs, making them easier to maintain and extend.

json.dump() → Python ➜ JSON (into file)
json.dumps() → Python ➜ JSON string
json.load() → JSON file ➜ Python (Read JSON from file)
json.loads() → JSON string ➜ Python (Convert string to Python object)