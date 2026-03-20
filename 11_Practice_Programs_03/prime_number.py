#chech whether the given number is prime or not using while loop :
num = int(input("Enter a number: "))
if num > 1:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "is not a prime number")
            break
        i += 1
    else:
        print(num, "is a prime number")
else:
    print("enter a number greater than 1")



#chech whether the given number is prime or not using for loop :
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print("enter a number greater than 1")




        


