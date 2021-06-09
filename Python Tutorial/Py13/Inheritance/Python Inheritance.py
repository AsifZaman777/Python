# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Dhaka: # Parent class
    def __init__(self,age,volume,area):
        self.age=age
        self.volume=volume
        self.area=area

    def excecute(self):  #overrided in Chattogram
        print("Age of Dhaka : "+self.age)
        print("Volume of Dhaka : "+self.volume)
        print("Area of Dhaka : "+self.area)

object_Dhaka=Dhaka("200 year","34567 km","345km")
object_Dhaka.excecute()

class Chattogram(Dhaka):  # Subclass of Dhaka
    def excecute(self):
        print("Age of Chattogrqam : " + self.age)
        print("Volume of Chattogram : " + self.volume)
        print("Area of Chattogram : " + self.area)

object_Chatto=Chattogram("151 year","34245km","2345km")
print("\n")
object_Chatto.excecute()


