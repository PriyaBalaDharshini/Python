import pandas as pd

# CSV File
df_csv = pd.read_csv("employees.csv")
print(df_csv)
data = pd.DataFrame(df_csv)
print(data)

print("1st 5: \n", df_csv.head())
print("1st 3: \n", df_csv.head(3))
print("Last 5: \n", df_csv.tail())
print("Last 3: \n", df_csv.tail(3))
print("Info: ", df_csv.info())
print("Summary: \n", df_csv.describe())

# Excel File

df_excel = pd.read_excel("employees.xlsx", sheet_name="Employees")
print("Excel Values: \n", df_excel)

print("1st 5: \n", df_excel.head())
print("Last 5: \n", df_excel.tail())
print("Info: ", df_excel.info())
print("Summary: \n", df_excel.describe())


# JSON File

df_json = pd.read_json("employees.json")
print("JSON Values: \n", df_json)

print("1st 5: \n", df_json.head())
print("Last 5: \n", df_json.tail())
print("Info: ", df_json.info())
print("Summary: \n", df_json.describe())


# New file creation
df_csv = pd.read_csv("employees.csv")
new_csv = df_csv.tail(6)
new_csv.to_csv("last_six.csv", index=False)
print(new_csv)

df_excel = pd.read_excel("employees.xlsx", sheet_name="Employees")
new_excel = df_excel.tail(4)
new_excel.to_excel("last_four.xlsx", sheet_name="new")

new_excel1 = df_excel.tail(2)
new_excel1.to_excel("last_two.xlsx")


df_json = pd.read_json("employees.json")
new_json = df_json.head()
new_json.to_json("out.json")
new_json.to_json("out1.json", orient="records")
new_json.to_json("out2.json", orient="split")
