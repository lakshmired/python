# 1. Write a program to print the odd numbers from 1 to 100
# start=1
# end=100

# for i in range(1,100-1):
#    if i %2!=0:
    # print("only odd numbers",i)



# 2. Write a program to print the even numbers from 1 to 100,100+1):

# maximum = int(input(" Please Enter the Maximum Value : "))
# for number in range(1, maximum+1):
    # if(number % 2 == 0):
        #  print("{0}".format(number))


# 3. Write a program to print {20,40,60,80,100} using for loop

# num={20,40,60,80,100}
# soc_set={20,40,60,80,100}
# for numbers in soc_set:
    # print(numbers,end=" ")

#or
# for num in num:
    # print(num)
     
# 4. Using while loop 
# a)print the number 1 to 10
# i = 1
# while(i<=10):
    # print(i)
    # i += 1  


# b)print the numbers 1 to 100  and it should print only even numbers

# max = 100
# num = 1
# 
# while num <= max:
    # if(num % 2 == 0):
        # print("{0}".format(num))
    # num = num + 1
      #or

# num = 2
# while num <= 100:
    # print(num)
    # num = num + 2
 

# c)print the numbers 1 to 100 and should print only odd numbers
#  and it should break the loop when value becomes 51
    
# w=1
# while(w<100):
    # w=w+1
    # print(w)
    # if(w==51):
    #  break
# 
# print("only odd numbers",w)   
    
    
    
# d)print the numbers 1 to 100 and should print 100 and skip 55 using continue 

# for i in range(1,100) :
# 
    # if i==55:
        # continue
    # else:
        # print(i, end=" ")


# 5. Write a 
# program to print the tables from 1 to 10
# take a input from user.

# 2 x 1= 2
# ..
# ..
# 2 x 10 =20


# num=int(input("enter the table number :\n"))
# for i in range (1,11):
    # print(f'{num}*{i}={num*i}')




# 6. Write a program to validate a person can vote or not
# *take the age as input from the user
# if age is less than 18 print he cannot vote
# if age is greater than 18 print he can vote
# if age is greater than 90 print please stay at home
# if age is 18 than  print please make the voter id


age=int(input("enter your age " ))

if age>18:
   print("he cannot vote " ) 
   if age<18:
    print("he can vote " ) 
    if age<90:
      print("please stay at home " ) 
      if age==18:
        print("please make the voter id " ) 
      else:
        print("please  not make the voter id " )
    else:
     
     print("please   use vote " )
else:
 
 print("please not use vote " )    
     
  


# 7.Take a inputs and Evaluate the expressions
# a)Take the Students name
# b)Take the student english marks
# maths,science,social,kannada,hindi while taking the inputs it should be in tha range (0-100)
# c)calculate the % and print

# % <35% print fail and print the Grade 'f'
# % >35% and <55% print just pass and print the Grade 'd'
# % >55% and <60% print  pass and print the Grade 'c'
# % >60% and <75% print  average and print the Grade 'b'
# % >75% and <90% print  good and print the Grade 'a'
# # % >90% and <100% print  excellent  and print the Grade 'A+'


studentsname=input("enter student name:\n")
english_marks=int(input("enter english_marks :\n"))
maths_marks=int(input("enter maths_marks:\n"))
science_marks=int(input("enter science_marks:\n"))
social_marks=int(input("enter social_marks:\n"))
kannada_marks=int(input("enter kannada_marks:\n"))
hindi_marks=int(input("enter hindi_marks:\n"))
for i in range(0,100):
    print("within the marks percentage below 100:\n ")
    # 

total_marks=int(english_marks+maths_marks+science_marks+social_marks+kannada_marks+  hindi_marks )
print("calculate the totalmarks",total_marks) 
average_marks=total_marks/6
print("calculate the average",average_marks)
percentage=float((total_marks/600)  * 100)
print("calculate the percentage",percentage)

marks=input("enter your marks") 

if marks <35:
 print("% to be fail")
else:
    print("the grade is f:",'f')
if marks %35>55:
    print("  there are % got just pass  marks")
else:
    print("the grade is d:","d")
