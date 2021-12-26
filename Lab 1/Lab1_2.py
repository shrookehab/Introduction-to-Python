'''
binaryNum = input("Enter 2-bit binary number: ")
count = 0
if len(binaryNum) == 2:
	num = int(binaryNum[0])
	num2 = int(binaryNum[1])
	if num == 0 and num2 == 0:
		print("number in decimal = ", 0)
	elif num == 0 and num2 == 1:
		print("number in decimal = ", 1)
	elif num == 1 and num2 == 0:
		print("number in decimal = ", 2)
	else:
		print("number in decimal = ", 3)
	
else:
	print("invalid input!!")
	
'''
binaryNum = input("Enter 2-bit binary number: ")
count = 0
if len(binaryNum) == 2:
	if binaryNum.count("0") == 2:
		print("number in decimal = ", 0)
	elif binaryNum.count("1") == 2:
		print("number in decimal = ", 3)
	else:
		num = binaryNum.index("1")
		if num == 0:
			count += 2
		if num == 1:
			count += 1
		print("number in decimal = ", count)

else:
	print("invalid input!!")
