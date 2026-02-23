# file=open("file.txt", "w")
# file.close()

# file=open("file1.txt", "w")
# file.write("Sample file content")
# file.close()

# file=open("file1.txt", 'r')
# content=file.read()
# print(content) # print(file.read())
# file.close()

# file=open("shopping.txt", "w")
# file.write("Apple\nBall\nVeggies")
# file.close()

# file=open("shopping.txt", "r")
# for item in file:
#     print(item.strip())
# file.close()

# file=open("shopping.txt", "a+")
# file.write("\nEggs\nMilk\nCurryleaves")
# content1=file.read()
# print(content1)
# file.close()

# with open("shopping.txt", "r") as file:
#     content=file.read()
#     print(f"content with condition with \n{content}")
    
    
# with open("shopping.txt", "w+") as file:
#     file.write("Content using with")
    
#Python Dictionary:
# import json
# person ={
#     "name":"Priya",
#     "age":30,
#     "is_married":True,
#     "address":{
#         "city":"Hosur",
#         "state":"Tamilnadu"
#     },
#     "skills":["Python, JS"]
# }

# print(person)

# #dict to json
# json_string=json.dumps(person, indent=2)
# print(json_string)

# #json to dict
# json_string1 = '{"name":"Priya", "age":30, "active":true}'
# person1=json.loads(json_string1)
# print(person1)

# import json
# data = {"name": "Priya", "age": 25, "married":True}
# file =open("data.json", "w")
# json.dump(data, file)

# string_file=json.dumps(data)
# print(string_file)

# data1='{"name": "Priya", "age": 25, "married": true}'
# # file=open("data.json", "r")
# # data1=json.load(file)
# # print(data)

# data2 = json.loads(data1)
# print(f"data2: {data2}")


import json
    
with open("res.json","r" ) as f:
    data=json.load(f)
    
    print(type(data))