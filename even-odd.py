# Program to check if a number is even/odd and positive/negative

# Take input from user
num = int(input("Enter a number: "))

# Check positive, negative or zero
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

# Check even or odd
if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

# Display result
print(f"The number {num} is {sign} and {parity}.")
