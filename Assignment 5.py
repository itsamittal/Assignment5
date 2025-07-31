Task1: Create a Dictionary of Student Marks
student_marks = {"Alice": 85,"Bob": 92,"Charlie": 78,"Diana": 90}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"student not found.'{name}'.")


Task 2: Demonstrate List Slicing 

numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_five = first_five[::-1]

# Step 4: Print both lists
print('Original list:',numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_five)

