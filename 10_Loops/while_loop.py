#While loop: it is used to repeat a block of code as long as a specified condition is true.
#example: in spotify we can continuesly play the same song by clicking the repeat button.
#syntax: while condition:

#01. Print numbers from 1 to 5 using while loop:
i = 1
while i<=5:
    print(i)
    i+=1#Output: 1 2 3 4 5

#02. Print a given string from user input 5 times :
str = input("Enter a string: ")
i = 1
while i<=5:
    print(str)
    i+=1#output: if user input is "Hello" then output will be "Hello" printed 5 times.


#Break statement: it is used to exit the loop when a specified condition is met.
i = 1
while i<=5:
    if i == 3:
        break
    print(i)
    i+=1#Output: 1 2


#Continue statement: it is used to skip the current iteration of the loop when a specified condition is met and continue with the next iteration.
i = 1
while i<=5:
    if i == 3:
        i+=1
        continue
    print(i)
    i+=1#Output: 1 2 4 5