# 2)write a program to take a input from the user and print the details
#   *Student Name 
#   *Student maths marks
#   *Student science marks
# ->print student name in Upper case
# ->add students marks (math+science) then print the total marks
# ->then find the average of two subjects

Name=input("enter the student name")
maths=int(input("enter the  maths marks"))
science=int(input("enter the science marks"))
print("name.uppercase(name)" ,Name)
totalmarks=maths+science
print(totalmarks) 
averagemarks=maths+science/2
print(averagemarks)