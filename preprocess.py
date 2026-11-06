import pandas as pd

# Read the dataset
data = pd.read_csv("students.csv")

# Show original data
print("Original Dataset")
print(data.head())

# Convert Communication column into numbers
data["Communication"] = data["Communication"].map({
    "Poor": 0,
    "Average": 1,
    "Good": 2,
    "Excellent": 3
})

# Convert Placed column into numbers
data["Placed"] = data["Placed"].map({
    "No": 0,
    "Yes": 1
})

print("\nDataset After Encoding")
print(data)