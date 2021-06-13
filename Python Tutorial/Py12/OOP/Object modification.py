class information :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def func(object):
        print("Student name is  : "+object.name) #self is accessed from the whole class
        print("Student age is : ",object.age)

p1=information("Asif Zaman",23)
print("Before changing the object : ")
p1.func()
print("\nBefore changing the object : ")
p1.age=25  # Updated the age
p1.func()

# delete object -------->
del p1.age   # deleted age

del p1 # Object deleted