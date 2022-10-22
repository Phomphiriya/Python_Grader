from multiprocessing.connection import answer_challenge
from turtle import circle


class BMI:
    def __init__ (self ,height = None ,weight = None):
        if height == None:
            self.height = "Empty"
        else:
            self.height = height
        if weight == None:
            self.weight = "Empty"
        else:
            self.weight = weight
    
    def getBMI(self):
        ans = self.weight/(self.height/100)**2
        return round(ans,2)
    
    def __str__(self):
        return "{} {}".format(self.height,self.weight)

height,weight = input("Enter H,W : ").split(",")
height,weight = int(height),int(weight)
cal = BMI(height,weight)

print(cal)
print(cal.getBMI())
