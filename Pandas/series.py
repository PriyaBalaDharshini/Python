import pandas as pd

# Series - 1D array
# List
data = [10, 20, 30, 40, 50, 60, 70, 80]
print("Normal: ", data)

pd_data = pd.Series(data)
print("Pandas Series:")
print(pd_data)
# Data access
print("index: ", pd_data[0])

# Slicing
print("Slicing: ", pd_data[::])

print("Data * 5: ", pd_data * 5)
print("Data + 27: ", pd_data + 27)
print("Data - 3: ", pd_data - 3)
print("Data / 7: ", pd_data / 7)
print("Data // 3: ", pd_data // 3)


pd_data = pd.Series(data, index=("a", "b", "c", "d"))
print("Pandas Series with defined index:")
print(pd_data)
# Data access
print("index: ", pd_data["c"])


# Dict - key value pair
dict_data = {"a": 10, "b": 20, "c": 30, "d": 40}
print("Normal Dict: ", dict_data)

pd_dict = pd.Series(dict_data)
print("Pandas Dict: ", pd_dict)


data_sum = pd.Series(sum(data))
data_sum1 = pd.Series(data)
print(data_sum)
print("Sum: ", data_sum1.sum())  # Sum
print("Average: ", data_sum1.mean())  # Average
print("Min: ", data_sum1.min())  # Min
print("Max: ", data_sum1.max())  # Max

# Filter
result = data_sum1[data_sum1 >= 30]
print("Filtered: ", result)
