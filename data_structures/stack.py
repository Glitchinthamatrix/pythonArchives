from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def insert(self,data):
        self.container.append(data)

    def getItem(self):
        print(self.container.pop())   

    def getLength(self):
        counter=0
        length=len(self.container)
        for i in range(length):
            counter+=1
        print(f"length is {counter}")    

newStack= Stack()

for i in range(20):
    print(f"inserting {i}")
    newStack.insert(i+1)

newStack.getLength()
newStack.getItem()