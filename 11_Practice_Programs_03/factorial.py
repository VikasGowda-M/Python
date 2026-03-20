#Printing factorial of a number using while loop:
num = int(input("enter the number:"))
i = 1
fact = 1
while i<=num:
    fact *= i
    i+=1
print("factorial of ",num,"is:",fact)


#Printing factorial of a number using for loop:
num = int(input("enter the number:"))
fact = 1
for i in range(1,num+1):
    fact *= i
print("factorial of ",num,"is:",fact)