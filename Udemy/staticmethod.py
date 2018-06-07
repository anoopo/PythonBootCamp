class Employee:
    def employeeDetails(self):
        self.name = "Anoop"

    @staticmethod
    def welcomeMessage():
        print ("Welcome")

employee = Employee()
employee.employeeDetails()
employee.welcomeMessage()
