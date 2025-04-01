class Students:
    count = 0
    total_gpa = 0;
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa

    def get_info(self):
        return f"this is {self.name} with {self.gpa} gpa"

    @classmethod
    def get_count(cls):
        return f"The total no. of students is {cls.count}"
    @classmethod
    def get_avg(cls):
        return f"THe average gpa is {cls.total_gpa/cls.count}"


student1 = Students("Yash",10)
student2 = Students("Harsh",7.05)
student3 = Students("Henry",0.00)
print(Students.get_count())
print(Students.get_avg())