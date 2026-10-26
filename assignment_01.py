# LIST OPERATIONS
students_list = ["Aarav", "Diya", "Riya", "Karan"]

print(" LIST OPERATIONS ")
print("Original List:", students_list)

# Add
students_list.append("Neha")
print("After Add:", students_list)

# Update
students_list[1] = "Diya Jolly"
print("After Update:", students_list)

# Delete
students_list.remove("Karan")
print("After Delete:", students_list)

# TUPLE OPERATIONS
students_tuple = ("Aarav", "Diya", "Riya", "Karan")

print("TUPLE OPERATIONS")
print("Original Tuple:", students_tuple)

# Count - counts how many times an element occurs
print("Count of Diya:", students_tuple.count("Diya"))

# Index - returns the first index of an element
print("Index of Riya:", students_tuple.index("Riya"))


# DICTIONARY OPERATIONS
students_dict = {
    101: "Aarav",
    102: "Diya",
    103: "Riya",
    104: "Karan"
}

print("DICTIONARY OPERATIONS")
print("Original Dictionary:", students_dict)

# Add
students_dict[105] = "Neha"
print("After Add:", students_dict)

# Update
students_dict[102] = "Diya Jolly"
print("After Update:", students_dict)

# Delete
del students_dict[104]
print("After Delete:", students_dict)

# SOME IMPORTANT METHODS
print("IMPORTANT METHODS ")

# List methods
print("List Length:", len(students_list))
print("List Count of Diya Jolly:", students_list.count("Diya Jolly"))

# Tuple methods
print("Tuple Length:", len(students_tuple))
print("Tuple Count of Diya Jolly:", students_tuple.count("Diya Jolly"))

# Dictionary methods
print("Dictionary Keys:", students_dict.keys())
print("Dictionary Values:", students_dict.values())
print("Dictionary Items:", students_dict.items())
