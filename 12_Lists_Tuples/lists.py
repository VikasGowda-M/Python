#Lists in Pyhton are ordered, mutable, and allow duplicate elements. 
#Lists are defined using square brackets [] and can contain elements of different data types.
#Creating a list
my_list = [1, 2, 3, "Hello", 4.5, True]
print(my_list)#Output: [1, 2, 3, 'Hello', 4.5, True]

#Accessing elements in a list:
print(my_list[0])#Output: 1
print(my_list[3])#Output: Hello

#Modifying elements in a list:
my_list[1] = 20
print(my_list)#Output: [1, 20, 3, 'Hello', 4.5, True] here 2 is changed to 20.

#Adding elements to a list:
my_list.append("World")#this will add "World" to the end of the list.
print(my_list)#Output: [1, 20, 3, 'Hello', 4.5, True, 'World']

my_list.insert(2, "Python")#this will insert "Python" at index 2.
print(my_list)#Output: [1, 20, 'Python', 3, 'Hello', 4.5, True, 'World']

#Removing elements from a list:
my_list.remove(20)#this will remove the first occurrence of 20 from the list.
print(my_list)#Output: [1, 'Python', 3, 'Hello', 4.5, True, 'World']

my_list.pop(2)#this will remove the element at index 2, which is 'Python'.
print(my_list)#Output: [1, 3, 'Hello', 4.5, True, 'World']


#Slicing a list:
#syntax: list_name[start:stop:step]
print(my_list[1:4])#Output: [3, 'Hello', 4.5] this will return the elements from index 1 to index 3 (stop index is exclusive).
print(my_list[:3])#Output: [1, 3, 'Hello'] this will return the first three elements of the list.
print(my_list[1:])#Output: [3, 'Hello', 4.5, True, 'World'] this will return all elements from index 1 to the end of the list.
#this can also be written as my_list[1:len(my_list)].


#sorting a list:
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()#this will sort the list in ascending order.
print(numbers)#Output: [1, 2, 5, 5, 6, 9]

numbers.sort(reverse=True)#this will sort the list in descending order.
print(numbers)#Output: [9, 6, 5, 5, 2, 1]

#loop through a list:
for item in my_list:
    print(item)#Output:[1, 2, 3, "Hello", 4.5, True]

#exmaple for loop through a list:
marks = [85, 90, 78, 92, 88]
total = 0
for m in marks:
    total += m
average = total / len(marks)
print("total marks:", total)#Output: total marks: 433
print("average marks:", average)#Output: average marks: 86.6