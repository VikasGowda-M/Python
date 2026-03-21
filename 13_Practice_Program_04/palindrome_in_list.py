#Check whether the given list is palindrome or not:(hint:use copy()):
list_1 = [1,2,3,2,1]
list_2 = list_1.copy()  #list_2 = list_1[::-1]
list_2.reverse()
print(list_2)
if list_1 == list_2:
    print("List is palindrome")
else:
    print("not a palindrome")


 #Check whether any element in given list is palindrome or not:
list_1 = [121,144,"madam","vikas"]
for word in list_1:
        if  str(word) == str(word)[::-1]:
             print(f"{word}:  is a plaindrome")
        else:
            print(f"{word}:   is not  a plaindrome")

#Ask users to enter the number of elements in list and name them astore them in a list. Then, display the list,
# #Check whether any element in given list is palindrome or not:
n = int(input("Enter the number of elements in list:"))
list_1 = []
for i in range(1,n+1):
     list_1.append(input(f"enter the element  {i} :"))
print("the list is :",list_1)
for word in list_1:
     if str(word) == str(word)[::-1]:
           print(f"{word}:  is a plaindrome")
     else:
        print(f"{word}:   is not  a plaindrome")




