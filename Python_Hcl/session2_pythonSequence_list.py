# List Is a mutable sequence type in Python that allows you to store a collection of items.
my_list1 = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c', 'd', 'e']
print(my_list1[0])  # First element of list1
print(my_list2[2])  # Third element of list2
print(my_list1[1:4])  # Sublist from index 1 to 3 of list1
print(my_list2[0:3])  # Sublist from index 0 to 2 of list2
print(my_list1 + my_list2)  # Concatenation of lists
print(my_list1 * 2)  # Repeat list1 twice
print(len(my_list1))  # Length of list1
print(len(my_list2))  # Length of list2
my_list1.append(6)  # Append 6 to list1
print(my_list1)  # Print updated list1
my_list2.remove('d')  # Remove 'd' from list2
print(my_list2)  # Print updated list2
my_list2.insert(2, 'z')  # Insert 'z' at index 2 in list2
print(my_list2)  # Print updated list2
print(my_list1.index(4))  # Find the index of element 4 in list1
print(my_list2.count('a'))  # Count occurrences of 'a' in list2
my_list1.sort(reverse=True)  # Sort list1 in descending order
print(my_list1)  # Print sorted list1
my_list2.reverse()  # Reverse list2
print(my_list2)  # Print reversed list2
print(my_list1[::2])  # Slicing with step
print(my_list2[::-1])  # Reverse list2 using slicing
del my_list1[0]  # Delete first element of list1
print(my_list1)  # Print updated list1
del my_list2  # Delete list2 variable
print("List2 deleted.")
my_updated_list = [1,2,3,4,5,["a","b","c"], [10,20,30], ["p",200,"r"], 99.5]
print(my_updated_list[5])  # Accessing nested list ["a","b","c"]
print(my_updated_list[5][1])  # Accessing 'b' from nested list
# Lists are mutable, so we can change their elements.
my_updated_list[5][1] = "x"
my_updated_list[7][1] = 250
my_updated_list[len(my_updated_list)-1] = 100.5
print(my_updated_list)  # Print updated nested list
