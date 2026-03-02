# 📘 Pandas Notes

## What is Pandas, Why Pandas, Important Concepts, Methods

### Pandas
Open source Python Library

### Uses
1. **Data Manipulation**  
   Organizing, transforming, and restructuring raw data so that it becomes meaningful, usable, and ready for analysis.  
2. **Data Analysis**  
   Examining, cleaning, transforming, and modeling data to uncover useful information, draw conclusions, and support decision-making.

---

## Main Concepts
1. **Series** – one-dimensional labeled array  
   Example: `[1, 2, 3, 4]`  
2. **DataFrame** – two (multi)-dimensional labeled data structure (rows and columns)  
   Example:  `[1, 2, 3] [4, 5, 6]`

---

## Aggregation
Applying a function to reduce multiple values into a single summary value.

### Common Functions
- `sum()` → total of values  
- `mean()` → average  
- `min()` / `max()` → smallest / largest value  
- `count()` → number of entries  
- `median()` → middle value  
- `std()` → standard deviation  
- `describe()` → multiple summary stats at once  

---

## Reading Files
- **`pd.read_csv()`** → To read a CSV file and return a DataFrame object.  
- **openpyxl** → to perform operations on Excel files  

Examples of reading:
- `df.head()` → first 5 rows  
- `df.head(3)` → first 3 rows  
- `df.tail()` → last 5 rows  
- `df.tail(3)` → last 3 rows  
- `df.info()` → summary of the file  
- `df.describe()` → statistical summary of numeric values  

---

## File Convert
- csv to excel  
- csv to json  
- csv to csv  
- excel to csv  
- excel to json  
- excel to excel  
- json to csv  
- json to excel  
- json to json  

---

## JSON to JSON Orient Values
- **records** – Each row becomes a JSON object in a list.  
- **split** – JSON contains separate keys for index, columns, and data.  
- **index** – Outer keys are row indices, values are row objects.  
- **columns** – Outer keys are column names, values are index‑keyed objects.  
- **values** – Just the raw data as a list of lists (no labels).  
- **table** – JSON Table Schema with schema + data.  

---

## Why Use loc and iloc?
- Dot and box methods are fine for columns, but they don’t handle rows well.  
- **loc** → label-based indexing (uses row/column names).  
- **iloc** → position-based indexing (uses integer positions).  
- They are more explicit, powerful, and safer than chaining `df["col"][row]`.

### Examples
- `df_data.loc[0, 'name']` → Accesses the value in row with label/index 0 and column 'name'.  
- `df_data.iloc[0, 3]` → Accesses the value in the first row (position 0) and the fourth column (position 3).  

---

## Selection Methods
- Use `.isin()` for exact matches (works for both strings and numbers).  
- Use `.str` methods for substring/pattern matching with strings.  
- Use `.between()` or comparison operators for range checks with numbers.  

### `isin()`
Expects a list‑like object (array, list, set, Series) of values to check against.  

### `between()`
Expects two scalar values: a lower bound and an upper bound.  

---

## Data Analysis
- **Check for null values** → `isnull()`  
- **Fill null values** → `fillna()`  
- **Remove null values** → `dropna()`  
- **Check for duplicates** → `duplicated()`  
- **Drop duplicates** → `drop_duplicates()` (does not affect original unless `inplace=True`)  
- **Rename columns** → `rename()`  
- **String operations** → `lower()`, `upper()`, `capitalize()`, `swapcase()`, `title()`  
- **Replace values** → `str.replace()`  
- **Sorting** → `sort_values()`, `sort_index()`  
- **Ranking** → `rank()`  
- **Grouping** → `groupby()`  
- **Aggregation** → `agg()` with functions like `mean`, `max`, `min`, `count`  

---
