class Employee:
    def setWorkHours(self):
        self.workHours = 40

    def displayWorkHours(self):
        print ("Working hours = ",self.workHours)

class Trainee(Employee):
    def setWorkHours(self):
        self.workHours = 45

    def resetWorkHours(self):
        super().setWorkHours()

emp = Employee()
train = Trainee()
emp.setWorkHours()
emp.displayWorkHours()
train.setWorkHours()
train.displayWorkHours()
emp.workHours = 50
emp.displayWorkHours()
train.resetWorkHours()
emp.workHours = 50
train.displayWorkHours()
