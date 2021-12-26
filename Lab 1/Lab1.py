
'''
username = "ahmed,omar,ali"
password = "123,456,789"
'''
username = "ahmed"
password = "123"

username1 = "omar"
password1 = "456"

username2 = "ali"
password2 = "789"

input1 = (input("Enter your name: ")).lower()
if input1 == username or input1 == username1 or input1 == username2:
	input2 = input("Enter your password: ")
	if input1 == username and input2 == password:
		print("Welcome ahmed")
		
	elif input1 == username1 and input2 == password1:
		print("Welcome omar")

	elif input1 == username2 and input2 == password2:
		print("Welcome ali")
		
	else :
		print("invalid password")
		
else:
	print("invalid name")
