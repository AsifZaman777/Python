#Lambda built in functions ---->
# filter() -> takes function and list as argument
#reeturn a new list based on the function evaluation


# ----------------------------------------------------------------
#Syntax ---->
# newList=list(filter(lambda ---- ),listName)
# map() ->
#newList=list(map(lambda -----),listName)
# ----------------------------------------------------------------


#Differance between map() and filter() ->

# In map: Function will be applied to all objects of iterable.

# In filter: Function will be applied to only those objects of iterable who goes True on the condition specified in expression.


#Examples :

random_list=[1,3,4,5,6,12,20,13]
newList=list(filter(lambda x: x%2==0,random_list))  #function runs only for the objects of the iterable that gone `true`
print("Only even numbers : ",newList)


random_list1=[1,3,4,5,6,12,20,13]
newList=list(map(lambda x:x*2,random_list)) # funtions runs for every objects of the iterable
print("Double numbers : ",newList)
