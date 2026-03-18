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


#methods of string:
#1. len(): The len() function is used to get the length of a string.
print(len(name))
#2. upper(): The upper() function is used to convert a string to uppercase
print(name.upper())
#3. lower(): The lower() function is used to convert a string to lowercase
print(name.lower())
#4. find(): The find() function is used to find the index of the first occurrence of a substring in a string.
print(name.find("Gowda"))
#5. replace(): The replace() function is used to replace a substring with another substring in a string.
print(name.replace("Vikas", "Priyanka"))
#6. split(): The split() function is used to split a string into a list of substrings based on a specified delimiter.
print(name.split(" "))
#7. strip(): The strip() function is used to remove any leading and trailing whitespace from a string.
name_with_spaces = "   Vikas Gowda M   "
print(name_with_spaces.strip())
#8. isalpha(): The isalpha() function is used to check if all the characters in a string are alphabetic
print(name.isalpha())
#9. isdigit(): The isdigit() function is used to check if all the characters in a string are digits
print(name.isdigit())
#10. slice(): The slice() function is used to extract a portion of a string.
print(name[0]) #prints the first character of the string
print(name[0:5]) #prints the first 5 characters of the string
#11. count(): The count() function is used to count the number of occurrences of a substring in a string.
print(name.count("a")) 
#12. startswith(): The startswith() function is used to check if a string starts with a specified substring.
print(name.startswith("Vikas"))
#13. endswith(): The endswith() function is used to check if a string ends with a specified substring.
print(name.endswith("M"))
#14. index(): The index() function is used to find the index of the first occurrence of a substring in a string. 
# It raises an error if the substring is not found.
print(name.index("Gowda"))
#15.cocatination: The + operator is used to concatenate two strings.
str1 = "Hello"
str2 = "World"
new_str = str1 + " " + str2
print(new_str)
print(len(new_str))






#String method and String function :
#the difference between a string method and a string function is that a string method is called on a string object 
# and it modifies the string object itself, 
# while a string function is called on the string class 
# and it returns a new string object without modifying the original string object.
#in methods we use dot operator to call the method on the string object.







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