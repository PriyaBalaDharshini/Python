import pandas as pd

scores = pd.DataFrame({"id": [1, 2, 3, 4, 5], "scores": [87, 54, 76, 55, 90]})

names = pd.DataFrame(
    {"id": [1, 2, 3, 4, 6], "names": ["Priya", "Bala", "Nandhu", "Suman", "Surya"]}
)

# Left join
left = pd.merge(scores, names, on="id", how="left")
print("Left join table: \n", left)

# Right join
right = pd.merge(scores, names, on="id", how="right")
print("Right join table: \n", right)

# inner join
inner = pd.merge(scores, names, on="id", how="inner")
print("Inner join table: \n", inner)

# outer join
outer = pd.merge(scores, names, on="id", how="outer")
print("Outer join table: \n", outer)
