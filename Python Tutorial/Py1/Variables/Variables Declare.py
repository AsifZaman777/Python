#Variables

#variable name --->

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

var_name="Eram"
var_value=2000
print(var_name,var_value)


#multiple variables assigning 1

x="tamim"
y="ovy"
z="prottoy"

print("assigning 1 : {} {} {}".format(x,y,z))

#multiple variables assigning 2

x,y,z="tamim" ,"ovy" ,"prottoy"

print("assigning 2 : {} {} {}".format(x,y,z))

#multiple variables assigning 3(Using list):

list=["tamim","ovy","prottoy"]
x,y,z=list
print("assigning 3 : {} {} {}".format(x,y,z))