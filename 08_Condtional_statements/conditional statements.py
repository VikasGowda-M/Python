#Conditional statements:
#donditional statements are used to perform different actions based on different conditions. 

#1.if statement: It is used to execute a block of code if a specified condition is true.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")

#2.if-else statement: It is used to execute a block of code if a specified condition is true, and another block of code if the condition is false.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


#3.if-elif-else statement: It is used to execute a block of code if a specified condition is true, and another block of code if the condition is false, and another block of code if the condition is false.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")



#nested if statement: It is used to execute a block of code if a specified condition is true, and another block of code if the condition is false, and another block of code if the condition is true.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
elif age >= 13:
    print("You are a teenager.")
else :
    print("You are a child.")



#logical operators in conditional statements:
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")
if age >= 18 and is_student.lower() == "yes":
    print("You are an adult student.")
elif age >= 18 and is_student.lower() == "no":
    print("You are an adult non-student.")
elif age < 18 and is_student.lower() == "yes":
    print("You are a minor student.")
else:
    print("You are a minor non-student.")






