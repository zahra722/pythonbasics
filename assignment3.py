###########################ASSIGNMENT 3##################################################

# 1. Write a program to store five city names entered by user in a list.

names = ['ahemdabad', 'hyderabad', 'delhi', 'banglore', 'mumbai']
print(names)

#2. Write a program to input marks of seven students, store it in a list and display them in a sorted manner.

marks = [50,40,60,70,80,90,100,20]
marks.sort()
print(marks)

#3. Write a program to store 5 numbers given by user in a list and print sum of 5 numbers.

list1 = [8,5,6,9,8]
total = sum(list1)
print(total)

#4. Write a program to count the number of zeros in the following tuple:

numbers = (8, 1, 0, 0, 0, 9, 5, 0, 6, 3, 0, 0, 1)
x = numbers.count(0)
print(x)



#5. Write a program to print the multiplication table of a given number using for loop.
#Ex. If user input is 3 print table of 3 as 3, 6, 9 till 30.

num = int(input("enter the number for table you want:"))
for i in range(1,11):
    print(num, 'x' , i, '=', num*i)

#6. Write program 1 again using a while loop.

i = ['ahemdabad', 'hyderabad', 'delhi', 'banglore', 'mumbai']
while i :
  print(i)
  break

#7. Write a program to display a user input name followed by Good Afternoon
name = input("enter your name:")
print(name, "good afternoon")

#8. Write a program to fill in a letter template given below with name and date from
#user input.
#letter = ‘’’ Dear <|User Name|>,
#You are selected to join BlinkEd AWS Certification course!
#<|Today’s Date|>’’’

name = input("enter your name:")
date = int(input("enter date:"))
print( "dear" , name , "\n You are selected to join BlinkEd AWS Certification course! \n " , date)

#9. Write a program to detect double spaces in a string.

course ='BlinkEd   training   2021-Pythonprogramming'
print(course)
print(course.find('  '))

#10. Replace the double spaces from above program with single spaces.

course ='BlinkEd   training   2021-Pythonprogramming'
print(course)
print(course.replace('  ',' '))


#11. Write a program to format the following letter using escape sequence characters.
#email = “Dear John, Please prepare material for BlinkEd ‘Learning and Sharing’
#session. Thanks!!”

print("email =  Dear john ,\n\t\t Please prepare material for BlinkEd ‘Learning and Sharing’ session. \n \t\t\t\t\t\t  Thanks!!”")



#12. Write a program to greet all the person stored in a list “names” below whose name
#starts with S.
#names = [“Tom”, “Jerry”, “Syed”, “Sanjay”, “Rohit”, “Manish”, “Tahir”, “Noor”,“Talib”, “Saif”]

names = ['tom','Jerry', 'Syed','Sanjay', 'Rohit', 'Manish', 'Tahir', 'Noor','Talib', 'Saif']
print(names.pop(2), "congrats")
print(names.pop(2),"congrats")
print(names.pop(7),"congrats")

#13. Write a program to find whether a given number is prime or not.
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")

#14. Write a program to find the sum of first n numbers using a while loop where n is user input

num =int(input("enter the number"))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

#15. Write a program to calculate the factorial of a given number n using for loop where n is user input
num = int(input("enter a number: "))
 
fac = 1
 
for i in range(1, num + 1):
	fac = fac * i
 
print("factorial of ", num, " is ", fac)

#16. Write a program to print the following star pattern.
#*
#***
#***** for n=3
n=1
while n<=5:
    print(n*"*")
    n=n+1




