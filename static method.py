class employee:
    company="microsoft"

    def getsalary(self, signature):
        print(f"salary is {self.salary}and company is {self.company}and the age of the Employee is {self.Age} \n {signature}")
    @staticmethod
    def greet(): # when we want to run the function without using self we use @static method
            print("good morning")
            print("how are you")
    @staticmethod # we cn add no.of static methods
    def time():
        
        print("the time is 10pm in the night")
           

Arsalaan=employee() 
Arsalaan.salary=450000
Arsalaan.Age=18
Arsalaan.getsalary("thanks!") # the message is added in the signsture we pass in the getsalary() function
Arsalaan.greet()
Arsalaan.time()
