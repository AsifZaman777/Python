# Python File 
 File handing is very important for web and mobile applications. Python also allows us
 to handle the file 
 
## File Handling
- The key function for working with files in Python is the open() function.

- The open() function takes two parameters; filename, and mode.
``Exapmple : file=open("Demo,txt","rt")``

- There are four different methods (modes) for opening a file:

```
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
```

In addition you can specify if the file should be handled as binary or text mode

```
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
```

## Os & Shutil module :
`Os` module : The Python `os.remove()` method deletes a file from your operating system. `os.remove()` only deletes a single file. It cannot delete a directory.
The os module allows developers to interface with the operating and file systems of a computer. `os.remove()` is a method included in the Python os module that allows you to delete an individual file.
Before we start working with these methods, we need to import the os library using a Python import statement.

```
os.remove("Filaname.ext")
```

os.rmdir() delete the empty directory only
```
os.rmdir("Filename.ext")
```



`Shutil` Module : If directory is not empty although we can easily delete the directory
but in `os module ` when we try to delete a directory containing files the directory
not be deleted.


The shutil library offers a number of functions related to file operations. 
In our case, we want to focus on the shutil.rmtree() method, which removes 
an entire directory tree.
```
import shutil

shutil.rmtree(file_path) # directory tree will be deleted 
```

# 
