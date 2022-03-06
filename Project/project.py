import tkinter
import tkinter as tk

database = {"1": {"Name": "Mina Sameh Bishoy", "Password": "1", "Balance": "100"},
            "215321701332": {"Name": "Ahmed Abdelrazek Mohamed", "Password": "1783", "Balance": "3500166"},
            "203659302214": {"Name": "Salma Mohamed Foaad", "Password": "1390", "Balance": "520001"},
            "126355700193": {"Name": "Adel Khaled Abdelrahman", "Password": "1214", "Balance": "111000"},
            "201455998011": {"Name": "Saeed Amin Elsawy", "Password": "2001", "Balance": "1200"},
            "201122369851": {"Name": "Amir Salama Elgendy", "Password": "8935", "Balance": "178933"},
            "201356788002": {"Name": "Wael Mohamed Khairy", "Password": "3420", "Balance": "55000"},
            "203366789564": {"Name": "Mina Sameh Bishoy", "Password": "1179", "Balance": "18000"},
            "201236787812": {"Name": "Omnia Ahmed Awad", "Password": "1430", "Balance": "180350"}}

trials = {"1": 0,
         "215321701332": 0,
         "203659302214": 0,
         "126355700193": 0,
         "201455998011": 0,
         "201122369851": 0,
         "201356788002": 0,
         "203366789564": 0,
         "201236787812": 0}

current_account = ""
current_user = {}



def btn_check_account_no(account_no):
    global main, current_account, current_user
    if account_no in database.keys():
        current_account = account_no
        current_user = database[current_account]
        main.destroy()
        main = create_pin_window()
        main.mainloop()
    else:
        openDialog('Invalid Account, please try again later')


def btn_check_pin(pin):
    global main, current_account
    if trials[current_account] < 3:
        if pin == database[current_account]["Password"]:
            main.destroy()
            main = optionswindow()
            main.mainloop()
        else:
            trials[current_account] += 1
            if trials[current_account] >= 3:
                openDialog('Sorry you need to go to the closest bank branch')
            else:
                openDialog('False Account No, please try again\ntrials left ' + str(3 - trials[current_account]))
    else:
        openDialog('Sorry you need to go to the closest bank branch')


def btn_check_amount(amount):
    global main, current_user
    if amount.isnumeric():
        if float(amount) <= 5000.0:
            if float(amount) % 100 == 0:
                if float(amount) <= float(current_user["Balance"]):
                    current_user["Balance"] = str(float(current_user["Balance"]) - float(amount))
                    main.destroy()
                    main = thanks_window()
                    main.mainloop()
                else:
                    openDialog("There is no enough balance in your credit")
            else:
                openDialog("Only allow amount that are multiple of 100.0LE")
        else:
            openDialog("The maximum value/transaction is 5000.0, try again later!!!")
    else:
        openDialog('Not valid!!!')

def openDialog(msg, title="Message"):
    top = tkinter.Toplevel(main)
    top.geometry("200x80+600+350")
    top.title(title)
    lab = tkinter.Label(top, text=msg)
    lab.grid(row=0, column=0)
    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)
    top.mainloop()


def open_options_again():
    global main
    main.destroy()
    main = optionswindow()
    main.mainloop()

def create_account_no_window():
    # Creating a window
    account_no_windo = tkinter.Tk()
    account_no_windo.title("Project")
    account_no_windo.geometry("400x150+450+250")

    # adding the login button
    checkaccount_noBtn = tkinter.Button(account_no_windo, text='Check Account No',
                                   command=lambda: btn_check_account_no(account_noEntry.get()), width=20, height=1)

    # Adding entry of username
    account_noEntry = tkinter.Entry(account_no_windo, width=40)

    # Adding labels
    labAN = tkinter.Label(account_no_windo, text='Account No:')

    # Griding
    labAN.grid(row=1, column=1)
    account_noEntry.grid(row=1, column=2)
    checkaccount_noBtn.grid(row=2, column=2)
    account_no_windo.columnconfigure(0, weight=1)
    account_no_windo.rowconfigure(0, weight=1)
    account_no_windo.columnconfigure(2, weight=1)
    account_no_windo.rowconfigure(2, weight=1)
    return account_no_windo


