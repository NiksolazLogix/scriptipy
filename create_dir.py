import os

directory = input("Enter directory name:")

parent_dir = "/Users/niksolaz/Desktop/Development/pytut/"
path = os.path.join(parent_dir, directory)

if os.path.exists(path): 
  print("Directory '% s' already exists" % directory)
else:
  try:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
  except OSError as error:
    print(error)

filename = input("Do you want create file? (y/n):")

if filename == "y":
  filename = input("Enter filename:")
  path = os.path.join(parent_dir, directory, filename)
  if os.path.exists(path):
    print("File '% s' already exists" % filename)
  else:
    open(path, "x")
    print("File '% s' created" % filename)