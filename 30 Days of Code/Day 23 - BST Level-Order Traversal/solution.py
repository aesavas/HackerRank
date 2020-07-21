"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-binary-trees/problem
"""
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):

        
        if root != None:
            queue = [root]
            while(len(queue) != 0):
                print(queue[0].data, end=" ")
                if(queue[0].left != None):
                    queue.append(queue[0].left)
                if(queue[0].right != None):
                    queue.append(queue[0].right)
                queue.pop(0) # Because we jump next Node, we delete that we used Node.
                
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
