class treeNode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.childern=[]

    def addChild(self,child):
        #child.data=data
        child.parent=self
        self.childern.append(child)

    def getLevel(self):
        index=0
        p=self.parent
        while p:
            index += 1
            p=p.parent
        return index

    def showTree(self):
        spaces= " "*self.getLevel()*3
        prefix = spaces +"|__"

        if self.getLevel() !=0:
            print(prefix+self.data)
            for child in self.childern:
                #print(child.data)
                child.showTree()
        
        else:
            print(self.data)
            for child in self.childern:
                    #print(child.data)
                child.showTree()

def createTree():
    root = treeNode("Electronic")

    tv = treeNode("TV")
    tv.addChild(treeNode("LG"))
    tv.addChild(treeNode("SAMSUNG"))

    phone = treeNode("PHONE")
    phone.addChild(treeNode("iphone"))
    phone.addChild(treeNode("oppo"))

    root.addChild(tv)
    root.addChild(phone)
    root.showTree()

createTree()
    
