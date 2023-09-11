class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        self.nextnode=None

    def createNode(self,data):
        data=Node(data)
        self.head=data
        self.nextnode=node

    def addNodeAtStartingIndex(self,data):
        #print(self.head.data)
        data=Node(data,self.head)
        self.head=data
        #print(self.head.data)
        self.nextnode=data
        #print(self.head.next)
    def addNodeInLast(self,data):
        data=Node(data)
        itr = self.nextnode
        while itr.next is not None:
            itr = itr.next
        itr.next=data
        self.nextnode=self.head
    
    def insert_at_anyposition(self,pos,data):
        #data=Node(data)
        idx=0
        itr=self.nextnode
        while itr is not None:
            temp=itr
            itr = itr.next
            idx += 1
            if idx == pos:
                data=Node(data,itr)
                temp.next=data
                print(temp.data)
                break

    def delete(self,data):
        itr= self.nextnode
        #print(itr.data)
        while itr is not None:
            temp = itr
            itr = itr.next
            print(temp.data)
            if itr.data == data:
                itr=itr.next
                temp.next=itr
                break
                

    def display(self):
        nodes=""
        itr=self.head
        while itr is not None:
            #print(str(self.head.data)+"-->")
            nodes += str(itr.data)+"-->"
            itr = itr.next
        #nodes += str(itr.data)+"-->"
        print(nodes)

node=LinkedList()
node.createNode(100)
node.addNodeAtStartingIndex(90)
node.addNodeAtStartingIndex(40)
node.addNodeInLast(99)
node.insert_at_anyposition(2, 77)
node.display()
node.delete(100)
node.display()