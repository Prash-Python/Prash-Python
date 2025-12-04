a = 10 # integer assignment where a goes into stack memory and 10 goes into heap memory.
b = 20 # integer assignment where b goes into stack memory and 20 goes into heap memory.
c = a + b # addition operation where c goes into stack memory and the result (30) goes into heap memory.
print("The sum of a and b is:", c)
print(type(c))
print(type(a))
print(type(b))
print(id(a))
print(id(b))
print(id(c))
a = 10.5
print(type(a))
print(id(a))
c = a + b
print("The new sum of a and b is:", c)
print(type(c))
print(id(c))
# Stack memory is used for identifiers, local variables and function calls.
# Heap memory is used for storing objects and data structures like integers, floats, lists, dictionaries, etc.
# In Python, memory management is handled by the Python Memory Manager, which allocates and deallocates memory as needed.
# Python uses a combination of stack and heap memory to manage data efficiently.