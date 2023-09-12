class BST:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
    def addChild(self,data):
        if data==self.data:
            return
        if data > self.data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BST(data)

        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BST(data)

    def inorderTraversal(self):
        elements=[]

        if self.left:
            elements += self.left.inorderTraversal()

        elements.append(self.data) #base node
        
        if self.right:
            elements += self.right.inorderTraversal()
        
        return elements
    
    def search(self,key):
        if key==self.data:
            print("Key is found")
            return
        
        if key<self.data:
            
            if self.left:
                print("I am going left")
                self.left.search(key)
            else:
                print("Key not found")

        if key>self.data:
            if self.right:
                print("I am going right")
                self.right.search(key)
            else:
                print("Key not Found")

        


if __name__ == '__main__':
    l=[17,34,65,15,13,90,6]
    root=BST(l[0])
    root.addChild(17)
    for i in range(1,len(l)):
       root.addChild(l[i])
    print(root.inorderTraversal())
    root.search(90)