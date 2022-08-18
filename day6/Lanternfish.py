
from requests import head


input='''2,5,5,3,2,2,5,1,4,5,2,1,5,5,1,2,3,3,4,1,4,1,4,4,2,1,5,5,3,5,4,3,4,1,5,4,1,5,5,5,4,3,1,2,1,5,1,4,4,1,4,1,3,1,1,1,3,1,1,2,1,3,1,1,1,2,3,5,5,3,2,3,3,2,2,1,3,1,3,1,5,5,1,2,3,2,1,1,2,1,2,1,2,2,1,3,5,4,3,3,2,2,3,1,4,2,2,1,3,4,5,4,2,5,4,1,2,1,3,5,3,3,5,4,1,1,5,2,4,4,1,2,2,5,5,3,1,2,4,3,3,1,4,2,5,1,5,1,2,1,1,1,1,3,5,5,1,5,5,1,2,2,1,2,1,2,1,2,1,4,5,1,2,4,3,3,3,1,5,3,2,2,1,4,2,4,2,3,2,5,1,5,1,1,1,3,1,1,3,5,4,2,5,3,2,2,1,4,5,1,3,2,5,1,2,1,4,1,5,5,1,2,2,1,2,4,5,3,3,1,4,4,3,1,4,2,4,4,3,4,1,4,5,3,1,4,2,2,3,4,4,4,1,4,3,1,3,4,5,1,5,4,4,4,5,5,5,2,1,3,4,3,2,5,3,1,3,2,2,3,1,4,5,3,5,5,3,2,3,1,2,5,2,1,3,1,1,1,5,1'''
fishes=list(map(int,input.split(",")))
class Node:
    def __init__(self,data,par) -> None:
        self.next=None
        self.data=data
        self.new=par


class Fish:


    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def insert(self,data)->None:
        if self.head==None:
            self.head=Node(data,False)
            self.tail=self.head
        else:
            temp=Node(data,False)
            self.tail.next=temp
            self.tail=self.tail.next
    def del_zero(self)->None:
        if self.head.data==0:
            self.head=self.head.next;
        else:
            temp1=self.head
            temp2=self.head.next
            while(temp2!=None):
                if temp2.data==0:
                    temp2=temp2.next
                    temp1.next=temp2
                    alpha=Node(8,True)
                    self.tail.next=alpha
                    self.tail=self.tail.next
                else:
                    temp1=temp1.next
                    temp2=temp2.next
    def remove_one(self)->None:
        
        temp=self.head
        while temp!=None:
            if temp.data==0:

                temp.data=6
                temp=temp.next
                alpha=Node(8,True)
                self.tail.next=alpha
                self.tail=self.tail.next
            else:
                if temp.new==True:
                    temp.new=False
                else:
                    temp.data=temp.data-1
                temp=temp.next
            
    def sum(self)->int:
        temp=self.head
        ans=0
        while(temp!=None):
            ans+=1
            temp=temp.next
        return ans



    def print(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"->",end=" ")
            temp=temp.next
        print()
arr=[1,2,3,4,0,2,4,5,6,0,5,6,0,3,1,0]

list=Fish()
for i in fishes:
    list.insert(i)

for i in range(1,81):
    list.remove_one()
print(list.sum())