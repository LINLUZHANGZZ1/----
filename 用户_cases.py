class User():
	def __init__(self, first_name, last_name,**user_info):
		self.first_name=first_name
		self.last_name=last_name
		for uses in user_info:
			user_info=user_info


	def describe_user(self):
		print('该用户的姓名为'+self.first_name.title()+self.last_name.title()
			  +',该用户的其他信息为'+user_info.title())

	def greet_user(self):
		print("hello,"+self.first_name+self.last_name+" ,good morring!")

user1=User('LIN','LUZHANG',AAAA='BBB')
print("该用户的姓名为"+user1.first_name.title()+user1.last_name.title())
user1.greet_user()
user1.describe_user()

