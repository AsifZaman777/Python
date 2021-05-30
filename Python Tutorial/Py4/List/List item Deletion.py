
# 1 particular item name

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
list1.remove("asif")
print(list1) #first item has been deleted

# 2 particular index deletion

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
list1.pop(1)
print(list1) #index 1 deleted

# 3 particular index deletion

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
del list1[2]
print(list1)

# 4 full list deletion (Item will be deleted but list remains)

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
list1.clear()
print("List deleted",len(list1))

# 5 full list deletion (list will be deleted from memory )

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
del  list1

'''
print(lsit1) ----> Show error(List doesnt exist)
'''