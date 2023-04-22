numList = []
num = int(input("Enter the number of students: "))
for i in range (0, num):
  name = input("Enter the name of student " + str(i+1) + ": ")
  numList.append(name)
for i in range(0, num):
  print("Student " + str(i+1) + ": " + numList[i])
