import pandas as pd

# Creating a simple DataFrame
data = {
    "Name": ["Swati", "Anu", "Ravi"],
    "Age": [19, 20, 21],
    "Course": ["Data Science", "AI", "Computer Science"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
