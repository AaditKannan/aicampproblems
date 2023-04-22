num = input("Enter the number of students: ")
for i in range (int(num)):
  name = input("Enter the name of student " + str(i+1) + ": ")
  nameList = ["Student " + str(i+1) + ": " + name]
  print(nameList)
