
#------------------------------String Conditions-------------------------->

list1=["asif","tamim","prottoy","Ovy","jubayer","mim"]
newlist=[]

# 1 st method

for i in list1:
    if "a" in i:
        newlist.append(i)
print("Name contains `a` :",newlist)

# 2nd method(One line command)


# >>>>>>Syntax: newlist = [`expression` for `item` in `iterable` if condition == True]<<<<<<

list1=["asif","tamim","prottoy","Ovy","jubayer","mim"]
newlist=[i for i in list1 if "a" in i]
print("\nUsing one line command : ",newlist)

#Another example :
list1=["asif","tamim","prottoy","Ovy","jubayer","mim"]
newlist=[i for i in list1 if i!="jubayer"]
print("\nCondition  : ",newlist)


#Iterable ----------------------->

#Iterable: The iterable can be any iterable object, like a list, tuple, set etc.

newlist=[i for i in range(10)]
print("\nNumbers using range : ",newlist)

#Condition :
newlist=[i for i in range(10) if i<5]
print("\nBelow number 5 : ",newlist)


#Expression -------------------------->

#Expression : The expression is the current item in the iteration, but it is also the outcome,
              # which you can manipulate before it ends up like a list item in the new list

list1=["asif","tamim","prottoy","Ovy","jubayer","mim"]
newlist=[i.upper() for i in list1]
print("\nUpperCase : ",newlist)

#List item manipulation:

#Expression have sometimes Condition

list1=["asif","tamim","prottoy","Ovy","jubayer","mim"]
newlist=[i  if i!="jubayer" else "Sadman" for i in list1]
print("\nJubayer is replaced with Sadman : ",newlist)
