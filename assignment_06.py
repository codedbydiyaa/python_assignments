# Assignment 6: Data Preprocessing using Pandas

import pandas as pd

# Step 1: Create a sample DataFrame
data = {
    "Name": ["Aman", "Diya", "Riya", "Aman", "Rahul"],
    "Marks": [85, None, 92, 85, None],
    "City": ["Indore", "Pune", None, "Indore", "Delhi"],
    "Remarks": ["Good", "Average", "Excellent", "Good", "Average"]
}

df = pd.DataFrame(data)

# Step 2: Display the original dataset
print("Original Dataset:")
print(df)

# Step 3: Explore the dataset
print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())

# Step 4: Remove duplicate records
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Step 5: Handle missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

print("\nAfter Handling Missing Values:")
print(df)

# Step 6: Remove an irrelevant column
df = df.drop(columns=["Remarks"])

# Step 7: Select and filter data using loc[]
print("\nStudents with Marks >= 80:")
print(df.loc[df["Marks"] >= 80])

# Step 8: Save the cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nPreprocessing completed successfully!")
print("Cleaned data saved to cleaned_students.csv")
