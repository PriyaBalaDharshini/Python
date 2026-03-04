import pandas as pd

# sales_data = {
#     "waiter": ["John", "Mary", "John", "Bob", "Mary"],
#     "total": [120, 120, 80, 250, 50],
# }

# sales = pd.DataFrame(sales_data)

# # result=sales.groupby('waiter')['total'].sum()
# # print(result)


# data = {
#     "product": ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse"],
#     "sales": [1200, 25, 1100, 75, 30],
#     "region": ["East", "East", "West", "West", "East"],
# }
# data_df = pd.DataFrame(data)
# print(data_df)

# result = data_df.groupby("product")["sales"].sum()
# print(result)

# result1 = data_df.groupby("region")["product"].count()
# print(result1)

# agg = data_df.groupby('product').agg({'sales':['sum', 'count', 'mean', 'median']})
# print(agg)


# students = pd.DataFrame({
#    'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
#    'subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
#    'score': [95, 78, 88, 92, 85, 90]
# })

# stu_df = pd.DataFrame(students)

# result = stu_df.groupby("name")["score"].sum()
# result = stu_df.groupby("name")["score"].mean()
# result = stu_df.groupby('name')["subject"].count()

# print(result)


sales_data = pd.DataFrame({
   'region': ['East', 'East', 'West', 'West', 'East', 'West']*2,
   'category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture']*2,
   'sales': [5000, 3000, 4500, 2800, 5200, 3100]*2
})

df=pd.DataFrame(sales_data)
result = df.groupby(['region', 'category'])['sales'].sum().reset_index()
#print(result)


pivot = sales_data.pivot_table(
   values='sales',      # What to calculate
   index='category',      # Rows
   columns='region',  # Columns
   aggfunc='count'        # How to aggregate
)
#print(pivot)


students = pd.DataFrame({
   'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
   'subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
   'score': [95, 78, 88, 92, 85, 90]
})

def score_range(series):
   return series.max() - series.min() 

result = students.groupby('name')['score'].agg(score_range)
# print(result)

def score(x):
   return x.max()-x.min()

def above_90(x):
   return (x>=90).sum()

res = students.groupby('name')['score'].agg(['mean', score_range, above_90])
print(res)


sales = pd.DataFrame({
   'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03'],
   'salesperson': ['John', 'Mary', 'John', 'Mary', 'John'],
   'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor'],
   'amount': [1200, 25, 75, 1150, 300]
})

who_sold_most = sales.groupby('salesperson')['amount'].sum().sort_values(ascending=False)
print(who_sold_most)

average  = sales.groupby('salesperson')['amount'].mean()
print(average)

# E-commerce transactions
orders = pd.DataFrame({
   'order_id': range(1, 13),
   'category': ['Electronics', 'Clothing', 'Electronics', 'Home'] * 3,
   'region': ['North', 'North', 'South', 'South'] * 3,
   'revenue': [1200, 300, 1500, 450, 1100, 280, 1600, 500, 1300, 320, 1400, 480],
   'quantity': [2, 5, 3, 2, 2, 6, 3, 2, 2, 4, 3, 2]
})

# Calculate average price per item
def ave_price(group):
   return group['revenue'].sum()/ group['quantity'].sum()


# Best performing category
best_category = orders.groupby('category')['revenue'].sum().idxmax()
print(f"\nTop Category: {best_category}")
   