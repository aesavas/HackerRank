"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        """
            counterNode = it travels on linked list for duplicate data.
            currentNode = it shows actual node to compare counterNode
        """
        if head != None:
            currentNode = head
            if(currentNode.next): 
                counterNode = currentNode.next
                while(currentNode):
                    if(counterNode):
                        if(currentNode.data == counterNode.data):     
                            currentNode.next = None #If there are duplicate data, we cut connection between them.
                        else:
                            currentNodenext = counterNode # If there is no duplite, we connect again two nodes.
                            currentNode = currentNode.next
                        counterNode = counterNode.next
                    else:
                        break
        return head

            

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 