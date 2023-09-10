
# Priniting tree like this 
# Electronics
#    |__Tv
#       |__Samsung
#       |__LG
#    |__Laptop
#       |__macbook
#       |__lenovo

class treeNode:
    def __init__(self,data):
        self.data=data
        self.childern=[]
        self.parent=None

    def add_child(self,child):
        child.parent = self # new node parent field will point to the curent object only
        self.childern.append(child)

    def print_tree(self):
        spaces = " " * self.get_level()*3
        prefix = spaces + "|__" if self.parent else "" #ternary opertor 
        print(prefix+ self.data)
        for child in self.childern:
            child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p=p.parent
        return level


def buildTree():
    root = treeNode("Electronics")

    tv = treeNode("Tv")
    tv.add_child(treeNode("Samsung"))
    tv.add_child(treeNode("LG"))

    laptop = treeNode("Laptop")
    laptop.add_child(treeNode("macbook"))
    laptop.add_child(treeNode("lenovo"))
    
    
    root.add_child(tv)
    root.add_child(laptop)
    root.print_tree()


buildTree()