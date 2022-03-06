
binaryList = []


for i in range(0, 8):
	str = input("Please enter Bit {bit} mode: ".format(bit = i))
	if str == "input":
		binaryList.append(0)
	if str == "output":
		binaryList.append(1)

binaryList.reverse()
print(binaryList)


filehandler = open("text.txt", 'w')
filehandler.write("DDRA=0b")
filehandler.flush()
for i in binaryList:
	filehandler.write("{}".format(i))
	filehandler.flush()


filehandler.close()
	
