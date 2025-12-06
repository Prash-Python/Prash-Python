# By default, the below will create a tuple if [] or () are not used. As below example,
a = 1,2,3,4,5
print(a, type(a))
# All other rules of tuples apply here as well, that is discussed in details for lists in exercise 5.
# Tuple Unpacking.
tup = (10,20,30,40,50,60)
a,b,c,d,e,f = tup
print("Unpacked values:", a,b,c,d,e,f)
tup1 = (100,200,300,400,500,600)
x, *y, z = tup1
print("Unpacked values with * operator:", x, y, z) 
a, b, *c, d, e = tup1
print("Unpacked values with * operator in middle:", a, b, c, d, e)
