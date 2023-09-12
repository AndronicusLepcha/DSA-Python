class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def addChild(self,data):
        if data==self.data:
            return
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinarySearchTree(data)

    def inorderTraversal(self):
        elements=[]
        #visit left tree
        if self.left:
            elements += self.left.inorderTraversal()
        
        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.inorderTraversal()

        return elements


def buildTree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,18,34]
    numbers_tree = buildTree(numbers)  
    print((numbers_tree.inorderTraversal())) 
