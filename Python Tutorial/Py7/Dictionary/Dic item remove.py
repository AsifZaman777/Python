
random_dict={
    "Name":"Asif",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}

# pop() method is used to delete the specific key ---->

random_dict.pop("Cgpa")
print("Using pop() : ",random_dict) # Cgpa deleted






# popitem() method deletes the last inserted item ------>

sample1={
    "Name  ":"Asif",
    "Age   ":20,
    "Blood-Group":"A+"   # last inserted item
}
sample1.popitem()
print("\nSample 1 : ",sample1) # Blood group deleted

sample1["University"]="AIUB"  # item inserting
print("Item inserted : ",sample1)

sample1.popitem()
print("Inserted item deleted : ",sample1) #university deleted


### Notation : in versions before 3.7, a random item is removed







# del() method deletes the specified key with items

random_dict={
    "Name":"Asif",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}
del random_dict["Semester"]
print("\nUsing del() : ",random_dict) # Semester deleted

# Entire dictionary deletion from memory

sample2={
    "Name : ": "Asif ",
    "Age : ": "23",
    "Location : ": "Mirpur"
}
del sample2 #sample2 deleted from the memory





# Clear() deletes  the items of the dictionary but dictionary remains in the memory

random_dict={
    "Name":"Asif",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}
random_dict.clear()
print("\nBlank dictionary : ",random_dict)