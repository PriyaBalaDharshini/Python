import pandas as pd

df = pd.DataFrame(
    {"A": [1, 2, None, 4, None], "B": ["Apple", None, "Cat", None, "Dog"]}
)

# Check for null
print(df.isnull())

# Fill null with a value
df_fill = df.fillna({"A": 0, "B": "random"})
print(df_fill)

# remove null values
print(df.dropna())

data = {
    "name": ["Priya", "Bala priya", "Thiru", "Bala priya", "Dhivya"],
    "email": [
        "priya@example.com",
        "bala@example.com",
        "thiru@example.com",
        "bala@example.com",
        "dhivya@example.com",
    ],
    "age": [20, 22, 24, 26, 28],
}

data_df = pd.DataFrame(data)
# print(data_df)

# Check for Duplicate
# print(data_df.duplicated())
# Drop Duplicate
# print(data_df.drop_duplicates()) # will not affect the original data
# print(data_df)

# Rename column
# rename_column = data_df.rename(columns={"name":"new_name"})
# print(rename_column)
# print(data_df)
# data_df['name']=data_df['name'].str.lower()
# data_df['name']=data_df['name'].str.upper()
# data_df['name']=data_df['name'].str.capitalize()
# data_df['name']=data_df['name'].str.swapcase()
# data_df['name']=data_df['name'].str.title()
# print(data_df)

# Replace value
# data_df["name"] = data_df["name"].str.replace("Bala priya", "Priya Bala")
# print(data_df)


# sorting




data_df = pd.DataFrame(data, index=["c", "g", "w", "l", "z"])
# sorted_data = data_df.sort_values(by="name")
# print(sorted_data)

sorted_data = data_df.sort_index()
print(sorted_data)

marks = pd.DataFrame({"scores":[98, 32, 67, 49, 88]})
rank = marks["scores"].rank()
print(rank)

#grouping
group_data ={
    "Department":["HR", "Finance", "HR", "Development", "IT", "IT"],
    "Salary":[20000, 30000, 10000, 22000, 45000, 22000]
}
group_df= pd.DataFrame(group_data)
# gr_result=group_df.groupby("Department")["Salary"].sum()
# print(gr_result)


#Aggregation
gr_result1=group_df.groupby("Department")["Salary"].agg(["mean", "max", "min",  "count"])
print(gr_result1)
