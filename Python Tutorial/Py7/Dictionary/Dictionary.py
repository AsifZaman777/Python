# Dictionary : A python collection that store data values in `key:values` form
# Dictionary is *ordered [ordered afetr python 3.7.0 but before Dictionary was unordered] and mutable data-structure of python not allow the duplicates

# Dictionary items -------------->

random_dict = {
    "Name": "Asif",
    "University": "AIUB",
    "Semester": "5th",
    "Cgpa": 3.91,
    "Student": True
}
print("\n", random_dict)
print("\n CGPA is :  ", random_dict["Cgpa"], "\nSemester running  :  ", random_dict["Semester"])

# Duplicates are prohibitted to use ------------------------->


random_dict = {
    "Name": "Asif",
    "University": "AIUB",
    "Semester": "5th",
    "Semester": "4th",  # this will be printed
    "Cgpa": 3.91,
    "Student": True
}
print(random_dict)
