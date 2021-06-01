
#Sytax

# ---------------------
#   for i in `Collections`:
#       ToDo
# ---------------------

#  OR

# ---------------------
#   for i in `range()`:
#       ToDo
# ---------------------



# List Loooping  ---------------------------------->
print("List :")
print()
newList=["Prottoy","Tamim","ovy"]
for i in newList:
    print(i)


# Continue  --------------->
# Skip iteration using `Continue`
print("\nContinue : ")
newList=["Prottoy","Tamim","ovy"]
for i in newList:
    if i=="Tamim":
        continue
    print(i) #"Tamim " Skipped

#Break --------->
# Loop breaker
print("\nBreak : ")
newList=["Prottoy","Tamim","ovy","Jubayer","Asif"]
for i in newList:
    if i=="Jubayer":
        break
    print(i, end=" ") #before Jubayer

#Looping in `String` --------->
print("\n String index : ")
for i in "Asif Zaman":
    print(i)





# range() function ------------->

# The range() function returns a sequence of numbers,starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

print("\nRange function : ")
for i in range(6):
    print(i)

# Step declaring ------------>

print("\nStep : ")
for i in range(1,10,2):
    print(i, end=" ")

# Reverse counting -------------->
print("\nStep reverse : ")
for i in range(10,1,-1):
    print(i,end=" ")