########################ASSIGNMENT 4################################################

#1. Create a function that can accept two arguments user_name and user_age and print its value

def welcome_student_multiple_params(user_name,user_age): # def is a keyword which stands for define 
    print(f'Hi {user_name},')
    print(f'age {user_age}')

user_name = input('what is your name: ') 
user_age=int(input('what is your age: '))
## Call a function
welcome_student_multiple_params(user_name,user_age) 

#2. Write a function arithmetic_calculator() which accepts two parameters and calculate
#the addition, subtraction, multiplication and division of it and returns the calculated values
def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def divide(x, y):
    return x / y  
  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  


#3. Create a function show_student_details() which accepts student_name and
#student_roll_number and prints both, and if the student_roll_number is missing in function call it should show it as 99

def show_student_details(student_name,student_roll_number=99):
    print("name", student_name, "roll no is:",student_roll_number )

show_student_details("zahra",99)
show_student_details("zahra")

#4. Generate a Python list of all the even numbers between 4 to 30 using list() and range() function

# numbers = [] 
# for i in range(4, 30):
#     if i % 2 == 0:
#         numbers.append(i)
[_ for _ in range(4, 30, 2)] 

#5. Write a function which returns the largest item from the given list using in-built function max()
#numbers_list = [4, 6, 8, 24, 12, 2, 6]

numbers_list = [4, 6, 8, 24, 12, 2, 6]
print(max(numbers_list))


