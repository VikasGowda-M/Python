#finding maximum and minimum in a list:
list = [4,12,1,3,2]
list.sort()
print("the maximum number is:",list[-1])#Output: the maximum number is: 12
print("the minimum number is:",list[0])#Output: the minimum number is: 1


#uing loops and list:
list = [4,12,1,3,2]
max_num = list[0]
for i in list:
    if i > max_num:
        max_num = i
print("the maximum number is:", max_num)

min_num = list[0]
for i in list:
    if i < min_num:
        min_num = i
print("the minimum number is:", min_num)

