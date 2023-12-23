class Employee:
    company="Microsoft"
    salary="3.5 LPA" # whwn there are no instance attributes it will check in the class and then it will print that 

Arsalaan=Employee()
ramesh=Employee()
# Arsalaan.salary="1.5 LPA"  if there is an instance attribute then it will print that 
# ramesh.salary="1.5 LPA"
Employee.company="Amazon"
print(Arsalaan.company)
print(ramesh.company)
# creating a inatance attribute saalry for both the objects
print(Arsalaan.salary)
print(ramesh.salary)

