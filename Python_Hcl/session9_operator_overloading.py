class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
P1 = Point(10,20)
P2 = Point(5,6)
P3 = P1 + P2
print(P3.x, P3.y)

# Exercise 1:
class NAME:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return (self.name + " " + other.name)
N1 = NAME("Rakhee")
N2 = NAME("Chibber")
N3 = N1 + N2
print(N3)

# Exercise 2: Remove all vowels from name in Exercise 1 above.
class NAME:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return (self.name + " " + other.name)
    def __sub__(self, other):
        str = ""
        vowels = "aeiouAEIOU"
        for i in self.name:
            if i not in vowels:
                str += i
        for j in other.name:
            if j not in vowels:
                str += j
        return str
N1 = NAME("Rakhee")
N2 = NAME("Chibber")
N3 = N1 + N2
print(N3)
N4 = N1 - N2
print(N4)



