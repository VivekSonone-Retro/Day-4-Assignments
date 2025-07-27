# Create two lists with same values
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Equality check
print("list1 == list2:", list1 == list2)  # True: same values

# Identity check
print("list1 is list2:", list1 is list2)  # False: different objects in memory

# Show they are different objects
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
