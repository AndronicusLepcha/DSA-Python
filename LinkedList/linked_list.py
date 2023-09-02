#operation 
#note: index for node start from 1 
#1.Create Node
#2.Insert Node at Begining
#3.Insert Node at Ending
#4.Insert Node at Any Position
#5.Delete Node at any Position 
#6.Display all the exisitng node
#7.Get the length of the Linked List
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.nextnode=None

    def create_node(self,data):
        node=Node(data,None)
        self.head=node
        self.nextnode=node
        # next=self.nextnode
        # print(next)

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        else:
            # itr=self.nextnode
            # while itr.next:
            #     itr=itr.next
            # itr.next=Node(data,None)
            next=self.nextnode
            print(next.data)

            node=Node(data,None)
            # print(next.data)
            next.next=node
            nextnode=node

    def get_length(self):
        itr=self.head
        len=0
        while itr is not None:
            itr=itr.next
            len=len+1
        return len

    def insert_at_anyposition(self):
        position=int(input('enter the postion to insert node'))
        #print(self.get_length())
        if position<=self.get_length():
            data=int(input("enter data"))
            index=1
            next = self.head
            while next is not None:
                temp1=next
                next=next.next
                index=index+1
                if index == position:
                    node=Node(data,next)
                    temp1.next=node
        else:
            print("Index out of range")

    def delete_at_anyposition(self):
        position=int(input('enter the postion to delete node'))
        if position == 1:
            self.head=self.head.next
            return
        #print(self.get_length())
        if position<=self.get_length():
            index=1
            next = self.head
            while next is not None:
                temp1=next
                next=next.next
                index=index+1
                if index == position:
                    temp1.next=next.next
        else:
            print("Index out of range")





    def print(self):
        if self.head is None:
            print('Lindked List is Empty')
            return 
        llist=''  # i will append in this as a string
        itr=self.head
        while itr is not None:
            llist += str(itr.data)+'-->'
            itr = itr.next

        print(llist)

if __name__ == '__main__':
    ll=LinkedList()
    ll.create_node(25)
    ll.insert_at_begining(90)
    ll.insert_at_begining(56)
    ll.insert_at_end(100)
    ll.print()
    ll.insert_at_anyposition()
    ll.print()
    ll.delete_at_anyposition()
    ll.print()