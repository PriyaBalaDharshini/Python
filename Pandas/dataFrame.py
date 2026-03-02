import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Priya", "Bala", "Thiru", "Surya", "Dhivya"],
    "emai": [
        "priya@example.com",
        "bala@example.com",
        "thiru@example.com",
        "surya@example.com",
        "dhivya@example.com",
    ],
    "age": [20, 22, 24, 26, 28],
}

print(data)


df_data = pd.DataFrame(data)
print("DF Data: \n", df_data)

data_list = [
    {"id": 1, "name": "Priya", "email": "priya@example.com", "age": 20},
    {"id": 2, "name": "Bala", "email": "bala@example.com", "age": 22},
    {"id": 3, "name": "Thiru", "email": "thiru@example.com", "age": 24},
    {"id": 4, "name": "Surya", "email": "surya@example.com", "age": 26},
    {"id": 5, "name": "Dhivya", "email": "dhivya@example.com", "age": 28},
    {"id": 6, "name": "Kiran", "email": "kiran@example.com", "age": 23},
    {"id": 7, "name": "Anjali", "email": "anjali@example.com", "age": 25},
    {"id": 8, "name": "Ravi", "email": "ravi@example.com", "age": 27},
    {"id": 9, "name": "Sneha", "email": "sneha@example.com", "age": 29},
    {"id": 10, "name": "Vikram", "email": "vikram@example.com", "age": 30},
]
data_list_df = pd.DataFrame(data_list)
print(data_list_df)
