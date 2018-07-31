#!/usr/bin/env python3


from abc import ABCMeta, abstractmethod


# Given Book class
class Book(object, metaclass=ABCMeta):
	def __init__(self,title,author):
		self.title=title
		self.author=author
	@abstractmethod
	def display():
		pass

# MyBook class
class MyBook(Book):
	price = 0
	def __init__(self, title, author, price):
		super(Book, self).__init__()
		self.price = price
	def display(self):
		print("Title: " + title)
		print("Author: " + author)
		print("Price: " + str(price))


if __name__ == "__main__":
	title = input()
	author = input()
	price = int(input())
	new_novel = MyBook(title,author,price)
	new_novel.display()
