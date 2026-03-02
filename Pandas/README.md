Pandas:
What is pandas, Why Pandas, Importatnt conecpts, Methods, 

Pandas: Oprn source python Library
Uses:
1. Data Manipulation - Data manipulation refers to the process of organizing, transforming, and restructuring raw data so that it becomes meaningful, usable, and ready for analysis
2. Data Analysis - Data analysis is the process of examining, cleaning, transforming, and modeling data to uncover useful information, draw conclusions, and support decision-making

Main Concepts:
1. Series - one-dimensional labeled array - one row [1, 2, 3, 4]
2. Data Frame - two(multi)-dimensional labeled data structure - row and column - [1, 2, 3]
                                                                          [4, 5, 6]

Aggregation:
Applying a function to reduce multiple values into a single summary value

Common Functions:

sum() → total of values

mean() → average

min() / max() → smallest / largest value

count() → number of entries

median() → middle value

std() → standard deviation

describe() → multiple summary stats at once

Reading Files:

rad_csv - To read a CSV file
pd.read_csv() is a Pandas I/O function. Its job is to read a CSV file and return a DataFrame object.

# print("1st 5: \n", df.head())
# print("1st 3: \n", df.head(3))
# print("Last 5: \n", df.tail())
# print("Last 3: \n", df.tail(3))
# print("Info: ", df.info()) - Summery of the csv file
# print("Summary: \n", df.describe()) - Statistic data of int values

openpyxl - to perform operation on excel file

File convert
1. csv to excel
2. csv to json
3. csv to csv
4. excel to csv
5. excel to json
6. excel to excel
7. json to csv
8. json to excel
9. json to json 

json to json :
orient values: 
1. records - Each row becomes a JSON object in a list.
    [
  {"id":1,"name":"Priya","age":25},
  {"id":2,"name":"Bala","age":28}
]

2. split - JSON contains separate keys for index, columns, and data.
    {
  "index":[0,1],
  "columns":["id","name","age"],
  "data":[[1,"Priya",25],[2,"Bala",28]]
}
3. index - Outer keys are row indices, values are row objects.
    {
  "0":{"id":1,"name":"Priya","age":25},
  "1":{"id":2,"name":"Bala","age":28}
}
4. columns - Outer keys are column names, values are index‑keyed objects.
    {
  "id":{"0":1,"1":2},
  "name":{"0":"Priya","1":"Bala"},
  "age":{"0":25,"1":28}
}

5. values - Just the raw data as a list of lists (no labels).
    [
  [1,"Priya",25],
  [2,"Bala",28]
]
6. table
    {
  "schema":{
    "fields":[
      {"name":"id","type":"integer"},
      {"name":"name","type":"string"},
      {"name":"age","type":"integer"}
    ],
    "primaryKey":["id"],
    "pandas_version":"1.4.0"
  },
  "data":[
    {"id":1,"name":"Priya","age":25},
    {"id":2,"name":"Bala","age":28}
  ]
}


Why Use loc and iloc?
Dot and box methods are fine for columns, but they don’t handle rows well.

loc → label-based indexing (uses row/column names).

iloc → position-based indexing (uses integer positions).

They are more explicit, powerful, and safer than chaining df["col"][row].



print(df_data.loc[0, 'name'])
#  Accesses the value in row with label/index 0 and column 'name' (label-based lookup).

print(df_data.iloc[0, 3])
#  Accesses the value in the first row (position 0) and the fourth column (position 3) (integer position-based lookup).

Use .isin() for exact matches (works for both strings and numbers).

Use .str methods for substring/pattern matching with strings.

Use .between() or comparison operators for range checks with numbers.

isin()

Expects a list‑like object (array, list, set, Series) of values to check against.

between()

Expects two scalar values: a lower bound and an upper bound.

DATA ANALYSIS:

