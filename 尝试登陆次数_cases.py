class User():
	def __init__(self, first_name, last_name):
		self.first_name=first_name
		self.last_name=last_name
		self.login_attempts=0
	def describe_user(self):
		print('该用户的姓名为'+self.first_name+self.last_name)
	def greet_user(self):
		print("hello,"+self.first_name+self.last_name+" ,good morring!")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0
user1 =User('a','b')

for m in range(5):
	user1.increment_login_attempts()

print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
