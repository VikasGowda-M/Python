#Dictionaries: It is a key value pair.
#they are mutable and unodered.
#example:
dict = {
    "name":"vikas",
    "age":20,
    "class":6
}
print(dict)#output is {'name': 'vikas', 'age': 20, 'class': 6}.



dict["sur_name"]="gowda"#this will add the new key with its value to previous named dictionary.
print(dict)#output is {'name': 'vikas', 'age': 20, 'class': 6, 'sur_name': 'gowda'}



#creating empty Dictionary:
names = {}
print(names)#output is {}.



#Nested Dictionary:We can create a dictionary inside the dictionary,
#example:
student = {
    "names" : {
        "vikas","ullas"
    },
    "subjects" : {
        "science","math"
    },
    "marks" : {
        50 , 60
    }
}
print(student)

#to print values of inside dictionary:
print(student["names"])#we use square brackets for inner dictionary to acces value from outer dictionary.
#the output is {'ullas', 'vikas'}.



#dictionary methods:
student.keys()#return all keys.
student.values()#return all values.
student.items()#returns all key and its respective values.
student.get("names")#return that key vales."if there is no key in dictionary present given by user it dosnt give error instead it prints none".  
student.update({"names":"priyanka"})#adds key with value to dictioanry.



#Type casting in dictionary:
#we can create list tuples  inside the dictionary.
dict2 = {
    "names" : ["vikas","priyanka"] 
    
}
print(dict2)


