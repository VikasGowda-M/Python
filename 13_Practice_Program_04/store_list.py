#Ask users to enter the names of three stores and store them in a list. Then, display the list:
list = []
for i in range(1,4):
    list.append(input(f"enter the name {i}:"))
print(list)


#Ask users to enter number of names and  enter the names of each person and store them in a list. Then, display the list:
n = int(input("enter the number of person:"))
list = []
for i in range(1,n+1):
    list.append(input(f"enter the name {i}:"))
print(list)