class Parent(object):
    def override(self):
        print("PARENT")

class Child(Parent):
    def override(self):
        print("CHILD")

dad = Parent()
son = Child()

dad.override()
son.override()