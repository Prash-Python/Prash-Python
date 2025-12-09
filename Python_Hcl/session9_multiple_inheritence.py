class Father:
    def skills(self):
        print("Skills A")

class Mother:
    def skills(self):
        print("Skills B")

class Child(Father, Mother):
    # Method Resolution Order => MRO
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Skills C")

c1 = Child()
c1.skills()