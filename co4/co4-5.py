#Create a class Publisher (name). Derive class Book from Publisher with attributes #title and author. Derive class Python from Book with attributes price and #no_of_pages. Write	a program that displays information about a Python book. Use #base class constructor invocation and method overriding.

class publisher:
	def __init__(self,name):
		self.name=name
		
class book(publisher):
	def __init__(self,name,title,author):
		super().__init__(name) 	
		self.title=title
		self.author=author 	
class python(book):
	def __init__(self,name,title,author,price,pageno):
		super().__init__(name,title,author)
		self.price=price
		self.pageno=pageno
	
	def display(self):
		print("\nBook details\n1)Name of the publisher: ",self.name,"\n2)Title of the Book : ",self.title,"\n3)Author of the book : ",self.author,"\n4)Price : ",self.price,"\n5)Page number : ",self.pageno)	
name=input("Enter the name of publisher : ")
title=input("Enter the title : ")
author=input("Enter the author name : ")
price=int(input("Enter the price : "))
pageno=int(input("Enter the page numbers : "))
b=python(name,title,author,price,pageno)
b.display()

