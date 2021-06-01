
#Set item can be removed by multiple ways ------------->

# 1 Using Remove() ------>
# >>>> Remove() will show an `ERROR` when the item we want to remove that doesn't exist in the SET <<<<<

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set1.remove("Mim")
print("Mim Removed : ",set1)

# 2 Using Discard() -------->
# >>>> Discard() will not show an `ERROR` when the item we want to remove that doesn't exist in the SET <<<<<

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set1.discard("Tamim")
print("\nTamim Removed  : ",set1)

# 3 Using Pop() -------->
# >>>>> Pop() will remove the last element of the `Set` as Set is inordered so we dont know what is the last item <<<<<

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set1.pop()
print("\nLast item removed : ",set1)

# 4 Using Clear() --------->
# >>>>> Clear will remove all the elements of the set but set remains <<<<<

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set1.clear()
print("\nSet is blank : ",set1)

# 5 Using del() ----->
#set1 will be removed from the memory (No existance)

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
del set1

# Now print(set1) will show Error.
