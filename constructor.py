class Employee:
    company="microsoft"

    def  __init__(self, name,salary,department): # it will run automatically we can call it as a constructor because it initialize the
     self.name=name
     self.salary=salary
     self.department=department
     print("hello")
    def getdetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the department of the employee is {self.department}")
         
arsalaan=Employee("arsalaan",2000,"supporting")    
arsalaan.getdetails()       