class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp
    def insert_at_begining(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        new.next=self.head
        self.head.prev=new
        self.head=new
    def insert_at_pos(self,data,pos):
        new=Node(data)
        temp=self.head
        if pos==0:
            if self.head:
                new.next=self.head
                self.head.prev=new
            self.head=new
            return
        count=0
        while temp and count<pos-1:
            temp=temp.next
            count+=1
        if not temp:
            print("List out of index")
            return
        new.next=temp.next
        new.prev=temp
        if temp.next:
            temp.next=prev=new
        temp.next=new
        
            
            
            
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
l1=LinkedList()
l1.insert_at_end(90)
l1.insert_at_end(80)
l1.insert_at_begining(10)
l1.insert_at_pos(40,1)
l1.display()
