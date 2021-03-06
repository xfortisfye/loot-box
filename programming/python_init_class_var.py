print("##### example 1 #####")
print("https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables")

class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs
e.kind                  # shared by all dogs
d.name                  # unique to d
e.name                  # unique to e


print("##### example 2 #####")

class Foo:
    static_var = 'every instance has access'

    def __init__(self, name):
        self.static_var = 'self instance value'
        self.instance_var = 'I am %s' % name

    def getValue(self):
        return self.static_var

    def toString(self):
        print("self.instance_var = " + self.instance_var)
        print("Class Static Variable | Foo.static_var = " + Foo.static_var)
        print("Class Instance Variable | self.static_var = " + self.static_var)
        print("Class Instance Variable | self.getValue() = " + self.getValue())

obj1 = Foo('obj1')
obj2 = Foo('obj2')

print("\nOriginal...\n")
obj1.toString()
obj2.toString()

print("\nModifying class initialised variable... | obj1.static_var = \"Shadowing static_var\"\n")
obj1.static_var = "Shadowing static_var"
obj1.toString()
obj2.toString()

print("\nModifying class static variable... | Foo.static_var = \"modified class\"\n")
Foo.static_var = "modified class"
obj1.toString()
obj2.toString()
