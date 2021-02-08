######################################### ASSIGNMENT 2 ##################################################

# 1. Write a program that asks the user to enter her/his name and her/his age. Print out a  message the year that s/he will turn 80 years old.
# Example: Output: Hello <user_name>, You will turn 80 years in <year>


name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2020 - age)+80)
print( "Hello ",name , " You will be 80 years old in the year " , year)

# 2. Write the same program as above printing when the user will turn 80 years and 100  years

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2020 - age)+100)
print( "Hello ",name , " You will be 100 years old in the year " , year)

# 3. Write a program that asks user to input a number. Program should print the number  with a label to identify the even and odd number.
#Example: if the number input is 12, it should print:
#12 EVEN

num = int(input(" enter the number :"))
if (num%2) == 0:
    print(num,"is EVEN")
else:
    print(num,"is ODD")

#4. Write a program that asks user to input a floating-point number, convert the number to  integer and print the integer value and its type

num = float(input("enter a floating number :"))
int_num = int(num)
print(int_num,type(int_num))

#5. Write a program to print the output of
#bool(0)

num = 0
print(bool(num))

#6. Write a program that returns the maximum of two numbers

a = 2
b = 4
if(a>b):
    print("a is maximum then b")
elif(b>a):
    print("b is maximum then a")

# Python program to find the
# maximum of two numbers


a = 2
b = 4

maximum = max(a, b)
print(maximum)

#7. Write a program that asks user to input 3 numbers and print the greatest number.

num1,num2,num3 = 9,6,7

#uncomment the lines if you want number from user
# num1 = float(input("enter the first number"))
# num2 = float(input("enter the second number"))
# num3 = float(input("enter the third number"))
if(num1>=num2) and (num1>=num3):
    largest = num1
elif(num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3

print("the largest number is",largest)

#8. Write a program that asks user to provide price of a Samosa,
#if the price is less than Rs. 5, print, “Wow, it is very cheap Samosa, I will eat 5
#samosas and I will pay Rs. <calculate price of samosas>”
#if price is between Rs. 5 and 20, “I will eat 2 samosas and I will pay Rs. <calculate  price of samosas>”
#if price is more than Rs. 20, print, “Not today, will have it some other day”

samosa_price = float(input("enter the price of samosa :"))
if(samosa_price<5):
    print("WOW, it is very cheap samosa ,i will eat 5 samosa and i will pay RS" ,5*samosa_price)
elif(samosa_price>5) and (samosa_price<20):
    print("i will eat 2 samosas and i will pay RS" , 2*samosa_price)
elif(samosa_price>20):
    print("not today,will have it some other day ")
else:
    print("ok bye")

#9. Write a program that asks user to input a number.
# If the number is divisible by 3, it should return “Three”.
# If it is divisible by 5, it should return “Five”.
# If it is divisible by both 3 and 5, it should return “ThreeFive”.
#Otherwise, it should return the same number.

num1=int(input("Enter your number:"))
if(num1%3==0):
    print(" is divisible by 3",num1)
elif(num1%5==0):    
    print("is  divisible by 5",num1)
elif(num1%3 and num1%5):
    print("it is divisible by 3 and 5",num1)
else:
    print(num1)

#10. Write a program for calculator, which ask user to input two numbers and input one  operation between +, -, * or /.
# Based on user input print the output Ex. Result of <number1 > <operation> <number2> = <output>
# Ask user to input if “want to continue using calculator (Y/N):” and repeat the same  calculator flow as above
# This function adds two numbers

# menus
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
a = int(input("enter thefirst number"))
b = int(input("enter the second number"))
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    c=a+b
    print(a , "+" ,b , "=" ,c)                      

elif ch==2:
    c=a-b
    print(a , "-" ,b , "=" ,c)                      

elif  ch==3:
    c=a*b
    print(a , "*" ,b , "=" ,c)                      


elif ch==4:
    c=a/b
    print(a , "/" ,b , "=" ,c)                      

else:
    print("Invalid Choice")












