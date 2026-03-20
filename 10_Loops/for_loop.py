# #for loop: it is used to iterate over a sequence (like a list, tuple, string) etc.
# #syntax: for variable in sequence:


# #01. Print numbers from 1 to 5 using for loop:
for i in range(1,6):
    print(i) #Output: 1 2 3 4 5


# #02. Print a given string from user input 5 times :
str = input("Enter a string: ")
for i in range(5):
    print(str) #output: if user input is "Hello" then output will be "Hello" printed 5 times.


# #03.print letters of a given string from user input:
str = input("Enter a string: ")
for letter in str:
    print(letter) #output: if user input is "Hello" then output will be "H" "e" "l" "l" "o" printed on new line.


#04.find a letter or character in a given string from user input:
str = input("Enter a string: ")
char = input("Enter a character to find: ")
for letter in str:
    if letter == char:
        print(f"Character {char} found in the string.{str}")
        print(f"Character {char} found at index {str.index(char)} in the string.{str}")
        break
else:
    print(f"Character {char} not found in the string.")
    #output: if user input is "Hello" and character to find is "o" then output will be "Character o found in the string.Hello" and "Character o found at index 4 in the string.Hello". 
    # If character to find is "x" then output will be "Character x not found in the string"


#range() function: it is used to generate a sequence of numbers. 
#note:it starts from 0 by default and increments by 1 (by default) and stops before a specified number.
# It takes three arguments: start, stop and step.
# syntax: range(start, stop, step)
# start: it is the starting point of the sequence. It is optional and default value is 0.
# stop: it is the end point of the sequence. It is required. 
# step: it is the increment value of the sequence. It is optional and default value is 1

#05. Print numbers from 1 to n using for loop and range() function:
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i) #Output: if user input is 5 then output will be 1 2 3 4 5

#06. Print even numbers from 1 to n using for loop and range() function:
n = int(input("Enter a number: "))
for i in range(2,n+1,2):
    print(i) #Output: if user input is 10 then output will be 2 4 6 8 10
               

 #pass statement: it is used to skip the current iteration of the loop and continue with the next iteration.    
 #It means "do nothing" now, I will implement it later.
 #07. Print numbers from 1 to n using for loop and range() function and pass statement: 
n = int(input("Enter a number: "))
for i in range(1, n+1):
  pass
print(i) #Output: if user input is 5 then output will be 5. 
         #it skips the for loop for now.