#Data types are the classification of data which tells the compiler or interpreter how the programmer intends to use the data.
#DataTypes in Python are:
#1. String
#2. Integer
#3. Float
#4. Boolean


#1. String: A string is a sequence of characters enclosed in single quotes, double quotes or triple quotes.
name = "Vikas Gowda M"
print(name)
#here name is a string variable that contains the value "Vikas Gowda M".


#2. Integer: An integer is a whole number without a decimal point. it can be positive, negative or zero.
age = 21
print(age)
#here age is an integer variable that contains the value 21.



#3. Float: A float is a number that contains a decimal point.
height = 5.9
print(height)
#here height is a float variable that contains the value 5.9.



#4. Boolean: A boolean is a data type that can only have two values: True or False.
is_student = True
print(is_student)
#here is_student is a boolean variable that contains the value True.



#Impoetant point to note here is that we can change the value of a variable by assigning a new value to it.
#Example:
namge = "Vikas Gowda M"
age = 21
age = 19
print(age)

 
#To check the data type of a variable we can use the built-in function type() which returns the data type of the variable.
name = "Vikas Gowda M"
age = 21
height = 5.9
is_student = True
print("data type to store name is:", type(name))
print("data type to store age is:", type(age))
print("data type to store height is:", type(height))
print("data type to store is_student is:", type(is_student))