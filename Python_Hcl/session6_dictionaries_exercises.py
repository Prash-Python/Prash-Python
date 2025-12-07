# """
# Question 1:
# input => String = "Coding"
# output => Dict = {"C":"CCC", "o":"ooo", "d":"ddd", "i":"iii", "n":"nnn", "g":"ggg"}
# """
text = "Coding"
my_dict = {ch:ch*3 for ch in text}
print(my_dict)

# """
# Question 2:
# Create a dictionary that has only those numbers as key whose cube is divisible by 4. 
# """
my_cube_dict = {x:x**3 for x in range(11) if (x ** 3) % 4 == 0}
print(my_cube_dict)

# """
# Question 3.a:
# Create a dictionary from 2 lists where lists represents the keys and values.
# """
keys_list = ["country", "capital"]
values_list = ["India", "Delhi"]
my_dict1 = {k:v for (k,v) in zip(keys_list, values_list)}
print(my_dict1)

# """
# Question 3.b:
# Create a dictionary and get 2 lists where lists represents the keys and values.
# """
my_dict2 = {x:x**2 for x in range(10) }
print(my_dict2)
my_key_list = []
my_values_list = []
for key, value in my_dict2.items():
    my_key_list.append(key)
    my_values_list.append(value)
print(my_key_list)
print(my_values_list)

# """
# Question 4: Ask user to enter a month using prompts and using dictionary return the number of days.
# """
def daysInMonth(month):
    month_to_num_days_dict = {"January":31, "February":28, "March":31, "April":30, "May":31,
                          "June":30, "July":31, "August":31, "September":30, "October":31,
                          "November":30, "December":31}
    days_returned = month_to_num_days_dict[month]
    print(days_returned)
prompt_month = input("Enter the month: ")
daysInMonth(prompt_month)

"""
Question 5: Print all the keys in dictionary in alphabetical order.
"""

def printAllKeysSorted():
    my_keys_list = []
    my_given_text = "python" + "java"
    my_created_dict = {x: x*3 for x in my_given_text}
    for key in my_created_dict.keys():
        my_keys_list.append(key)
    # my_keys_list = sorted(my_created_dict.keys())
    my_keys_list.sort()
    print(my_keys_list)
printAllKeysSorted()

"""
Question 6: Print all months with 31 days
"""
month_to_num_days_dict = {"January":31, "February":28, "March":31, "April":30, "May":31,
                          "June":30, "July":31, "August":31, "September":30, "October":31,
                          "November":30, "December":31}

def print_all_months_having_31_days():
    list_of_31_days_month = []
    count = 0
    for month_key in month_to_num_days_dict.keys():
        if month_to_num_days_dict[month_key] == 31:
            list_of_31_days_month.insert(count, month_key)
            count += 1
    print(list_of_31_days_month)
print_all_months_having_31_days()

