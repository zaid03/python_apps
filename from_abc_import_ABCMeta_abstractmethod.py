from abc import ABCMeta, abstractmethod

# Provided abstract Book class
class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @abstractmethod
    def display():
        pass

# Derived MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)  # Call the parent class (Book) constructor
        self.price = price

    def display(self):
        # Print the details in the required format
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

# Taking inputs and creating an instance of MyBook
title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
