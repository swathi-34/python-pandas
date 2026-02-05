import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

print("Student Data:")
print(df)

# Checking missing values
print("\nMissing values:")
print(df.isnull())

# Filling missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter filling missing values:")
print(df)

# Basic analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
