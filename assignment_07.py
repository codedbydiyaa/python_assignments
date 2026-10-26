import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Student": ["Amit", "Bhavna", "Chetan", "Diya", "Esha", "Farhan"],
    "Maths": [75, 82, 68, 90, 72, 85],
    "Python": [80, 78, 70, 92, 75, 88],
    "Attendance": [85, 90, 78, 95, 80, 92],
    "City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

plt.scatter(df["Maths"], df["Python"])
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.show()

correlation = df[["Maths", "Python", "Attendance"]].corr()
print("Correlation Matrix:")
print(correlation)

sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
