def GET_LIST(decimalNum):
	binaryList = []
	while decimalNum != 0:
		binBit = decimalNum % 2
		binaryList.append(binBit)
		decimalNum = decimalNum // 2
		
	while len(binaryList) < 4:
		binaryList.append(0)
		
	binaryList.reverse()
	return binaryList

#'''
def SET_BIT(decimalNum, bitNum):
	newList = GET_LIST(decimalNum)
	newList.reverse()
	newList[bitNum] = 1
	newList.reverse()
	return newList

def CLR_BIT(decimalNum, bitNum):
	newList = GET_LIST(decimalNum)
	newList.reverse()
	newList[bitNum] = 0
	newList.reverse()
	return newList

def TOG_BIT(decimalNum, bitNum):
	newList = GET_LIST(decimalNum)
	newList.reverse()
	if newList[bitNum] == 0:
		newList[bitNum] = 1
	else:
		newList[bitNum] = 0
	newList.reverse()
	return newList

def GET_BIT(decimalNum, bitNum):
	newList = GET_LIST(decimalNum)
	newList.reverse()
	return newList[bitNum]
	
'''	
def SET_BIT(decimalNum, bitNum):
	return ((1 << bitNum) | decimalNum)

def CLR_BIT(decimalNum, bitNum):
	return ((~(1 << bitNum))& decimalNum)

def TOG_BIT(decimalNum, bitNum):
	return ((1 << bitNum) ^ decimalNum)

def GET_BIT(decimalNum, bitNum):
	return ((decimalNum >> bitNum ) & 1)
'''
