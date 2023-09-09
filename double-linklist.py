class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
        
class MyLinkedList:

    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        

    def get(self, index: int) -> int:
        curr=self.head.next

        while curr and index>0:
            curr=curr.next
            index-=1
        
        
        if curr and curr!=self.tail and index==0:
            return curr.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        next=self.head.next
        prev=self.head
        next.prev=new_node
        prev.next=new_node
        new_node.next=next
        new_node.prev=prev
        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        next=self.tail
        prev=self.tail.prev
        next.prev=new_node
        prev.next=new_node
        new_node.next=next
        new_node.prev=prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.head.next
        while curr and index>0:
            curr=curr.next
            index -=1
        
        if curr and index==0:
            new_node=Node(val)
            next=curr
            prev=curr.prev
            next.prev=new_node
            prev.next=new_node
            new_node.next=next
            new_node.prev=prev

        

    def deleteAtIndex(self, index: int) -> None:
        curr=self.head.next
        while curr and index>0:
            curr=curr.next
            index -=1
        
        if curr and curr!=self.tail and index==0:
            next=curr.next
            prev=curr.prev
            next.prev=prev
            prev.next=next