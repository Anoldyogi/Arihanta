class p:
	a=10
	def __init__(self):
		print(p.a)
		print("parent constructor")

	def m1(self):
		print("parent instance method")
	@classmethod
	def m2(cls):
		print("parent class method")
	@staticmethod
	def m3():
		print("parent static method")

class c(p):
	pass

c=c()
print()
c.m1()
c.m2()
c.m3()
print(c.a)
