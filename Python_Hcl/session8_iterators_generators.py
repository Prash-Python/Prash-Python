# Calculate power of two for the given exponential.
def power_two_generator(max=0):
    n = 1
    while n <= max:
        yield 2 ** n
        n += 1
a = power_two_generator(6)
for i in a:
    print(i)