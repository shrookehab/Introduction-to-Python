username = "ahmed"
password = "123"

username1 = "omar"
password1 = "456"

username2 = "ali"
password2 = "789"

for i in range(0,3):
	input1 = (input("Enter your name: ")).lower()
	if input1 == username or input1 == username1 or input1 == username2:
		input2 = input("Enter your password: ")
		if input1 == username and input2 == password:
			print("Welcome ahmed")
			break
			
		elif input1 == username1 and input2 == password1:
			print("Welcome omar")
			break

		elif input1 == username2 and input2 == password2:
			print("Welcome ali")
			break
			
		else :
			if i == 2:
				print("invalid password")
			else:
				print("invalid password please Try again")
				print("")
			
	else:
		if i == 2:
			print("invalid name")
		else:	
			print("invalid name please Try again")
			print("")