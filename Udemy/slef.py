class Employee(object):
    age = 30
    def employeeDetails(self, name):
        self.name = name

    def printEmployeeDetails(self, name):
        print ("Inside the second function")
        print ("Name = ", self.name)
        print ("Age = ", Employee.age)

employeeOne = Employee()
employeeOne.employeeDetails("Anoop")
employeeOne.printEmployeeDetails("Anoop")
print (employeeOne.age)
