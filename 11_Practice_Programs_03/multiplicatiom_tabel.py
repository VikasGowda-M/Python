#Printing multiplication tabel for n number using while loop:
num = int(input("Enter the number :"))
i = 1
while i<=10:
    print(num, "x", i, "=", num*i)
    i+=1

#Printing multiplication tabel for n number using for loop:
num = int(input("Enter the number :"))
for i in range(1,11):
    print(num, "x", i, "=", num*i)
     