class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getinfo(self):
        return f"{self.name} as {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_position
    

employee1 = Employee("Henry","Manager")
employee2 = Employee("Tom","Cashier")
employee3 = Employee("David","Cook")
employee4 = Employee("Michel","Janitor")
print(Employee.is_valid_position("Manager"))
print(employee1.getinfo())
print(employee2.getinfo())
print(employee3.getinfo())