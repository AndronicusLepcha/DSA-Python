    # Intersection of Two Linked Lists:
    # Find the node where two linked lists intersect. If they don't intersect, return null.

    # Add Two Numbers Represented by Linked Lists:
    # Given two linked lists representing two non-negative numbers, where each node contains a single digit, add the two numbers and return it as a linked list.

    # Palindrome Linked List:
    # Check if a linked list is a palindrome.

    # LRU Cache with Linked List:
    # Implement an LRU (Least Recently Used) cache using a linked list.

    # Swap Nodes in Pairs:
    # Given a linked list, swap every two adjacent nodes and return the modified list.

    # Add Two Numbers as Linked Lists:
    # Given two numbers represented by linked lists, where each node contains a single digit, add the two numbers and return the result as a linked list.

    # Split Linked List:
    # Split a linked list into two lists, one containing even-indexed elements and the other containing odd-indexed elements.

    # Merge Sort for Linked Lists:
    # Implement the merge sort algorithm to sort a linked list.

    # Partition Linked List:
    # Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

    # Sort a Linked List Using Insertion Sort:
    # Sort a linked list using the insertion sort algorithm.

   

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.list=[]
        self.temp1=None

    def create_node(self,data):  #first node in the linked list
        node = Node(data,None)
        self.head=node
    
    def addNodeInStartIndex(self,data):
        node = Node(data,self.head)
        self.head=node

    def addNodeatLastIndex(self,data):
        itr=self.head
        while itr is not None:
            temp=itr
            itr = itr.next
            if itr is None:
                node = Node(data)
                temp.next=node

    def addNodeAtAnyIndex(self,data,pos):
        idx=0
        if pos == idx:
            self.addNodeInStartIndex(data)
        elif pos == self.LinkedListLength():
            self.addNodeatLastIndex(data)
        else:
            itr=self.head
            while itr is not None:
                idx += 1
                temp=itr
                itr=itr.next
                if idx == pos:
                    node = Node(data,itr)
                    temp.next=node
                    break

    def deleteNodeAtAnyIndex(self):
        self.printLinkedList()
        pos=int(input("Enter the index to delete the node "))
        if pos == 0:
            self.head=self.head.next

        if pos <= self.LinkedListLength():
            idx=0
            itr = self.head
            while itr is not None:
                idx += 1
                temp=itr
                itr=itr.next

                if idx == pos:
                    itr=itr.next
                    temp.next = itr
        else:
            raise IndexError()
    
    def LinkedListLength(self):
        length=0
        itr = self.head
        while itr is not None:
            length += 1
            itr=itr.next
        return length

    def printLinkedList(self):
        itr=self.head
        nodes=" "
        while itr is not None:
            nodes += str(itr.data)+"-->"
            itr=itr.next
        print(nodes)

    # Remove Duplicates from Sorted List:
    # Given a sorted linked list, delete all duplicates such that each element appears only once.
    def removeDuplicates(self):
        itr = self.head
        idx=0
        while itr is not None:
            if itr.data not in self.list:
                self.list.append(itr.data)
                idx += 1 
            else:
                print("Duplicate element found at index ",idx)
                self.deleteNodeAtAnyIndex()
            itr = itr.next

# Detect a Cycle:
#make cycle
#    def MakeCycle(self):
#         itr=self.head
#         while itr.next is not None:
#             temp=itr
#             itr=itr.next
#     #Make the last node point to the head to create a cycle   
#         itr.next=self.head
# Determine if a linked list has a cycle and find the starting point of the cycle if it exists.
    def detectCycle(self):
        tortoise = self.head
        hare = self.head
        while tortoise is not None and hare.next is not None:
            tortoise=tortoise.next
            hare=hare.next.next
            if tortoise ==  hare:
                print("Cycle Detected")
                return
        print("No Cycle detected")
           
 # Rotate Linked List:
 # Given a linked list, rotate it to the right by k places, where k is non-negative.
    def rotateLL(self):
        itr=self.head
        while itr.next is not None:
            temp=itr
            itr=itr.next
    #Make the last node point to the head to create a cycle   
        itr.next=self.head
     #update the head pointer to the new head (temp of next)
        self.head=temp.next
    # break the cycle
        temp.next = None   
                    



node=LinkedList()
node.create_node(100)
node.addNodeInStartIndex(99)
node.addNodeatLastIndex(101)
node.addNodeatLastIndex(101)
node.addNodeatLastIndex(101)
node.addNodeatLastIndex(101)
node.addNodeatLastIndex(101)
node.addNodeatLastIndex(400)
node.addNodeAtAnyIndex(80, 0)
node.addNodeAtAnyIndex(99, 4)
node.addNodeAtAnyIndex(800, 5)
node.deleteNodeAtAnyIndex()
node.removeDuplicates()
node.printLinkedList()
node.rotateLL()
node.detectCycle()
node.printLinkedList()
