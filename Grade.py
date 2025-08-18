# Program to calculate grade from marks

# Take marks input from user
marks = float(input("Enter your marks (0-100): "))

# Check grade
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Print result
print("Your Grade is:", grade)
