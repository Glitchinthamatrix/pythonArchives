from collections import deque
class Queue:
    def __init__(self):
        self.container=deque()

    def add(self,data):
        self.container.append(data)  

    def getItem(self):
        print(f"the item is {self.container[0]}")    

    def mapQueue(self):
        for i in range(len(self.container)):
            print(self.container[i],end="=>")


newque=Queue()

for i in range(101):
    newque.add({"rank":f"{i}","data":f"i squared is {i*i}"})

newque.mapQueue()           