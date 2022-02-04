from collections import deque
class TreeNode():
    def __init__(self,name):
        self.name=name
        self.connections=deque()
        self.parent=None

    def add_connection(self,node):
        node.parent=self
        self.connections.append(node)  

    def get_parent(self):
        return self.parent

    def __repr__(self):
        return f"class TreeNode(name: {self.name}, parent:{self.parent})"       

    def get_connections(self):
        print(f"connections of {self.name}")
        for conn in self.connections:
            space="    "
            print(f"{space}name: {conn.name}\n")
        return f"{self.name} has {len(self.connections)} connections"

    def get_level(self):
        level=0
        next=self.parent
        while(next):  
            level+=1
            next=next.parent
        return f"level of {self.name} is {level}"    

nitesh=TreeNode('nitesh')
terrorist=TreeNode("terrorist")
nitesh.add_connection(terrorist)
third=TreeNode("third")
terrorist.add_connection(third)
print(nitesh.get_level())
nitesh.add_connection(third)
print(terrorist.get_level())
print(third.get_level())
print(nitesh.get_connections())
