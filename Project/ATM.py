#******************************************************************#
#		Name: Shrook Ehab Attia									   #
#		Track: AI-Nasr City										   #
#		FileName: ATM Project									   #
#		Version: VER1											   #
#																   #
#******************************************************************#


import tkinter
import tkinter as tk

nomOfTrials = {"215321701332": 0,
				"203659302214": 0,
				"126355700193": 0,
				"201455998011": 0,
				"201122369851": 0,
				"201356788002": 0,
				"203366789564": 0,
				"201236787812": 0}

database = {"215321701332": {"Name": "Ahmed Abdelrazek Mohamed", "Password": "1783", "Balance": "3500166"},
            "203659302214": {"Name": "Salma Mohamed Foaad", "Password": "1390", "Balance": "520001"},
            "126355700193": {"Name": "Adel Khaled Abdelrahman", "Password": "1214", "Balance": "111000"},
            "201455998011": {"Name": "Saeed Amin Elsawy", "Password": "2001", "Balance": "1200"},
            "201122369851": {"Name": "Amir Salama Elgendy", "Password": "8935", "Balance": "178933"},
            "201356788002": {"Name": "Wael Mohamed Khairy", "Password": "3420", "Balance": "55000"},
            "203366789564": {"Name": "Mina Sameh Bishoy", "Password": "1179", "Balance": "18000"},
            "201236787812": {"Name": "Omnia Ahmed Awad", "Password": "1430", "Balance": "180350"}}


currentAccount = ""


def rechargeWindow():
	global main
	main.destroy()
	main = windowRecharge()
	
	main.mainloop()
	
def mainWindow():
    global main
    main.destroy()
    main = windowSwitch()
	
    main.mainloop()

def pop_upWindow(mssage, title="Bank Message"):
	global main
	top = tk.Toplevel(main)
	top.geometry("250x85+500+300")
	top.title(title)
	lab = tk.Label(top, text=mssage).grid(row=0, column=0)
	tk.Button(top, text="OK", command=lambda: top.destroy(), width=20, height=1, bg="red").grid(row=1, column=0)
    
	top.mainloop()

def btnValidateAccount(accountNO):
    global main, currentAccount
    if accountNO in database.keys():
        currentAccount = accountNO
        main.destroy()
        main = windowPassword()
        main.mainloop()
    else:
        pop_upWindow("Invalid Account, Please Try again later!!")


def btnValidatePassword(accountPassword):
	global main, currentAccount
	if nomOfTrials[currentAccount] < 3:
		if accountPassword == database[currentAccount]["Password"]:
			main.destroy()
			main = windowSwitch()
			main.mainloop()
		else:
			nomOfTrials[currentAccount] += 1
			if nomOfTrials[currentAccount] <= 3:
				pop_upWindow('Invalid Password, please try again\nThe num of Trials left ' + str(3 - nomOfTrials[currentAccount]))
	else:
		pop_upWindow("You have Reached the Maximum num of Trials")


def btnChangePassword(newPassword):
    global main, currentAccount
    database[currentAccount]['Password'] = newPassword
    main.destroy()
    main = windowMessage("Password has been changed successfully :)")
    main.mainloop()


def btnValidateAmount(enteredAmount):
    global main, currentAccount
    if enteredAmount.isdigit():
        if float(enteredAmount) <= 5000.0:
            if float(enteredAmount) % 100 == 0:
                if float(enteredAmount) <= float(database[currentAccount]["Balance"]):
                    database[currentAccount]["Balance"] = str(float(database[currentAccount]["Balance"]) - float(enteredAmount))
                    main.destroy()
                    main = windowMessage()
                    main.mainloop()
                else:
                    pop_upWindow("There is no enough balance in your Account")
            else:
                pop_upWindow("Only allow amount that are multiple of 100.0")
        else:
            pop_upWindow("The maximum value/transaction is 5000.0\nTry again later!!!")
    else:
        pop_upWindow("Invalid Input!!!\nMust be digits")



def btnFawryRecharge(enteredAmount):
    global main, currentAccount
    if enteredAmount.isdigit():
        if float(enteredAmount) <= 5000.0:
            if float(enteredAmount) <= float(database[currentAccount]["Balance"]):
                database[currentAccount]["Balance"] = str(float(database[currentAccount]["Balance"]) - float(enteredAmount))
                main.destroy()
                main = windowMessage()
                main.mainloop()
            else:
                pop_upWindow("There is no enough balance in your Account")
        else:
            pop_upWindow("The maximum value/transaction is 5000.0\nTry again later!!!")
    else:
        pop_upWindow("Invalid Input!!!\nMust be digits")


def btnwindowSwitch(input):
	global main
	main.destroy()
	if input == 'f':
		main = windowFawryServices()
	elif input == 'b':
		main = windowBalanceInquery()
	elif input == 'w':
		main = windowCashWithdraw()
	else :
		main = windowChangePassword()

	main.mainloop()


def windowSwitch():
    window = tk.Tk()
    window.geometry("425x250+450+250")
    window.title("Main Menu")

    tk.Button(window, text="Cash Withdraw", command=lambda: btnwindowSwitch('w'), width=30, height=2, bg="light yellow").grid(row=0, column=0) 
    tk.Button(window, text="Change Password", command=lambda: btnwindowSwitch('c'), width=30, height=2, bg="light yellow").grid(row=1, column=1) 
    tk.Button(window, text="Balance Inquiry", command=lambda: btnwindowSwitch('b'), width=30, height=2, bg="light yellow").grid(row=2, column=0) 
    tk.Button(window, text="Fawry Service", command=lambda: btnwindowSwitch('f'), width=30, height=2, bg="light yellow").grid(row=3, column=1) 
    tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=30, height=2, bg="red").grid(row=4, column=0)
      
    return window
	

