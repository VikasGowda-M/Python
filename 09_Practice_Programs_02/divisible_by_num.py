#check wether the given number is divisible by the other number or not:
num1 = int(input("Enter the number to be checked: "))
num2 = int(input("Enter the number to check divisibility: "))
result = num1 % num2
if num2 != 0:
    if result == 0:
        print(f"{num1} is divisible by {num2}.")
else:
    print("Cannot divide by zero.")