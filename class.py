class Shoes:

    def __init__(self,brand , owner, size):
        self.brand = brand
        self.owner = owner
        self.size = size


    def show(self):
        print("Brand:",self.brand,"Name", self. owner, "size ", self.size )

sandals = Shoes("Adidas", "Anita", 42 )
sandals.show( )

class Physics:
    gravity = 9.8

    def potentialenergy(self, mass, height):
        return mass * self.gravity * height


# ObjectName = ClassName()
phys = Physics()  # Creating a phyics object
print(phys.potentialenergy(10, 10))