#1. count - Returns the number of times a value appears in the tuple.

t1=(1, 2, 3, 2, 4, 2)
print(t1.count(4))

#2. index(value, [start], [end]) - Returns the index of the first occurrence of a value. Optional start and end can limit the search.
t1 = (11, 22, 33, 22, 44, 22, 78, 53, 44, 89, 44, 76)
print(t1.index(44))
print(t1.index(44, 5, 9))

t = (5, 10, 15, 20)

print(len(t))       # 4 → length of tuple
print(max(t))       # 20 → largest element
print(min(t))       # 5 → smallest element
print(sum(t))       # 50 → sum of elements

# list to tuple conversion
my_list = [1, 2, 3]
my_tuple=tuple(my_list)
print(my_tuple)

# tuple to list conversion
my_tuple1 = (23, 45, 67)
my_list1 =list(my_tuple1)
print(my_list1)