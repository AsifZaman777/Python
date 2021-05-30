

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]

list1.append("Ovy")
print(list1)

list1.insert(1,"Ovy") #Pushed in index 1
print(list1)



#-------------concatination-------------->

#Extend method to concatinate

list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
list2=["Eram",98,True]

list1.extend(list2)
print("Extended list : ",list1)

# `+` to concatinate
print("Concatination : ",list1+list2)
