# Define a Employee class with attributes role,department & salary.Also create showDetails() method.
# Create an Engineer class that inherits properties from employee & also have attributes: name & age
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("name =", self.name)
        print("age =", self.age)
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Software Engineer", "IT", "Rs. 1,00,000")

engg1 = Engineer("Arnav Singh",29)        
engg1.showDetails()