def windowMessage(mssage="Transaction Completed, Thank you"):
	window = tk.Tk()
	window.geometry("400x150+450+250")
	window.title("Successful Transaction")


	tk.Label(window, text=mssage).grid(row=1, column=1)
	tk.Button(window, text="Main Menu", command=lambda: mainWindow(),
						 width=20, height=1, bg="light blue").grid(row=2, column=2)
	tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=20, height=1, bg="red").grid(row=3, column=2)
	 

	return window


def windowLogin():
	window = tk.Tk()
	window.title("Login")
	window.geometry("300x100+500+300")

	labelAccount = tk.Label(window, text='ID').grid(row=1, column=1)

	entryAccount = tk.Entry(window, width=40)
	entryAccount.grid(row=1, column=2)

	btnLogin = tk.Button(window, text='Validate Account', command=lambda: btnValidateAccount(entryAccount.get()), bg = 'light green',
						width=20, height=1).grid(row=2, column=2)

	return window


def windowPassword():
	window = tk.Tk()
	window.title("Validate Password")
	window.geometry("325x100+500+300")
	
	labelPassword = tk.Label(window, text='Password').grid(row=1, column=1)
	entryPassword = tk.Entry(window, width=40, show="*")
	entryPassword.grid(row=1, column=2)
	btnLogin = tk.Button(window, text='LOGIN', command=lambda: btnValidatePassword(entryPassword.get()), bg = 'light green',
						 width=20, height=1).grid(row=2, column=2)

	return window



def windowCashWithdraw():
	window = tk.Tk()
	window.geometry("325x100+500+300")
	window.title("Cash Withdraw")

	labelAmount = tk.Label(window, text='Withdraw Amount').grid(row=1, column=1)
	entryCash = tk.Entry(window, width=40)
	entryCash.grid(row=1, column=2)
	tk.Button(window, text='Withdraw', command=lambda: btnValidateAmount(entryCash.get()), bg="light blue",
								  width=20, height=1).grid(row=2, column=2)
	tk.Button(window, text='Main Menu', command=lambda: mainWindow(), bg="light yellow",
                         width=20, height=1).grid(row=3, column=2)
	tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=20, height=1, bg = 'red').grid(row=4, column=2)
    
	return window


def windowChangePassword():
	global main, currentAccount

	window = tk.Tk()
	window.geometry("325x100+500+300")
	window.title("Change Password")


	labelPassword = tk.Label(window, text='New Password').grid(row=1, column=1)
	entryPassword = tk.Entry(window, width=40, show="*")
	entryPassword.grid(row=1, column=2)
	tk.Button(window, text='Change', command=lambda: btnChangePassword(entryPassword.get()), bg="light blue",
						 width=20, height=1).grid(row=2, column=2)
	tk.Button(window, text='Main Menu', command=lambda: mainWindow(), bg="light yellow",
                         width=20, height=1).grid(row=3, column=2)
	tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=20, height=1, bg="red").grid(row=4, column=2)
	 
	return window


def windowBalanceInquery():
	global currentAccount
	window = tk.Tk()
	window.geometry("225x100+500+300")
	window.title("Balance Inquiry")


	labelInfo = tk.Label(window, text="Welcome " + database[currentAccount]["Name"]).grid(row=1, column=1)
	labelBalance = tk.Label(window, text="Your balance is: " + database[currentAccount]["Balance"]).grid(row=2, column=1)
	tk.Button(window, text='Ok', command=lambda: mainWindow(), bg="light blue",
						 width=20, height=1).grid(row=3, column=1)
	tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=20, height=1, bg="red").grid(row=4, column=1)

	return window



def windowFawryServices():
	global main, currentAccount

	window = tk.Tk()
	window.title("Fawry Services")
	window.geometry("300x250+450+250")

	tk.Button(window, text="Orange", command=lambda: rechargeWindow(), width=20, height=2, bg="light green").grid(row=0, column=1)
	tk.Button(window, text="Etisalat", command=lambda: rechargeWindow(), width=20, height=2, bg="light green").grid(row=1, column=1)
	tk.Button(window, text="Vodafone", command=lambda: rechargeWindow(), width=20, height=2, bg="light green").grid(row=2, column=1)
	tk.Button(window, text="We", command=lambda: rechargeWindow(), width=20, height=2, bg="light green").grid(row=3, column=1)
	tk.Button(window, text="Main Menu", command=lambda: mainWindow(), bg="light yellow",
						 width=20, height=1).grid(row=4, column=2)
	tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=20, height=1, bg="red").grid(row=5, column=2)
	 
	return window


def windowRecharge():
	window = tk.Tk()
	window.title("Recharge Service")
	window.geometry("500x150+450+250")

	tk.Label(window, text='Mobile Number').grid(row=1, column=1)
	tk.Label(window, text='Amount').grid(row=2, column=1)

	entryMobile = tk.Entry(window, width=40)
	entryMobile.grid(row=1, column=2)
	entryAmount = tk.Entry(window, width=40)
	entryAmount.grid(row=2, column=2)
	
	tk.Button(window, text='Recharge', command=lambda: btnFawryRecharge(entryAmount.get()), width=20, height=1, bg="light blue").grid(row=3, column=2)
	tk.Button(window, text='Main Menu', command=lambda: mainWindow(), width=20, height=1, bg="light yellow").grid(row=4, column=2)
	tk.Button(window, text="Exit App", command=lambda: window.destroy(), width=20, height=1, bg="red").grid(row=5, column=2)
	 
	return window


main = windowLogin()
main.mainloop()
