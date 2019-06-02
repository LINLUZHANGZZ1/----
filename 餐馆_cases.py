class Restaurant():
	"""这里是表示一家餐馆的类"""
	def __init__(self,restaurant_name,cuisine_type):
		"""初始化属性name和type"""
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print("这家餐厅的名字是"+self.restaurant_name.title()+" 类型是"+self.cuisine_type.title())

	def open_restaurant(self):
		print("这家餐馆正在营业")
restaurant1=Restaurant('KFC','快餐店')
restaurant2=Restaurant('田野餐厅','中式快餐店')
print('餐厅名字是'+restaurant1.restaurant_name.title()+','+'类型是'+restaurant1.cuisine_type.title())
print('餐厅名字是'+restaurant2.restaurant_name.title()+','+'类型是'+restaurant2.cuisine_type.title())