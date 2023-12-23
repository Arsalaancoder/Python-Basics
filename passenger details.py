#  class-template
# object-instance
# it is based on Dry-do not repeat
class Railwayform:
    formtype="Railwayform"
    a=input("Enter the name:")
    
    def data(self):
     print(f"Name = {self.Name}")
     print(f"CoachNo = {self.coachNo}")
     print(f"BerthNo = {self.BerthNo}")
     print(f"Train = {self.train}")
     print(f"Departurefrom = {self.Departurefrom}")
     print(f"Destination = {self.Destination}")
     print(f"Departuretime = {self.Departuretime}")
     print(f"Arrivaltime = {self.Arrivaltime}")


     
passengerdetails=Railwayform()  
passengerdetails.Name="Arsalaan"
passengerdetails.coachNo="S8"
passengerdetails.BerthNo="45"
passengerdetails.train="Simhapuri"
passengerdetails.Departurefrom="Secunderabad"
passengerdetails.Destination="Gudur"
passengerdetails.Departuretime="11:00 PM"
passengerdetails.Arrivaltime="9:00 AM"

passengerdetails.data()
