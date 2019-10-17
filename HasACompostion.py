class Engine:
	def __init__(self):
		self.power='128kw'
	def useEngine(self):
		print("Use car")

class Car:
	def __init__(self):
		self.engine=Engine()
	def useCar(self):
		self.engine.useEngine()
		print(self.engine.power)


c=Car()
c.useCar()
