# Take input from the user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Swap without a third variable using arithmetic
a = a + b
b = a - b
a = a - b

# Display the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
