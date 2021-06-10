#File creation
# file creation in directory
try:
  path="C:\\Users\\User\\Desktop\\PyFile\\"
  friends=open(path+"HalalBoys.txt","x")
except:
    print("File already exist")
