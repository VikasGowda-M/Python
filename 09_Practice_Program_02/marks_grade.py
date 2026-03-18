# #marks grade:
marks1 = int(input("Enter marks for subject 1(out of 100): "))
marks2 = int(input("Enter marks for subject 2(out of 100): "))
marks3 = int(input("Enter marks for subject 3(out of 100): "))
total_marks = marks1 + marks2 + marks3
print("Total marks obtained from all 3 subjects:", total_marks)
percentage = (total_marks / 300) * 100
if percentage >= 90:
    print(f"Grade: A \n obtained percentage is :{percentage:.2f}% - excellent performance")
elif percentage >= 80 and percentage < 90:
    print(f"Grade: B \n obtained percentage is :{percentage:.2f}% - good performance")
else:
    print(f"Grade: C \n obtained percentage is :{percentage:.2f}% - needs improvement")











