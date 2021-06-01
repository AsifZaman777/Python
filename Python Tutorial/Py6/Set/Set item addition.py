
#Add items in Set-------------->

#Once we created the Set we can not change it but we can add items
#add() and update() are used to add the items in `Set`

#Add method ------------------------>

# add() is used to add a single item in Set :

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set1.add("Sadman")
print("Single item addition : ",set1) #Sadman added

#Update method ------------------>

#Update() is used to add multiple items like (List, Tuples, Dict)

#Set to Set addition-->

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={1,55,67,89.0}

set1.update(set2)
print("Set Set add : ",set1)

#Set to List addition-->

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
list1=[1,90,89+2j]
set1.update(list1)
print("Set List add : ",set1)
