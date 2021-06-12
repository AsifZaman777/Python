# in / not in / is not operators are used to check the items in list
# in and not in used in list or string
# is not is use in no literal object

#Character check in string

name="Asif Zaman"
if "Z" in name:
    print("\nGot it")
else:
     print("\nDont get it")

# List item check

friend_list=["Asif","Tamim","Prottoy","Ovy"]

if "Asif" in friend_list:
    print("\nAvailable")
else:
    print("Asif not acailable")

if "Asif" not in friend_list:
    print("\nNo avalilable")
else:
    print("Available")

# `is not`

name=None
if name is not None:
    print("Name is {}".format(name))
else:
    print("\nNo name available")

