# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Notation  : 'Read the attached readme file first for better understanding about Lambda'

double=lambda x:x*2  #double value is returned
print(double(5))

# multiply unknown numbers ->

def multiplier(n):
    return lambda x:x*n
digit1=multiplier(2)
print("Answer1 : ",digit1(12))
digit2=multiplier(3)
print("Answer2 : ",digit2(11))


