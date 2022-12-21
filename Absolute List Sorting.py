#User function Template for python3

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    
    def sortList(self,head):
        lst=[]
        curr=head
        while curr:
            lst.append(curr.data)
            curr=curr.next
        lst.sort()
        curr=head
        for ele in lst:
            curr.data=ele
            curr=curr.next
        return head
        
        pass
