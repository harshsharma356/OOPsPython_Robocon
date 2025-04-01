class Company:
    class Empolyee:
        def __init__(self, name, position):
              self.name = name
              self.position = position

class Nonprofit:
    class Employee:
          def __init__(self, name, position):
                self.name = name
                self.position = position

          def get_details(self):
                return f"{self.name} {self.position}"        
    def __init__(self, company_name):
            self.compamy_name = company_name
            self.employees = []
    def add_employees(self, name, position):
            new_employee = self.Employee(name, position)
            self.employees.append(new_employee)
    def list_employees(self):
            return [employee.get_details() for employee in self.employees]

company = Company("Hello World")
company.add_employees("Henry","HR")
company.add_employees("John","Manager")
company.add_employee("Jerry","software developer")

print(company.list_employees()) 