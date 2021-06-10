import os
path="C:\\Users\\User\\Desktop\\PyFile\\"
if os.path.exists(path+"HalalBoys.txt"):
    print("Yes file is available")
else:
    print("File doesnt exist")