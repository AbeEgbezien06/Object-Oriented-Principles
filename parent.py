# ENCAPSULATION
# This is process of providing restrictions on data, encapsulated data provides a certain level of privacy/security.
#
# There are two levels of encapsulation protected and private
# Protected
# Protected
class Parent:
    def __init__(self):
        self._n = 2

# Child class
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Members of Parent class: ")
        print(self._n)

obj1 = Child()

obj2 = Parent()

print(obj2._n)



# Private

# Private
class Parent:
    def __init__(self):
        self.a = "Variable A"
        self.__b = "Variable B"

# Child class
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Members of Parent class: ")
        print(self.a)
        print(self.__b)  # This line will cause an error

# child = Child()
obj1 = Parent()
print(obj1.a)

# Printing B throws an error
print(obj1.__b)  # This line will cause an error
