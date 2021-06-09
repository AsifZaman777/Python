x=int(input())
y=int(input())

try:
    x/y
except (ZeroDivisionError):
    print("Exception : check the value of y")
else:
    print(x/y)

