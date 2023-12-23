class Employee:
      
      def  __init__(self,Name,Age,From,Profisnality,Company,Salary):
        self.Name=Name
        self.Age=Age
        self.From=From
        self.profisnality=Profisnality
        self.Company=Company
        self.Salary=Salary
      def getfrom(self):
        print(f"Name = {self.Name}")
        print(f"Age = {self.Age}")
        print(f"From = {self.From}")
        print(f"Profisnality = {self.profisnality}")
        print(f"Company = {self.Company}")
        print(f"Salary = {self.Salary}")

        

Arsalaan=Employee("Arsalaan",18,"Hyderabad","Python & Web Developer","Microsoft","9.8 LPA")
Arsalaan.getfrom()