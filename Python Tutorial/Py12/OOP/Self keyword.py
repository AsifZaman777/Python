# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class information :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def func(object):
        print("Student name is  : "+object.name) #self is accessed from the whole class
        print("Student age is : ",object.age)

p1 = information("Asif Zaman",21)
p1.func() 



