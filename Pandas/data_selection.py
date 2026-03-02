import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Priya", "Bala Priya", "Thiru", "Bala Priya", "Dhivya"],
    "email": [
        "priya@example.com",
        "bala@example.com",
        "thiru@example.com",
        "surya@example.com",
        "dhivya@example.com",
    ],
    "age": [20, 22, 24, 26, 28],
}

# df_data = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])
# print(df_data.loc['e'])
df_data = pd.DataFrame(data)
# print(df_data.loc[0])
# print(df_data["name"][1])
# print(df_data['name'])
# print(df_data.age)

# print(df_data.loc[0, 'age'])
# print(df_data.loc[0, 'name'])

# print(df_data.iloc[0, 3])

# Conditionals filering
# print(df_data[df_data["age"]>=25])  #Dtailed data
# print(df_data["age"]>=25) #True or false

# # is in
# print(df_data[df_data["name"].isin(["Bala Priya"])])
# print(df_data[df_data["name"].str.contains("Priya")])

# # between
# print(df_data[df_data['age'].between(22, 26)])

# Query
print(df_data.query("id>=3"))
