# Create a list of favorite colors
favorite_colors = ["blue", "green", "red", "purple", "yellow"]

# Ask the user to input a color
user_color = input("Guess a favorite color: ").lower()

# Check membership
if user_color in favorite_colors:
    print("Yes! That's one of the favorite colors.")
else:
    print("Nope, that's not on the list.")
