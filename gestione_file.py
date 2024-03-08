import os

filename = input("Enter filename:")
print("filename is: " + filename)

if os.path.exists(filename):
  f = open(filename, "a")
  f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!")
  f = open(filename, "r")
  print(f.read())
  f.close()
else:
  open(filename, "x")
  print("Il file creato!")



 
