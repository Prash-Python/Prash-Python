class Calculator:
    def add(self, a = 8, b = 9, c = 10):
        return (a + b + c)
c1 = Calculator()
print(c1.add())
print(c1.add(10))
print(c1.add(20, 20))
print(c1.add(30, 30, 30))
