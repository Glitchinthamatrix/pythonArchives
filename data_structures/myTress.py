class TreeNode():
    def __init__(self,name,data):
        self.name=name
        self.data=data
        self.children=[]
        self.parent=None

    def get_name(self):
        return self.name
        
    def print_self(self):
        print(f"name: {self.name}")
        print("no parent" if self.parent==None else self.parent.name)
        print(f"data: {self.data}")
        print(f"children: {self.children}")
    
    def has_child(self):
        return False if len(self.children)>0 else True
    
    def print_children(self):
        if(len(self.children)<1):
            print("this node has no children")
        else:
            for index,child in enumerate(self.children):
                print(f"{index+1}: {child.name}")

    def get_parent(self):
        print(f"parent of {self.name} is {self.parent}")

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level=0
        p=self.parent
        if p:
            level+=1
            p=p.parent
        return level    


rohan=TreeNode("rohan",78)
rohanJr=TreeNode("rohanJr",78)
rohanJrII=TreeNode("rohanJrII",78)
rohanJrIII=TreeNode("rohanJrIII",78)
rohan.add_child(rohanJr)
rohanJr.add_child(rohanJrII)
rohanJrII.add_child(rohanJrIII)
rohanJrIII.get_parent()
rohanJrII.get_parent()            
rohanJr.get_parent()
rohan.get_parent()