class Parent(object):
    def implicit(self):
        print("PARENT")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()