# arguments are the elements or items passed in the function



# argument ---------------------->

string1="tamim"
string2="prottoy"

def name(string1,string2):
    print(string1+" "+string2)

name(string1,string2)

# Arbitary arguments (*args  [Py documentation notation]) -------------------->

#----------------------------------------------------------------

# If we do not know how many arguments that will be passed into our function, add a `*` before the parameter name in the function definition.
# ---------> Arbitary argument return a tuple  <-------------

#----------------------------------------------------------------

def friends(*name):
    print("\nNames of friends : ",name) # >>Tuple of name returned <<

def access_index(*acccess):
    print("Tuple index access : ",acccess[2]) # >>Ovy returned <<

friends("Tamim","Prottoy","Ovy","Sadman","Jubayer")
access_index("Tamim","Prottoy","Ovy","Sadman","Jubayer")






# Keyword arguments---------------------->

#---------------------------------------------------------------

#We can also send arguments with the `key = value` syntax.
#Do not follow the order

#---------------------------------------------------------------

def keyword(friend1,friend2,friend3):
    print("\nName of one friend : ",friend2)

keyword(friend1="Tamim",friend2="Prottoy",friend3="Ovy")


# Arbitary Keyword argument(kwargs [Py Documentation]) ----------------------->
#-----------------------------------------------------------

# If we do not know how many keyword arguments that will be passed into our function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly

#-----------------------------------------------------------

def keyword(**friends):
    print("\nName of one friend : ",friends) # dictionary returned

keyword(friend1="Tamim",friend2="Prottoy",friend3="Ovy")


def arg_keyword(**friends):
    print("\nName of one friend : "+friends["person1"]) # dictionary returned
    print("Name of one friend : " + friends["person3"])  # dictionary returned


arg_keyword(person1="Tamim",person2="Prottoy",person3="Ovy")






#Default parameter value ------------------->

# without passing any argument a default function value will be shown
print("\nDefault argument : ")
def name(human_name="Asif"):
    print(human_name)

name("Tamim")
name("Prottoy")
name("Jubayer")
name()
name("Mim")

# we can also send the python collection [List, Set, Tuple, Dictionary]   into a function

def random_list(list1):
    print("\nList : ")
    for i in list1:
        print("\n",i)


list1=["Tamim","Prottoy","Ovy"]
random_list(list1)





#Pass statement  ----------------->
# function content can not be empty if we need to keep it empty we can use `Pass`

def random():
    pass




