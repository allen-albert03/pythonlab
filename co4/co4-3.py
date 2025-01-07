class rectangle:
	def __init__(self,length,width):
		self.__length=length
		self.__width=width
		
	def area(self):
		return self.__length*self.__width
	
	def __lt__(self,other):
		return self.area() < other.area() 
print("\nRectangle1\n")
length=int(input("Enter the length: "))
width=int(input("Enter the width : "))		
rect1=rectangle(length,width)
print("The area is: ",rect1.area())
print("\nRectangle2\n")
length=int(input("Enter the length: "))
width=int(input("Enter the width : "))
rect2=rectangle(length,width)
print("The area is: ",rect2.area())
if(rect1<rect2):
	print("area of rectangle1 is smaller than area of rectangle2")
elif(rect1>rect2):
	print("area of rectangle1 is larger than area of rectangle2")
else:
	print("Both rectangles have same area")
