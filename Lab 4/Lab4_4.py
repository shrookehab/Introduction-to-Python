from tkinter import *


def RBtn_func():
	global Selected_RBtn
	print(Selected_RBtn.get())
	
def RBtn1_func():
	global Selected_RBtn1
	print(Selected_RBtn1.get())
	
def RBtn21_func():
	global Selected_RBtn21
	print(Selected_RBtn21.get())
	
def RBtn22_func():
	global Selected_RBtn22
	print(Selected_RBtn22.get())
	
def RBtn31_func():
	global Selected_RBtn31
	print(Selected_RBtn31.get())
	
def RBtn32_func():
	global Selected_RBtn32
	print(Selected_RBtn32.get())
	
def RBtn41_func():
	global Selected_RBtn41
	print(Selected_RBtn41.get())
	
def RBtn42_func():
	global Selected_RBtn42
	print(Selected_RBtn42.get())
	
def RBtn51_func():
	global Selected_RBtn51
	print(Selected_RBtn51.get())
	
def RBtn52_func():
	global Selected_RBtn52
	print(Selected_RBtn52.get())
	
def RBtn61_func():
	global Selected_RBtn61
	print(Selected_RBtn61.get())
	
def RBtn62_func():
	global Selected_RBtn62
	print(Selected_RBtn62.get())
	
def RBtn71_func():
	global Selected_RBtn71
	print(Selected_RBtn71.get())
	
def RBtn72_func():
	global Selected_RBtn72
	print(Selected_RBtn72.get())
	
def RBtn81_func():
	global Selected_RBtn81
	print(Selected_RBtn81.get())
	
def RBtn82_func():
	global Selected_RBtn82
	print(Selected_RBtn82.get())
	
def generatCode():
	binaryList = []

	if Selected_RBtn.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn1.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn21.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn22.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn31.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn32.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn41.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn42.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn51.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn52.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn61.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn62.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn71.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn72.get() == 1:
		binaryList.append(1)
		
	if Selected_RBtn81.get() == 1:
		binaryList.append(0)
	elif Selected_RBtn82.get() == 1:
		binaryList.append(1)

	binaryList.reverse()
	print(binaryList)

	filehandler = open("text.c", 'w')
	filehandler.write("void main(){\n")
	filehandler.write("\tDDRA = 0b")
	filehandler.flush()
	for i in binaryList:
		filehandler.write("{}".format(i))
		filehandler.flush()

	filehandler.write("\n}")

	filehandler.close()

root = Tk()  
root.geometry('500x300')  
root.title('Playing with Radio buttons')

Selected_RBtn = IntVar()
Selected_RBtn1 = IntVar()

bitLabel1 = Label(root, text="Pin 0 Mode").grid(row=0, column=0)
RButton = Radiobutton(root, text="input", command=RBtn_func, value=1, variable=Selected_RBtn).grid(row=0, column=1)
RButton = Radiobutton(root, text="output", command=RBtn1_func, value=1, variable=Selected_RBtn1).grid(row=0, column=2)

Selected_RBtn21 = IntVar()
Selected_RBtn22 = IntVar()

bitLabel2 = Label(root, text="Pin 1 Mode").grid(row=1, column=0)
RButton2 = Radiobutton(root, text="input", command=RBtn21_func, value=1, variable=Selected_RBtn21).grid(row=1, column=1)
RButton2 = Radiobutton(root, text="output", command=RBtn22_func, value=1, variable=Selected_RBtn22).grid(row=1, column=2)

	
Selected_RBtn31 = IntVar()
Selected_RBtn32 = IntVar()

bitLabel3 = Label(root, text="Pin 2 Mode").grid(row=2, column=0)
RButton3 = Radiobutton(root, text="input", command=RBtn31_func, value=1, variable=Selected_RBtn31).grid(row=2, column=1)
RButton3 = Radiobutton(root, text="output", command=RBtn32_func, value=1, variable=Selected_RBtn32).grid(row=2, column=2)


Selected_RBtn41 = IntVar()
Selected_RBtn42 = IntVar()

bitLabel4 = Label(root, text="Pin 3 Mode").grid(row=3, column=0)
RButton4 = Radiobutton(root, text="input", command=RBtn41_func, value=1, variable=Selected_RBtn41).grid(row=3, column=1)
RButton4 = Radiobutton(root, text="output", command=RBtn42_func, value=1, variable=Selected_RBtn42).grid(row=3, column=2)


Selected_RBtn51 = IntVar()
Selected_RBtn52 = IntVar()

bitLabel5 = Label(root, text="Pin 4 Mode").grid(row=4, column=0)
RButton5 = Radiobutton(root, text="input", command=RBtn51_func, value=1, variable=Selected_RBtn51).grid(row=4, column=1)
RButton5 = Radiobutton(root, text="output", command=RBtn52_func, value=1, variable=Selected_RBtn52).grid(row=4, column=2)


Selected_RBtn61 = IntVar()
Selected_RBtn62 = IntVar()

bitLabel6 = Label(root, text="Pin 5 Mode").grid(row=5, column=0)
RButton6 = Radiobutton(root, text="input", command=RBtn61_func, value=1, variable=Selected_RBtn61).grid(row=5, column=1)
RButton6 = Radiobutton(root, text="output", command=RBtn62_func, value=1, variable=Selected_RBtn62).grid(row=5, column=2)

	
Selected_RBtn71 = IntVar()
Selected_RBtn72 = IntVar()

bitLabel7 = Label(root, text="Pin 6 Mode").grid(row=6, column=0)
RButton7 = Radiobutton(root, text="input", command=RBtn71_func, value=1, variable=Selected_RBtn71).grid(row=6, column=1)
RButton7 = Radiobutton(root, text="output", command=RBtn72_func, value=1, variable=Selected_RBtn72).grid(row=6, column=2)
	
Selected_RBtn81 = IntVar()
Selected_RBtn82 = IntVar()

bitLabel8 = Label(root, text="Pin 7 Mode").grid(row=7, column=0)
RButton8 = Radiobutton(root, text="input", command=RBtn81_func, value=1, variable=Selected_RBtn81).grid(row=7, column=1)
RButton8 = Radiobutton(root, text="output", command=RBtn82_func, value=1, variable=Selected_RBtn82).grid(row=7, column=2)

Button1 = Button(root, text="Generate C Code", command=generatCode).grid(row=8, column=1)


root.mainloop()

