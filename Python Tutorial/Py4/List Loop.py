
# 1 Using for without range

print("\nFor loop excecution : ")
list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]

for i in list1:
    print(i)


# 2 using  range func

print("\nRange function excecution : ")
list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
for i in range(len(list1)):
    print(list1[i])


# 3 While Loop

print("\nWhile loop excecution : ")
list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
i=0
while i<len(list1):
    print(list1[i])
    i=i+1

# 4 Short hand for loop  (Most effective way to display)

print("\nShort hand for loop excecution : " )
list1=["asif",True,90.78,"tomato","carrot","AIUB","Smart"]
[print(i) for i in list1]
