# with open ("test_file.txt",'r+') as file:
#     file.write("testing writing in the files2")
import os
import datetime
import csv
# os.rename('testig_rename.txt', 'testing_rename.txt')
# y = os.scandir()
# print(y)
# x= os.lstat(os.getcwd())
# print(x)
# z=os.path.getsize('testing_rename.txt')
# print(z)
# timestamp = os.path.getmtime('testing_rename.txt')
# v = datetime.date.fromtimestamp(timestamp)
# print(v)
# w = os.path.abspath("spider.txt")
# print(w)
# d = os.listdir('test_dir')
# print(d)
#os.mkdir('test_dir2')

# host = [['test_machine', '192.168.2.1'],['2test_machine', '192.1.1.1']]
# with open('host.csv','w') as test_csv:
#     writer = csv.writer(test_csv)
#     writer.writerows(host)

#exercise 1
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = users[0].keys()
with open('by_department.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


#exercise 2

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open('flowers.csv','r') as file:
    # Read the rows of the file into a dictionary
    dict_file = csv.DictReader(file)
    # Process each item of the dictionary
    for row in dict_file:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))


#exercise 3

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open('flowers.csv', 'r') as file:
    # Read the rows of the file
    rows = csv.reader(file)
    next(file)
    # Process each row
    for row in rows:
      color, name, ttype = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(name, color, ttype)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

