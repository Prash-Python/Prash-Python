# Convert given string to all upper case.
s1 = "Python Programming"
s2 = lambda func : func.upper()
print(s2(s1))

# Check if a number is positive, zero or negative.
n = lambda x : "Postive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(0))
print(n(-4))
print(n(5))

# Multiply each number in a list by 10.
p1 = [lambda arg = x : arg * 10 for x in range(10,17)]
for i in p1:
    print(i())

# Perform addition and multiplication in single line with tuple.
arithmetic = lambda x,y : (x*y, x+y)
print(arithmetic(5,10), type(arithmetic)) # Type here will give as function and not tuple.Since result is not saved as tuple.

# Perform addition and multiplication in single line with list.
arithmetic = lambda x,y : [x*y, x+y]
print(arithmetic(5,10), type(arithmetic)) # Type here will give as function and not list. Since result is not saved as list.