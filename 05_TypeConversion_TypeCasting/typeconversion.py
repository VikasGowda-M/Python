'''#TypeConversion or TypeCasting is the process of converting one data type to another data type.
#Example: Which Shows error

# {{  age = input("Enter your age: ")
# print("Your age is ", age + 10)  }}

#In the above code we are trying to add 10 to the age which is a string and it will give an error 
#because we cannot add a string and an integer.'''


#To fix this error we can use type conversion to convert the age from string to integer before adding 10 to it.
age = int(input("Enter your age: "))
print("Your age is ", age + 10)
#In the above code we are using the int() function to convert the age from string to integer 


#another way to do type conversion is
age = input("Enter your age: ")
age = int(age)
print("Your age is ", age + 10)

#Similarly we can also convert a string to a float using the float() function and a string to a boolean using the bool() function. 
#Example 1:
height = float(input("Enter your height: "))
print("Your height is ", height + 0.5)

#Example 2:
is_student = bool(input("Are you a student? (True/False): "))
print("Is student: ", is_student)
