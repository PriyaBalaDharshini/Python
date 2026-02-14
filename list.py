#List
fruits=["apple", "banana", "cherry"]

# 1. append(x) → Add item at the end
fruits.append("kiwi") # Not able to add more than a element
print(fruits)

# 2. insert(i, x) → Insert item at index
fruits.insert(2, "blueberry")
print(fruits)

# 3. remove(x) → Remove first occurrence of value
fruits1=["apple", "banana", "cherry", "banana", "kiwi"]
fruits1.remove("banana")
print(fruits1)

# 4. pop([i]) → Remove and return item at index (last if not specified)
fruits.pop()
print(fruits)
print(fruits1)
fruits1.pop(1)
print(fruits1)

# 5. clear() → Remove all items fruits.clear() print(fruits) # []
fruits1.clear()
print(fruits1)

# 6. extend(iterable) → Add multiple items from another iterable
colors1=["red", "blue", "green"]
colors2=["black", "orange", "violet"]
colors1.extend(colors2)
print(colors1)

# 7. index(x) → Return index of first occurrence
letters=["a", "b", "c", "b", "d", "e", "a", "v", "a"]
print(letters.index("b"))

# 8. count(x) → Count occurrences of value
print(letters.count("a"))

# 9. sort() → Sort list ascending (can use key/reverse)
letters.sort()
print(letters)

# 10. reverse() → Reverse order of list
letters.reverse()
print(letters)

# 11. copy() → Return shallow copy of list
new = fruits.copy()
print(new)

my_list=["start", "tree", "van", "ball", "can"]
#my_list.sort()

# 12. sort() → Sort list descending
my_list.sort(reverse=True)
print(my_list)

# 13. sum() -> Sum of all the elements
my_num=[23, 56, 82, 65]
total=sum(my_num)
print(total)

# 14. max() -> Find the largest number
largest = max(my_num)
print(largest)

# 15. reverse without reverse()
process=["open", "start", "use", "complete", "end", "close"]
rev_list=process[::-1] #using slicing
print(rev_list)

#16. Remove duplicates
process=["open", "start", "use", "complete", "end", "close", "open"]
dup=list(set(process))
print(dup)

numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[1:4])
print(numbers[2:])     # [30, 40, 50, 60, 70] → starts at index 2
print(numbers[4:])     # [50, 60, 70] → starts at index 4
print(numbers[:3])     # [10, 20, 30] → stops before index 3
print(numbers[:5])     # [10, 20, 30, 40, 50] → stops before index 5
print(numbers[::2])    # [10, 30, 50, 70] → every 2nd element
print(numbers[1::2])   # [20, 40, 60] → start at index 1, then every 2nd element
print(numbers[::3])    # [10, 40, 70] → every 3rd element
print(numbers[1:6:2])  # [20, 40, 60] → from index 1 to 5, step 2
print(numbers[0:7:3])  # [10, 40, 70] → from index 0 to 6, step 3
print(numbers[-4:-1])   # [40, 50, 60] → slice from 4th-last to 1st-last
print(numbers[::-1])    # [70, 60, 50, 40, 30, 20, 10] → reverse list
print(numbers[5:2:-1])  # [60, 50, 40] → start at index 5, go backwards to index 3



