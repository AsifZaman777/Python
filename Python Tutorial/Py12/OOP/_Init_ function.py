# Normally python classes have _Init_ function. In object oriented concept it is known as `constructor`

# __init__ is one of the reserved methods in Python. The __init__ method can be called when an object is created from the class,
# and access is required to initialize the attributes of the class.
# Moving on with this article on Init In Python,

# Self keyword   --------->
#self keyword is similar like an object. It creates an instance

class info :
    def __init__(self,name,age):
        self.name=name
        self.age=age

object=info("Asif Zaman",21)

print(object.name)
print(object.age)



