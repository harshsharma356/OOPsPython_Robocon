class Students:
    passingYEAR = 2028  #Class Variable
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_students += 1

student1 = Students("Johan", 18)
student2 = Students("Anna",19)
student3 = Students("John",17)

print(student1.name,student1.age)
print(student2.name,student2.age)
print(student3.name,student2.age)
print(Students.passingYEAR, student1.passingYEAR, student2.passingYEAR)
print(Students.num_students)
print(f"No. of Students graduating in the year {Students.passingYEAR} is {Students.num_students}\nName os these students are\n{student1.name}\n{student2.name}\n{student3.name} ")