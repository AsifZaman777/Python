# When a non-existent attribute is referenced, and when that attribute reference or assignment fails, an attribute error is raised.

def random():
    a=2
    print(a)

try:
    object1=random()
    print(object1.attribute)  # there is no `attribute` Attribute  in random() function
except AttributeError:
 print("Attribute exception raised")
else:
    print("No exception occured")
