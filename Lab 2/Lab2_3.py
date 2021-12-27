import bit_math_op

binNum = int(input("Please Enter decimal number: "))
bit = int(input("Please Enter the bit you want: "))

#print("The binary befor operations is: ",bit_math_op.GET_LIST(binNum))

#'''
#==============================using binary=================================

print("SET_BIT: ",bit_math_op.SET_BIT(binNum, bit))

print("CLR_BIT: ",bit_math_op.CLR_BIT(binNum, bit))

print("TOG_BIT: ",bit_math_op.TOG_BIT(binNum, bit))

print("GET_BIT: ",bit_math_op.GET_BIT(binNum, bit))
print("The binary after operations is: ",bit_math_op.GET_LIST(binNum))

#===========================================================================
#'''
'''
#==============================using decimal================================

binaryNum = bit_math_op.SET_BIT(binNum, bit)
print("SET_BIT: ", binaryNum)

binaryNum = bit_math_op.CLR_BIT(binNum, bit)
print("CLR_BIT: ", binaryNum)

binaryNum = bit_math_op.TOG_BIT(binNum, bit)
print("TOG_BIT: ", binaryNum)

binaryNum = bit_math_op.GET_BIT(binNum, bit)
print("GET_BIT: ", binaryNum)

print("The binary after operations is: ",bit_math_op.GET_LIST(binaryNum))
#===========================================================================

'''


