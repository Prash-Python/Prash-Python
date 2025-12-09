class Grandparent():
    def ask(Self):
        print("Ask to grandparent")

class Parent(Grandparent):
    def ask(self):
        print("Ask to parent")
        super().ask()

class Child(Parent):
    def ask(self):
        super().ask()
        print("Ask to child")
c1 = Child()
c1.ask()
