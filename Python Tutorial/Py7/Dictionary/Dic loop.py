random_dict={
    "Name":"Asif",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}

# without methods() ----------->

for i in random_dict:
    print(i) # printing keys

print("\n")
for i in random_dict:
    print(random_dict[i]) # printing the values

# With methods()   ------------>
print("\n")

for i in random_dict.keys():
    print(i)  # print keys

print("\n")
for i in random_dict.values():
    print(i) #print values
