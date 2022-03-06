Employee = {}
while True:
	print("==================================")
	print("To Add New Employee press 1")
	print("To Print Employee Data press 2")
	print("To Delete Employee press 3")
	print("To exit press 4")
	print("==================================")
	print("")
	option = input("please enter your choice: ")
	print("")
	print("==================================")
	if option == "1":
		id = input("please enter Employee id: ")
		name = input("please enter Employee name: ")
		job = input("please enter Employee job: ")
		salary = int(input("please enter Employee salary: "))
		Employee[id] = [name, job, salary]
	elif option == "2":
		printid = input("please enter Employee id you want to print: ")
		print("The id = ", printid)
		print("The Employee name = ", Employee[printid][0])
		print("The Employee job = ", Employee[printid][1])
		print("The Employee salary = ", Employee[printid][2])
		#Employee.items()
	elif option == "3":
		delid = input("please enter Employee id you want to delete: ")
		Employee.pop(delid)
	else:
		break