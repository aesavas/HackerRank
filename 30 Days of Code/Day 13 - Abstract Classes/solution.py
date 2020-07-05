"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-abstract-classes/problem
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price
    
    def display(self):
        print("Title: {}\nAuthor: {}\nPrice: {}".format(self.title, self.author,self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()