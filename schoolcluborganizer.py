memList = []
roleList = []
memCt = int(input("Enter the number of members: "))


def mem_f ():
  for i in range(0, memCt):
    memName = input("Enter the name of the member " + str(i+1) + ": ")
    memList.append(memName)
    memRole = input("Enter the role of member " + str(i+1) + ": " )
    roleList.append(memRole)
mem_f ()
print("Club Members:")
for i in range(0,memCt):
  print (memList[i] + " - " + roleList[i])
