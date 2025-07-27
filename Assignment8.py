# Take age and citizenship status from user
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

# Check eligibility
if age >= 18 and citizen == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
