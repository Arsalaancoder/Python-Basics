class Student:
    name="Arsalaan"

    def __init__(self, Name,Age,School,TenhtGpa):
     self.Name=Name
     self.Age=Age
     self.School=School
     self.TenhtGpa=TenhtGpa

    def std(self):
        print(f"Name = {self.Name}")
        print(f"Age = {self.Age}")
        print(f"School = {self.School}")
        print(f"Tenth GPA = {self.TenhtGpa}")

Arsalaan = Student('Arsalaan','16','sri chaitanaya','10.0')
Arsalaan.std()

