#  Creating empty list
my_list = []

# Appending elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"List after appending: {my_list}")

# Inserting the values 
my_list.insert(1, 15)
print(f"List after inserting 15: {my_list}")

# Extending list with another list
my_list.extend([50, 60, 70])
print(f"List after extending: {my_list}")

# Removing the last element
my_list.pop()
print(f"List after removing the last element: {my_list}")

# Sorting list in ascending order
my_list.sort()
print(f"List after sorting: {my_list}")

# Finding and printing the index of 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")