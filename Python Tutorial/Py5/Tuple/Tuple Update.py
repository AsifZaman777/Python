# Once tuple is created it can not be modified anymore
# First thing first so we need to convert the `tuple` in a `List`
# Then we need to convert the list in to a tuple again

#  Item Manipulation -------------------->

tuple1=("Asif","Jubair",105,True,"Tamim")
list1=list(tuple1)
print("Py5 turned into list : ",list1)

list1[1]="Prottoy" #item updated in list
tuple1=tuple(list1)
print("Update tuple : ", tuple1)

# Item Addition -------------------------->

tuple1=("Asif","Jubair",105,True,"Tamim")
list2=list(tuple1)
list2.append("Coke")
tuple1=tuple(list2)
print("Item added in tuple: ",tuple1)
