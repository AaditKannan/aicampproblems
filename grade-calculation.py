#variables
name = input("Enter your name: ")
maxScore = input("Enter the maximum score: ")
score = input("Enter your score: ")

#conditionals
if int(score) >= 0.6*int(maxScore):
  print(name + ", you passed the test!")
else:
  print(name + ", you failed the test!")
