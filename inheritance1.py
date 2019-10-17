class p:
	def m1(self):
		print("parent class")

class c(p):
	def m2(self):
		print("child class")

c=c()
c.m2()
c.m1()
