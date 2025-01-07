class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width
		
	def displayarea(self):
		area=(self.length)*(self.width)
		return area
	def displayperi(self):
		print("Perimeter is : ",2*(self.length+self.width))
length=int(input("Enter the length: "))
width=int(input("Enter the width: "))
rect1=Rectangle(length,width)
a1=rect1.displayarea()
print("Area is : ",a1)
rect1.displayperi()
length=int(input("Enter the length: "))
width=int(input("Enter the width: "))
rect2=Rectangle(length,width)
a2=rect2.displayarea()
print("Area is : ",a2)
rect2.displayperi()
if a1 > a2:
	print("First rectangle is greater")
elif a1 == a2:
	print("Both area is same")
else:
	print("Second area is greater")

