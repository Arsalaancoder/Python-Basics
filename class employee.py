class Employee:
    company="microsoft"
    salary=100

Arsalaan=Employee()
chakri=Employee()
# Arsalaan.salary=900
# chakri.salary=800
print( Arsalaan.company)    
print(chakri.company)
Employee.company="google"
print(Arsalaan.company)    
print(chakri.company)
print(Arsalaan.salary)    
print(chakri.salary)