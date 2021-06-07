# two eays to copy the dictionaries

# copy()---------------------------------------->

random_dict={
    "Name":"Asif",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}
newDict=random_dict.copy()
print(newDict) #Dictionary copied

# dict()  ---------------------------------------->

random_dict={
    "Name":"Asif",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}
print("\n")
newDict=dict(random_dict)
print(newDict)