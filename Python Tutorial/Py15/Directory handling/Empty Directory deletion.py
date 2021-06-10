import os
try:
  path="C:\\Users\\User\\Desktop\\PyFile"
  os.rmdir(path) #only delete the empty file
except:
    print("Make the file empty")