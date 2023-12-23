import random
userInput = int(input("Enter the number:"))
var = random.randint(0,10)
if userInput>var:
    print("computer number is",var)
    print("you number is greater than var")
elif userInput<var:
    print("computer number is",var)
    print("your number is smaller than var")      

else:
    print("computer number is",var)
    print("Hurray you find it!")
                            


