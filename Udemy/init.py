class Employee:
    def __init__(self,name):
        self.name = name
    def employeeDetails(self):
        print ("Welcome", self.name)

emp1 = Employee("Anoop")
emp2 = Employee("AnoopO")
emp1.employeeDetails()
emp2.employeeDetails()
