from tkinter import *
from functools import partial


database = {"215321701332":["Ahmed Abdelrazek Mohamed", "1783", 3500166],
			"203659302214":["Salama Mohamed Foaad", "1390", 520001],
			"126355700193":["Adel Khaled Adelrahman", "1214", 111000], 
			"201455998011":["Saeed Amin Elsawy", "2001", 1200], 
			"201122369851":["Amir Salama Elgendy", "8935", 178933], 
			"201356788002":["Wael Mohamed Khairy", "3420", 55000], 
			"203366789564":["Mina Sameh Bishoy", "1179", 18000], 
			"201236787812":["Omnia Ahmed Awad", "1430", 180350]}
def _mainWindow(window):
	window.title('Main Window')
	toplevelLabel = Label(window, text="Welcome Shrook").grid(row=0, column=0)
	Button1 = Button(window, text="Close", command=window.destroy).grid(row=1, column=0)
	window.mainloop()

def Login(accountNum, password):
	isValid = False
	for item in database:
		if accountNum.get() == item:
			isValid = True
	if isValid == True and password.get() == str(database[accountNum][1]):
		window = Toplevel()
		window.title('Main Window')
		toplevelLabel = Label(window, text="Welcome Shrook").grid(row=0, column=0)
		Button1 = Button(window, text="Close", command=window.destroy).grid(row=1, column=0)
		window.mainloop()
		
	if isValid == False:
		window = Toplevel()
		window.title('Welcome')
		toplevelLabel = Label(window, text="Wrong Input").grid(row=0, column=0)
		Button1 = Button(window, text="Close", command=window.destroy).grid(row=1, column=0)
		window.mainloop()
			

root = Tk()  
root.geometry('250x150')  
root.title('User Bank Account :)')

accountNumLabel = Label(root, text="Account Number").grid(row=0, column=0)
accountNum = StringVar()
accountNumEntry = Entry(root, textvariable=accountNum).grid(row=0, column=1)  

passwordLabel = Label(root,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)  

LoginCommand = partial(Login, accountNum, password)
loginButton = Button(root, text="Login", command=LoginCommand).grid(row=5, column=1)  

root.mainloop()