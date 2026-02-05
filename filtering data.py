import pandas as pd

df = pd.read_csv("students.csv")

# Students with marks above 80
high_scorers = df[df["Marks"] > 80]

print("High Scorers:")
print(high_scorers)
