class bank(object):
	def __init__(self):
		self.cash = 0

	def balance(self):
		print("Current balance is %d\n" % self.cash)
		menu()

	def deposit(self):
		try:
			self.deposit_ = int(input("\nDeposit cash: "))
		except Exception:
			pass
			self.deposit()
		self.cash = self.deposit_ + self.cash
		print "Success."
		self.balance()
		menu()

	def widraw(self):
		try:
			self.widraw_ = int(input("\nWidraw cash: "))
		except Exception:
			pass
			self.widraw()
		if(self.cash>=self.widraw_):
			self.cash = self.cash - self.widraw_
			print "Success."
			self.balance()
			menu()
		else:
			print "No cash."
			self.balance()
			menu()

o = bank()

def menu():
	print "1 Deposit\n2 Widraw\n3 Balance"
	try:
		choice = int(input(": "))
	except Exception:
		pass
		menu()
	if(choice==1):
		o.deposit()
	elif(choice==2):
		o.widraw()
	elif(choice==3):
		print ""
		o.balance()
	else:
		print "Wrong choice.\n"
		#print "Press 1 to go back to main menu: "
		#if(choice=1):
		menu()

print "Welcome to Skrrt ATM service."
menu()