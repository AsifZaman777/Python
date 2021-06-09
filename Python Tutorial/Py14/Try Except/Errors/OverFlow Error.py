# The Overflow Error is raised when the result of an arithmetic operation is out of range.
# OverflowError is raised for integers that are outside a required range.

try :
    import  math
    print(math.exp(100))
except OverflowError:
    print("Out of range ")