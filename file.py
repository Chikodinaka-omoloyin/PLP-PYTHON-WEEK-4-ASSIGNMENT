import os
# R= Read
# A= Append
# W= Write
# X= Create

# Reads file if it does exist

file = open("names.txt")
for line in file: 
    print(line)
file.close() 

# Trying to read a file that doesn't exist
try:
    file= open("monkeys.txt")
    print(file.read())
except:
    print("The file you want to read does not exist")
finally:
    file.close()   
# Appimportend- Adds more items to the file 
file= open("names.txt", "a")
file.write("\nFunmilayo")
file.close()

file= open("names.txt")
print(file.read())
file.close()

# Write(Overwrites)
file= open("test.txt", "w")
file.write("I am trying to add files to this empty file")
file.close()

file= open("test.txt")
print(file.read())
file.close()

# Opens a file for writing, and creates if it doesn't exist

f= open("monkeys.txt", "w")
f.close()
     

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("grace.txt"):
    file= open("grace.txt","x")
file.close()
# avoid an error if it doesn't exist 
if  os.path.exists("grace.txt"):
    os.remove("grace.txt")
else:
    print("The file you wish to delete does not exist")

with open("friends.txt") as file:
    content= file.read()
with open("names.txt","w") as file:
    file.write(content)          