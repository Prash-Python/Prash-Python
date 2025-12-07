"""
Question 1:
input => String = "Coding"
output => Dict = {"C":"CCC", "o":"ooo", "d":"ddd", "i":"iii", "n":"nnn", "g":"ggg"}
"""
text = "Coding"
my_dict = {ch:ch*3 for ch in text}
print(my_dict)

"""
Question 2:
Create a dictionary that has only those numbers as key whose cube is divisible by 4. 
"""
my_cube_dict = {x:x**3 for x in range(11) if (x ** 3) % 4 == 0}
print(my_cube_dict)

"""
Question 3.a:
Create a dictionary from 2 lists where lists represents the keys and values.
"""
keys_list = ["country", "capital"]
values_list = ["India", "Delhi"]
my_dict1 = {k:v for (k,v) in zip(keys_list, values_list)}
print(my_dict1)

"""
Question 3.b:
Create a dictionary and get 2 lists where lists represents the keys and values.
"""
my_dict2 = {x:x**2 for x in range(10) }
print(my_dict2)
my_key_list = []
my_values_list = []
for key, value in my_dict2.items():
    my_key_list.append(key)
    my_values_list.append(value)
print(my_key_list)
print(my_values_list)