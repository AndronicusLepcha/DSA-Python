   
class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def addNode(self,data):
        if self.data==data: # duplicate data is not allowed
            return

        if data<self.data:
            if self.left != None:
                self.left.addNode(data)
            else:
                self.left=Tree(data)

        if data>self.data:
            if self.right != None:
                self.right.addNode(data)
            else:
                self.right=Tree(data)

    def display(self,node): # inorder traversal
        if(node==None):
            return
        self.display(node.left);
        print(node.data);
        self.display(node.right)

    def treeHegiht(self,node):
        if node is None:
            return 0
        right=self.treeHegiht(node.right)
        left=self.treeHegiht(node.left)
        height=max(left,right)
        return height+1

    def removeRRcase(self,node):
        print("The node from which the rr case should be solved is "+str(node.data))
        x=node
        y=x.right
        z=y.right

        self.right=y
        y.left=x

    def isBalanced(self,node):
        if node is None:
            return 0
        left=self.treeHegiht(node.left)
        right=self.treeHegiht(node.right)
        print("Hegiht of left tree "+str(left))
        print("Hegiht of right tree "+str(right))

        if left-right < 1 or right-left < 1:
            #print("Need to remove")
            self.removeRRcase(node.right);
        
        return left+right
    
 
class RRcase:
    node=[1,0,3,4,5]
    root=Tree(node[0]);
    #addNode(l[0]);
    for x in range(1,len(node)): 
        root.addNode(node[x])
        
    root.display(root)
    print("Height of the tree is "+str(root.treeHegiht(root)))
    root.isBalanced(root)

