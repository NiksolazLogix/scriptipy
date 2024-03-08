import os

filename = input("Enter filename:")
print("filename is: " + filename)

if os.path.exists(filename):
  os.remove(filename)
else:
  print("The file does not exist")
  path = os.getcwd()
  dir_list = os.listdir(path)
  for l in dir_list:
    if l.endswith(".txt"):
      print(l)
    else:
      print("No txt files in this directory")