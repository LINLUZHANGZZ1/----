class Restaurant():
	"""这里是表示一家餐馆的类"""
	def __init__(self,restaurant_name,cuisine_type):
		"""初始化属性name和type"""
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print("这家餐厅的名字是"+self.restaurant_name.title()+" 类型是"+self.cuisine_type.title()+"服务人数为"+self.number_served.title())

	def open_restaurant(self):
		print("这家餐馆正在营业")

	def set_number(self,number_served):
		self.number_served=number_served

	def increment_number_served(self,_increase_number):
		self.number_served += _increase_number
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['草莓味冰淇淋','西瓜味冰淇淋','酸奶味冰淇淋']

	def describe_flavor(self):
		for i in self.flavors:
			print(i)

if __name__ == '__main__':
	Restaurant1 = IceCreamStand('a','b')
	Restaurant1.describe_flavor()


