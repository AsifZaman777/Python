
list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]

print(list1[0])  #any item in any index
print(list1[2:]) #from 2nd to last
print(list1[:3]) #display before index 3
print(list1[2:5]) #display from 2-4 th index
print(list1[-1]) #display from back
print(list1[-3:-1]) #rev display



#check the existance of item in list

if "tomato" in list1:
    print("yes, tomato in the list")
else:
    print("no")