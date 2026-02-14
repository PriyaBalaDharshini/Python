Type conversion:
There are two types:
1. Implicit (automatic by Python)
2. Explicit (you convert manually)


Four Primary Built-in Collection Data Types
1. List
    a. use []
    b. ordered 
        1. Insertion order is preserved: When you add elements, Python remembers the sequence. Printing or iterating will
        2. always follow that same order unless you deliberately change it.
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
         print(d)  # {'a': 3, 'b': 2}