def create_pin_window():
    # Creating a window
    pin_windo = tkinter.Tk()
    pin_windo.title("Project")
    pin_windo.geometry("400x150+450+250")

    # adding the button
    checkaccount_noBtn = tkinter.Button(pin_windo, text='Check PIN', command=lambda: btn_check_pin(entry.get()),
                                   width=20, height=1)

    # Adding entry of pin
    entry = tkinter.Entry(pin_windo, width=40, show="*")

    # Adding labels
    labAN = tkinter.Label(pin_windo, text='Pin Code:')

    # Griding
    labAN.grid(row=1, column=1)
    entry.grid(row=1, column=2)
    checkaccount_noBtn.grid(row=2, column=2)
    pin_windo.columnconfigure(0, weight=1)
    pin_windo.rowconfigure(0, weight=1)
    pin_windo.columnconfigure(2, weight=1)
    pin_windo.rowconfigure(2, weight=1)
    return pin_windo


def optionswindow():
    window = tk.Tk()
    window.geometry("400x250+450+250")
    window.title("Main Window")

    tk.Button(window, text="Cash Withdraw", command=lambda: whatwindow(1), width=30, bg="light blue").grid(row=1,
                                                                                                           column=1)
    tk.Button(window, text="Password Change", command=lambda: whatwindow(2), width=30, bg="light blue").grid(row=1,
                                                                                                             column=2)
    tk.Button(window, text="Balance Inquiry", command=lambda: whatwindow(3), width=30, bg="light blue").grid(row=2,
                                                                                                             column=1)
    tk.Button(window, text="Fawry Service", command=lambda: whatwindow(4), width=30, bg="light blue").grid(row=2,
                                                                                                           column=2)
    tk.Button(window, text="Exit", command=lambda: whatwindow(5), width=30, bg="red").grid(row=3, column=1)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(3, weight=1)
    window.rowconfigure(3, weight=1)
    return window


def thanks_window():
    window = tk.Tk()
    window.geometry("400x150+450+250")
    window.title("Thank You")

    btn = tkinter.Button(window, text='Go To Home', command=lambda: open_options_again(),
                                   width=20, height=1)

    # Adding labels
    lb = tkinter.Label(window, text='Thank you for choosing our bank')

    # Griding
    lb.grid(row=1, column=1)
    btn.grid(row=2, column=2)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(2, weight=1)
    window.rowconfigure(2, weight=1)
    return window

def validateAmount():
    global amount
    if int(amount.get()) <= 5000:
        print("Valide")


def cash_withdraw():
    window = tk.Tk()
    window.geometry("500x200+450+250")
    window.title("Cash Withdraw")

    # adding the button
    withdraw_btn = tkinter.Button(window, text='Withdraw', command=lambda: btn_check_amount(entry.get()),
                                  width=20, height=1)

    entry = tkinter.Entry(window, width=40)

    # Adding labels
    lab_amount = tkinter.Label(window, text='Amount value:')
    # Griding
    lab_amount.grid(row=1, column=1)
    entry.grid(row=1, column=2)
    withdraw_btn.grid(row=2, column=2)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(2, weight=1)
    window.rowconfigure(2, weight=1)
    return window


def whatwindow(v):
    global main
    if v == 1:
        print("1 created successfully")
        main.destroy()
        main = cash_withdraw()
        main.mainloop()
    elif v == 2:
        main.destroy()
        main = password_change_window()
        main.mainloop()
    elif v == 3:
        main.destroy()
        main = checkBalance()
        main.mainloop()
    elif v == 4:
        main.destroy()
        main = fawry_services_window()
        main.mainloop()
    elif v == 5:
        print("5 created successfully")
        main.destroy()
        main = create_account_no_window()
        main.mainloop()


def gotohome():
    global main, window
    window.destroy()
    main = optionswindow()


