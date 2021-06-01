
# 1 Union() ---------->
# Union() method that returns a new set containing all items from both sets,

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={1,3,4,5}
newSet=set1.union(set2)
print("\nNew Set : ",newSet)

# 2 Update () ------------->
# update() method that inserts all the items from one set into another:

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={1,3,4,5}
set1.update(set2)
print("\nUpdated set 1 : ",set1)

# 3 intersection_Update() ---------->
# intersection_Update() allows to keep only the duplicate items

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={"Asif","Kakoli","Random","Ovy"}
set1.intersection_update(set2)
print("\nSimilar items : ",set1)

# 4 intersection() ------------->
# Collect the duplicate items but return a new Set

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={"Asif","Kakoli","Random","Ovy"}
newSet=set1.intersection(set2)
print("\nInterSection : ",newSet)

# 5 Symmetric_difference_Update() -------->
# Update the required set without duplicate values

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={"Asif","Kakoli","Random","Ovy"}
set1.symmetric_difference_update(set2)
print("\nSymmetric_difference_Update : ",set1)

# 6 symmetric_difference() -------->
# Return a new set but not allowing the different values

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
set2={"Asif","Kakoli","Random","Ovy"}
newSet=set1.symmetric_difference(set2)
print("\n Symmetric_differance : ",newSet)
