class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class ListNode:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,data):
        if self.head==None:
            node=Node(data)
            self.head=node
            self.tail=node
        else:
            node=Node(data)
            self.tail.next=node
            self.tail=node

    def displayNode(self):
        temp=self.head
        print("head")
        while temp!=None:
            print("-->",temp.data)
            temp=temp.next
class LL:
    ll=ListNode()
    ll.addNode(100)
    ll.addNode(200)
    ll.addNode(202)
    ll.displayNode()            