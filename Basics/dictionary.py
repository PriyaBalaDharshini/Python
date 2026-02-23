user = {
    "name":"Priya",
    "age":30,
    "is_married":True
}

print(user)
user["name"]="Lawvenya"
user["is_married"]=False
user["city"]="Cbe"
del user["age"]
print(user)

# 1. fromkeys(seq, value) → Creates dict from keys with same value
# the dict.fromkeys() method can only assign a single, shared value to all keys
keys =["a", "b", "c"]
new_dict=dict.fromkeys(keys, 10)
print(new_dict)

# 2. zip To assign different values to each key
key1=["aa", "bb", "cc"]
value1=[11, 22, 33]
dict1=dict(zip(key1, value1))
print(dict1)

# 3. get(key) → Returns value for key
print(user.get("name"))
print(user.get("is_married"))

# 4. keys() → Returns all keys
print(user.keys())

# 5. values() → Returns all keys
print(user.values())

# 6. items() → Returns key–value pairs as tuples
print(user.items())

# 7. pop(key) → Removes item with given key
user.pop("is_married")
print(user)

# 8. popitem() → Removes last inserted key–value pair
user.popitem()
print(user)

# 9. update(dict) → Updates dictionary with new key–value pairs
user.update({"city": "New York", "age": 26})
print(user)

# 10. setdefault(key, value) → Returns value if key exists, else inserts key
user.setdefault("age", 28)
print(user)

student = {"name": "Priya", "age": 22, "marks": 85}

if "is_married" in student:
    print("Key Exists")
else:
    print("Key does not Exists")


for key, value in student.items():
    print(key, ":", value)


marks = {"math": 90, "science": 95, "english": 88}

heighest=max(marks.values())
print(heighest)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: update()
dict1.update(dict2)
print(dict1)  
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Method 2: dictionary unpacking (Python 3.5+)
merged = {**dict1, **dict2}
print(merged)  
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