def checkBalance():
    global window
    window = tk.Tk()
    window.geometry("400x150+450+250")
    window.title("Balance Inquiry")
    msg = "Welocme " + current_user["Name"]
    label_name = tkinter.Label(window, text=msg, width=30)
    label_name.grid()
    msg2 = "Your Amount is : " + current_user["Balance"]
    label_amount = tkinter.Label(window, text=msg2, width=30)
    label_amount.grid()
    btn = tkinter.Button(window, text="OK ", command=gotohome, width=10)
    btn.grid()
    return window

def password_change(chpass):
	database[current_account]["Password"]=chpass
	success=tkinter.Toplevel()
	success.title('password change successfully')
	success.geometry("400x150+450+250")
	labAN = tkinter.Label(success, text='password change successfully')
	labAN.pack()
	ok_btn= tkinter.Button(success, text='OK', command=success.destroy, width=20, height=1)
	ok_btn.pack()

def password_change_window():
    # Creating a window
    global main, current_account
    window = tkinter.Tk()
    window.title("Change Password")
    window.geometry("400x150+450+250")
    labAN = tkinter.Label(window, text='Enter the new password:')
    labAN.pack()
    passwd = tkinter.Entry(window, width=40, show="*")
    passwd.pack()
    # adding the button
    chgpass = tkinter.Button(window, text='Enter', command=lambda: password_change(passwd.get()), width=20, height=1)
    chgpass.pack()
    # Adding entry of pin
    # account_noEntry = tkinter.Entry(pch_windo, width=40, show="*")

    return window


def confirm_Amount(amountTotal):
	global main, current_account, window
	window = tkinter.Tk()
	window.title('Recharge Service')
	window.geometry("400x150+450+250")
	balancAmount = float(database[current_account]["Balance"])
	if balancAmount >= float(amountTotal):
		database[current_account]["Balance"] = str(balancAmount - float(amountTotal))
		popup_window = tkinter.Tk()
		popup_window.title('Successfuly Recharged')
		popup_window.geometry("400x150+450+250")
		labAN1 = tkinter.Label(popup_window, text='Successfuly Recharged')
		labAN1.pack()
		confirm = tkinter.Button(popup_window, text=' Confirm ', command=popup_window.destroy, width=20, height=1)
		confirm.pack()


	else:
		popup_window = tkinter.Tk()
		popup_window.title('Invalid Amount')
		popup_window.geometry("400x150+450+250")
		labAN1 = tkinter.Label(popup_window, text='Invalid Amount')
		labAN1.pack()
		confirm = tkinter.Button(popup_window, text=' OK ', command=popup_window.destroy, width=20, height=1)
		confirm.pack()
	
	#return window


def recharge_window():
	global main, current_account, window
	window = tkinter.Tk()
	window.title('Recharge Service')
	window.geometry("400x150+450+250")
	labAN1 = tkinter.Label(window, text='Phone number')
	labAN1.pack()
	entry1 = tkinter.Entry(window, width=40)
	entry1.pack()
	labAN2 = tkinter.Label(window, text='Amount')
	labAN2.pack()
	entry2 = tkinter.Entry(window, width=40)
	entry2.pack()

	confirm = tkinter.Button(window, text=' Confirm ', command=lambda: confirm_Amount(entry2.get()), width=20, height=1)
	confirm.pack()
	#return window


def fawry_services_window():
    # Creating a window
    global main, current_account, window
    window = tkinter.Tk()
    window.title("Fawry Services")
    window.geometry("400x150+450+250")
    labAN = tkinter.Label(window, text='Choose your Network')
    labAN.pack()
    etisalat = tkinter.Button(window, text='Etisalat', command=lambda: recharge_window(), width=20, height=1)
    etisalat.pack()
    vodafone = tkinter.Button(window, text='Vodafone', command=lambda: recharge_window(), width=20, height=1)
    vodafone.pack()
    orange = tkinter.Button(window, text=' Orange ', command=lambda: recharge_window(), width=20, height=1)
    orange.pack()
    we = tkinter.Button(window, text='   We   ', command=lambda: recharge_window(), width=20, height=1)
    we.pack()
    # Adding entry of pin
    # account_noEntry = tkinter.Entry(pch_windo, width=40, show="*")

    return window


main = create_account_no_window()
main.mainloop()
