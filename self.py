class Employee:
    company="microsoft"
    def getsalary(self):
        print(f"salary is {self.salary}\n and company is {self.company}\n and the age of the Employee is {self.Age}")

Arsalaan=Employee() 
Arsalaan.salary=450000
Arsalaan.Age=18
Arsalaan.getsalary ()   # self is internally changed into Employee.getsalary()
