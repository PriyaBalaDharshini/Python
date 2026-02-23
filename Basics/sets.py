# 1. add Adds an element to the set.
set1={"apple",  "ball", "cat"}
set1.add("egg")
print(set1)

# 2. update Adds multiple elements from another iterable.

set2={"apple",  "ball", "cat"}
set2.update(["egg", "frog", "goat"])
print(set2)

# 3. remove(x) Removes an element; raises error if not found.
set3 = {'egg', 'ball', 'apple', 'goat', 'frog', 'cat'}
set3.remove("apple")
print(set3)

# 4. discard(x) Removes an element; does nothing if not found.
set4 = {'egg', 'ball', 'apple', 'goat', 'frog', 'cat'}
set4.discard("Tree")
print(set4)

#5. pop() removes and returns random element
set5 = {'egg', 'ball', 'apple', 'goat', 'frog', 'cat'}
set5.pop()
print(set5)

#6. union() Returns a new set with all elements from both.

set_a= {1, 2, 3,5 ,4, }
set_b={'goat', 'apple', 'ball', 'egg', 'cat'}
print(set_a.union(set_b))

#7. intersection Returns common elements

setA={'goat', 'apple', 'ball', 'egg', 'cat'}
setB={'tree', 'apple', 'van', 'egg', 'dog'}
print(setA.intersection(setB))

#Membership testing (fast lookups)
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)   # True
print("orange" in fruits)  # False

