#Tuples in Python are similar to lists, but they are immutable, meaning that once a tuple is created, its elements cannot be changed. 
#Tuples are defined using parentheses () and can contain elements of different data types.


#main diiference between list ,tuple ,strings are:
#1. Lists are mutable, while tuples and strings are immutable.
#2. Lists are defined using square brackets [],
#  while tuples are defined using parentheses () 
# and strings are defined using single quotes '' or double quotes "".


#Creating a tuple:
my_tuple = (1, 2, 3, "Hello", 4.5, True)
print(my_tuple)#Output: (1, 2, 3, 'Hello', 4.5, True)

#Accessing elements in a tuple:
print(my_tuple[0])#Output: 1
print(my_tuple[3])#Output: Hello


#Modifying elements in a tuple:
#my_tuple[1] = 20 #this will raise a TypeError because tuples are immutable.

#occurrence of an element in a tuple:
print(my_tuple.count(2))#Output: 1 this will return the number of times 2 appears in the tuple.

#Finding the index of an element in a tuple:
print(my_tuple.index("Hello"))#Output: 3 this will return the index of the first occurrence of "Hello" in the tuple.


#tuple packing and unpacking:
#tuple packing:
#we can create a tuple without using parentheses, this is called tuple packing.
#it is useful when we want to return multiple values from a function.
my_tuple = 1, 2, 3, "Hello", 4.5, True
print(my_tuple)#Output: (1, 2, 3, 'Hello', 4.5, True)

#tuple unpacking:
#we can assign the elements of a tuple to individual variables, this is called tuple unpacking.
a, b, c, d, e, f = my_tuple
print(a)#Output: 1
print(d)#Output: Hello
print(f)#Output: True
