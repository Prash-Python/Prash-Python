"""
Sets are unordered collections of unique elements in Python.
Sets are immutable.
They do not allow duplicate values.
"""
set1 = set()
set2 = {1, 2, 3, 4, 5}
set3 = set([1, 2, 3, 4, 5])
set4 = set("hello")
set5 = set((1, 2, 3, 4, 5))
print("Empty set:", set1)
print("Set with integers:", set2)
print("Set created from list:", set3)
print("Set created from string:", set4)
print("Set created from tuple:", set5)
# Adding elements to a set
set1.add(10)
set1.add(20)
set1.add(30)
set1.add(40)
set1.add(20)  # Duplicate element, will not be added
print("Set after adding elements:", set1)
# Removing elements from a set
set1.remove(40)
print("Set after removing an element:", set1)
set1.discard(50)  # Element not present, no error
print("Set after discarding a non-existing element:", set1)
popped_element = set1.pop()
print("Popped element:", popped_element)
print("Set after popping an element:", set1)
# Set operations
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
union_set = setA.union(setB)
intersection_set = setA.intersection(setB)
difference_set = setA.difference(setB)
symmetric_difference_set = setA.symmetric_difference(setB)
print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets:", difference_set)
print("Symmetric difference of sets:", symmetric_difference_set)
# Set comprehensions
squared_set = {x ** 2 for x in range(1, 11)}
print("Set of squares:", squared_set)
even_set = {x for x in range(1, 21) if x % 2 == 0}
print("Set of even numbers from 1 to 20:", even_set)
prime_set = {x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
print("Set of prime numbers from 2 to 50:", prime_set)
# Frozen set example
frozen_set_example = frozenset([1, 2, 3, 4, 5])
print("Frozen set example:", frozen_set_example)
# Attempting to add an element to a frozen set will raise an error
try:
    frozen_set_example.add(6)
except AttributeError as e:
    print("Error:", e)
# Set membership testing
print("Is 3 in setA?", 3 in setA)
print("Is 10 in setB?", 10 in setB)
# Set length
print("Length of setA:", len(setA))
print("Length of setB:", len(setB))
# Iterating through a set
print("Elements in setA:")
for element in setA:
    print(element)
# Clearing a set
setA.clear()
print("SetA after clearing:", setA)
# Example of nested sets using frozenset
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print("Nested set using frozenset:", nested_set)
# Set comparison
setC = {1, 2, 3}
setD = {1, 2, 3, 4, 5}
print("Is setC a subset of setD?", setC.issubset(setD))
print("Is setD a superset of setC?", setD.issuperset(setC))
# Copying a set
original_set = {1, 2, 3, 4, 5}
copied_set = original_set.copy()
print("Copied set:", copied_set)
print("Original set and copied set are the same object?", original_set is copied_set)
# Example of set intersection update
setE = {1, 2, 3, 4, 5}
setF = {4, 5, 6, 7, 8}
setE.intersection_update(setF)
print("SetE after intersection update with setF:", setE)
# Example of set union update
setG = {1, 2, 3}
setH = {4, 5, 6}
setG.update(setH)
print("SetG after union update with setH:", setG)
# Example of set difference update
setI = {1, 2, 3, 4, 5}
setJ = {4, 5, 6, 7, 8}
setI.difference_update(setJ)
print("SetI after difference update with setJ:", setI)
# Example of set symmetric difference update
setK = {1, 2, 3, 4, 5}  
setL = {4, 5, 6, 7, 8}
setK.symmetric_difference_update(setL)
print("SetK after symmetric difference update with setL:", setK)
# Example of checking if two sets are disjoint
setM = {1, 2, 3}
setN = {4, 5, 6}
print("Are setM and setN disjoint?", setM.isdisjoint(setN))
# Example of frozenset operations
frozen_set1 = frozenset([1, 2, 3])
frozen_set2 = frozenset([3, 4, 5])
frozen_union = frozen_set1.union(frozen_set2)
print("Union of frozen sets:", frozen_union)
frozen_intersection = frozen_set1.intersection(frozen_set2)
print("Intersection of frozen sets:", frozen_intersection)
# Example of set difference with frozensets
frozen_difference = frozen_set1.difference(frozen_set2)
print("Difference of frozen sets:", frozen_difference)
# Example of set comprehension to create a set of squares of even numbers from 1 to 10
squares_of_even = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print("Squares of even numbers from 1 to 10:", squares_of_even)  # Output: {4, 16, 36, 64, 100}
# Example of set comprehension to create a set of squares of odd numbers from 1 to 10
squares_of_odd = {x ** 2 for x in range(1, 11) if x % 2 != 0}
print("Squares of odd numbers from 1 to 10:", squares_of_odd)  # Output: {1, 9, 25, 49, 81}
# Example to read nested set using set comprehension
nested_set_example = {frozenset({1, 2}), frozenset({3, 4, frozenset({5, 6})})}
print("Nested set example:", nested_set_example)
for subset in nested_set_example:
    print("Subset:", subset)
    for item in subset:
        print("Item in subset:", item)
# Example to create a set of tuples using set comprehension
tuples_set = {(x, x ** 2) for x in range(1, 6)}
print("Set of tuples (number, square):", tuples_set)  # Output: {(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)}
