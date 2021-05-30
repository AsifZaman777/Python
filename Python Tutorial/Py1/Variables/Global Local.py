#python function is declared by `def`

string1='Canada'

def declare1():
    string1='USA'
    print("I love",string1)

declare1() #printing local
print("I love ", string1) #printing gloabl




#global keyweord to declare any variables globally

def declare2():
    global string3
    string3='bangladesh'

declare2() #defined string3 globally
print("I love " ,string3)