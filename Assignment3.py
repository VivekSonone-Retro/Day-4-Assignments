# Input age and country from the user
age = int(input("Enter your age: "))
country = input("Enter your country: ")

# Use logical operators to check eligibility
if age > 18 and country.lower() == "india":
    print("You are eligible.")
else:
    print("You are not eligible.")
