from select import select


class Node:
    def __init__(self,next,data):
        self.next=next
        self.data=data

class LinkedList:
    def __init__(self,head):
        self.head=head
    def printList(self,node=None) ->None:
        if node==None:
            temp=self.head
        else:
            temp=node
        while temp:
            print(temp.data)
            temp=temp.next
    def addItem(self,data)->None:
        temp=temp.head
        while temp:
            temp=temp.next
        temp.next=Node(data=data)
    def deleteAtEnd(self):
        temp=self.head
        prev =temp
        while temp.next :
            prev=temp
            temp=temp.next
        prev.next=None
    def insertAfterkey(self,key,data):
        temp= self.head
        while temp.data!=key:
            if temp.next:
                temp=temp.next
            else:
                print("key not exist")
                return
        temp.next=Node(data=data,next=temp.next)
    


