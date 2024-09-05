
my_list = []

# Append 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position in the list
my_list.insert(1, 15)

# Extend [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element 
my_list.pop()

# Sort in ascending order
my_list.sort()

# print the index of the value 30 
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")
