# #Printing sum  of n numbers using while loop:
num = int(input("Enter the number:"))
sum = 0
i = 1
while i<=num:
      sum += i
      i +=1
print("sum of ",num,"numbers is",sum)


# #Printing sum of n numbers using for loop:
num = int(input("Enter the number:"))
sum = 0
for i in range(num+1):
      sum += i
print("sum of ",num,"numbers is",sum)
      
