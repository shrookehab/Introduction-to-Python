empList = ["ahmed", "ali", "amr"]
SalList = [2000, 3000, 4000]

employee = input("please enter employee name: ")
isFound = False

for emp in empList:
	if employee == emp:
		isFound = True
		break
		
if isFound == True:
	print("The Salary of this employee = ", SalList[empList.index(employee)])
else:
	print("Employee not found")