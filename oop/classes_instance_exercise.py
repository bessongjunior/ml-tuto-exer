'''
Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
'''

class Student:
    student_name = 'Junior Besong'
    marks = 85 
    
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")

setattr(Student, 'student_name', 'Bessong Junior') 
setattr(Student, 'marks', 85) 

print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")

