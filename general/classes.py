class Person:
    def __init__(self,name,age,height,weight):
        # the constructor function
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def printAge(self):
        #the self keyword holds all the properties of the class instances
        #method that prints age
        print(f"my age is {self.age}")
    def describe(self):
        #method that describes the instance
        print(f"hello there, my name is {self.name} and i'm {self.age} years old, my weight/height ratio is {abs(self.weight/self.height)}")    

p1=Person("nitesh",19,6,70)
print("programme running...")
p1.describe() 

