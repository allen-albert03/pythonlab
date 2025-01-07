#create bank acc const and methods at the bank to widraw and retrive money
class bank:
	def __init__(self,acc_no,name,typ,bal):
		self.acc_no=acc_no
		self.name=name
		self.typ=typ
		self.bal=bal
	
	def deposit(self,amt):
		if(amt>0):
			self.bal=self.bal+amt
			print("Successfully deposited")
		else:
			print("Invalid amount")
	
	def withdraw(self,amt):
		if(amt>self.bal):
			print("Insufficent")	
		else:
			self.bal=self.bal-amt
			print("successfully withdrawn")
		
	def current_bal(self):
		print("Your balance is: ",self.bal)
	
	def viewdetails(self):
		print("Your account number is : ",self.acc_no)
		print("Your name is : ",self.name)
		print("Type of account : ",self.typ)
		print("Balance is : ",self.bal)
acc_no=int(input("Enter the account number: "))
name=input("Enter the name: ")
typ=input("Enter the type of account: ")
bal=int(input("Enter the balance"))
c1=bank(acc_no,name,typ,bal)
while True:
	print("Menu\n 1-Deposit \n 2-Withdraw \n 3-Current balance \n4-View details \n 5-Exit")	
	ch=int(input("Enter your choice : "))
	if(ch==1):
		amt=int(input("Enter the amount to be deposted: "))
		c1.deposit(amt)
	elif(ch==2):
		amt=int(input("Enter the amount to be withdrawn: "))
		c1.withdraw(amt)
	elif(ch==3):
		c1.current_bal()
	elif(ch==4):
		c1.viewdetails()
	elif(ch==5):
		break
	else:
		print("Invalid choice")
