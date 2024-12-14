import os
# R= Read
# A= Append
# W= Write
# X= Create

def modify_file(filename):
  """Reads a file, adds a line, and writes it to a new file.

  Args:
    filename: The name of the file to modify.
  """

  try:
    with open(filename, 'r') as file:
      content = file.read()

    new_content = content + "\nI just added this new line."

    with open("modified_" + filename, 'w') as new_file:
      new_file.write(new_content)

    print(f"File '{filename}' modified successfully. New file: 'modified_{filename}'")

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except IOError:
    print(f"Error: Could not read or write file '{filename}'.")
  
# Get the filename from the user
filename = input("Enter the filename: ")

# Modify the file
modify_file(filename)