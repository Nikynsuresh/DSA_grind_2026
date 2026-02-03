class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def insert_at_pos(self,pos,data):
        new=Node(data)
        count=0
        temp=self.head
        if pos==0:
            new.next=self.head
            self.head=new
            return
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
            if temp is None:
                print("List out of index")
                return
        new.next=temp.next
        temp.next=new
    def delete_at_begining(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head=self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delete_at_pos(self,pos):
        if self.head is None:
            print("List is empty")
            return
        if pos==0:
            self.head=self.head.next
            return
        count=0
        temp=self.head
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
        if temp is None or temp.next is None:
            print("List out of index")
            return
        temp.next=temp.next.next
    def delete_by_val(self,val):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data==val:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next is not None:
            if temp.next.data==val:
                temp.next=temp.next.next
                return
            temp=temp.next
        print("List out of index")
    def length_of_list(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        print(count)
    def reverse_list(self):
        def reverse(node):
            if node is None or node.next is None:
                return node
            new=reverse(node.next)
            node.next.next=node
            node.next=None
            return new
        self.head=reverse(self.head)
            
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
l1=linkedlist()
l1.insert_at_begining(90)
l1.insert_at_begining(80)
l1.insert_at_begining(70)
l1.insert_at_end(60)
l1.insert_at_end(10)
l1.insert_at_pos(2,10)
l1.display()
l1.reverse_list()
l1.display()
