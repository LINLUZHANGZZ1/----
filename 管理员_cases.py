class User():
	def __init__(self, first_name, last_name):
		self.first_name=first_name
		self.last_name=last_name



	def describe_user(self):
		print('该用户的姓名为'+self.first_name.title()+self.last_name.title()
			  +',该用户的其他信息为'+user_info.title())

	def greet_user(self):
		print("hello,"+self.first_name+self.last_name+" ,good morring!")
class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__( first_name, last_name)
		self.privileges=['can add post','can delete post','can ban user']
	def show_privileges(self):
		for i in self.privileges:
			print(i)

admin1=Admin('LIN','LU')
admin1.show_privileges()