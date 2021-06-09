#When unexpected values are inserted by the user

try:
    x=input("Please insert your age: ")
    y=int(x)  # Casting in integer
    print("Number is : ",y)
except (ValueError):
    print("\nException : Enter Integer value only")


