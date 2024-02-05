class Employee:
    count = 0

    def __init__(self, name, desig, salary):
        self.name = name
        self.desig = desig
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print("There are %d employees" % Employee.count)

    def displayDetails(self):
        print("Name:", self.name, ", Designation:", self.desig, ", Salary:", self.salary)


e1 = Employee("SAHIL", "Manager", 80000)
e2 = Employee("Johhny", "Team Leader", 50000)
e3 = Employee("SiyaRam", "Programmer", 30000)
e4 = Employee("Rohan", "Assistant", 25000)

print("Details of all employees:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()

e4.displayCount()
