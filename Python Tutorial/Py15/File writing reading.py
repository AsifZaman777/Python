# File write and read

friends=open("C:\\Users\\User\\Desktop\\PyFile\\HalalBoys.txt","w") #only write the value
friends.write("Here all the boys are halal")
friends.write("\n1.Asif")
friends.write("\n2.Ovy")
friends.write("\n3.Tamim")
friends.write("\n4.Prottoy")
friends.write("\n5.Monem")

friends.close()

# friends=open("C:\\Users\\User\\Desktop\\PyFile\\HalalBoys.txt","r") #read the file
# print(friends.read())