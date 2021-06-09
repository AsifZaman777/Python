#LookUp Error
# Lookup Error acts as a base class for the exceptions that occur when a key or index used on a mapping or sequence of
# a list/dictionary is invalid or does not exists.

# The two types of exceptions raised are:
#
# IndexError
# KeyError

dictionary1={
    1:"Asif",
    2:"Jubayer",
    3:"Tamim"
}
try:
    print(dictionary1[4])  #out of bound (Key error)
except LookupError:
    print("Out of bounds")
else:
    print(dictionary1)


print("\n")
list1=["Asif","Protty","Tamim","Jubayer","Ovy"]
try:
    print(list1[6])
except LookupError:
    print("Out of bound")
else:
    print(list1)