import shutil
try:
   path="C:\\Users\\User\\Desktop\\PyFile"  # path of the directory
   shutil.rmtree(path)  #remove the whole directory"
   print("Directory deleted")
except:
    print("Directory doesn't exist")
