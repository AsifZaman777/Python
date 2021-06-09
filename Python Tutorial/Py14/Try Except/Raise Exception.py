# Throw an exception based on condition
# We can throw an exception using `raise` keyword

x=int(input("Please enter positive value : "))

if x<=-1:
    raise Exception("Negative numbers are not allowed")
else:
    print(x)

