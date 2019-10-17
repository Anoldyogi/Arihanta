class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eat(self):
		print("eat biryani and drink beer")


class employee(person):
	def __init__(self,name,age,empno,sal):
		#self.name=name
		#self.age=age
		super().__init__(name,age)
		self.empno=empno
		self.sal=sal
	def work(self):
		print("employee working")
	def info(self):
		print(self.name)
		print(self.age)
		print(self.empno)
		print(self.sal)

e=employee("durga",23,114,'115k')
e.eat()
e.work()
e.info()
