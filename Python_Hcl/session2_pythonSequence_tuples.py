# Creating a tuple in Python which is an immutable sequence type.
my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = ('a', 'b', 'c', 'd', 'e')
print(my_tuple1[0])  # First element of tuple1
print(my_tuple2[2])  # Third element of tuple2
print(my_tuple1[1:4])  # Subtuple from index 1 to 3 of tuple1
print(my_tuple2[0:3])  # Subtuple from index 0 to 2 of tuple2
print(my_tuple1 + my_tuple2)  # Concatenation of tuples
print(my_tuple1 * 2)  # Repeat tuple1 twice
print(len(my_tuple1))  # Length of tuple1
print(len(my_tuple2))  # Length of tuple2
print(my_tuple1.index(4))  # Find the index of element 4 in tuple
print(my_tuple2.count('a'))  # Count occurrences of 'a' in tuple2
print(my_tuple1[::2])  # Slicing with step 2
print(my_tuple2[::-1])  # Reverse tuple2 using slicing
my_tuple3 = (10, 20, 30, (40, 50, 60), ('x', 'y', 'z'), 70.5, [100, 200, 300])
print(my_tuple3[3])  # Accessing nested tuple (40, 50, 60)
print(my_tuple3[3][1])  # Accessing '50' from nested tuple
print(my_tuple3[4][2])  # Accessing 'z' from nested tuple
print(my_tuple3[6][0])  # Accessing '100' from nested list
my_tuple3[6][1] = 250  # Modifying element in nested list
print(my_tuple3)  # Print updated tuple with modified nested list