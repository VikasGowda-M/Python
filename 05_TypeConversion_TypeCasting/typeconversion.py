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

#implicit type conversion:
#In implicit type conversion, Python automatically converts one data type to another data type without the need for explicit conversion.
#Example:
num1 = 10
num2 = 5.5
result = num1 + num2
print("The result is ", result)
#In the above code, Python automatically converts the integer num1 to a float before performing the addition operation with num2, 
# which is a float. The result is a float value of 15.5.


#explicit type conversion:
#In explicit type conversion, we manually convert one data type to another data type using built-in functions like int(), float(), str(), etc.
#Example:
num1 = 10
num2 = 5.5
result = num1 + int(num2)
print("The result is ", result)
#In the above code, we are explicitly converting the float num2 to an integer using the int() function before performing the addition operation with num1.
