# Program to check whether a triangle is right-angled using a function

# Function to check right-angled triangle
def is_right_angled(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0] > 0 and sides[0] + sides[1] > sides[2]:
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return True

    return False

side1 = float(input("Enter the length of first side: "))
side2 = float(input("Enter the length of second side: "))
side3 = float(input("Enter the length of third side: "))

# Function calling
if is_right_angled(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
