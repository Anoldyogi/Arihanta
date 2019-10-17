class car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color

	def getCarInfo(self):
		print("Name of car is {}, name of model is {} and colro of car is {} ".format(self.name,self.model,self.color))

class employee:
	def __init__(self,name,eno,car):
		self.name=name
		self.eno=eno
		self.car=car
	def getEmployeeInfo(self):
		print("employee name is" , self.name)
		print("eno name is" , self.eno)
		print("below is the car info")
		self.car.getCarInfo()

c=car('ford',"v02","blue")
e=employee("Durga",101,c)
e.getEmployeeInfo()
