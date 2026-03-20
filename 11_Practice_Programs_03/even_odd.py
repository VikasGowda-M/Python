#Print even numbers and odd numbers from 1 to n using for loop and range() function:
n = int(input("Enter a number: ")) 
print("Even numbers from 1 to", n, "are:")
for i in range(2,n+1,2):
    print(i)
print("Odd numbers from 1 to",n,"are")
for j in range(1,n+1,2):
    print(j)

#Print even numbers and odd numbers from 1 to n using while loop and range() function:
n = int(input("Enter the number"))
i=1
print("Even numbers from 1 to", n, "are:")
while i<=n:
    if i%2==0:
        print(i)
    i+=1
j=1
print("Odd numbers from 1 to",n,"are")
while j<=n:
    if j%2!=0:
        print(j)
    j+=1



        
      
    
    

