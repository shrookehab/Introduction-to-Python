import tkinter

database = {"215321701332": {"Name": "Ahmed Abdelrazek Mohamed", "Password": "1783", "Balance": "3500166"},
            "203659302214": {"Name": "Salma Mohamed Foaad", "Password": "1390", "Balance": "520001"},
            "126355700193": {"Name": "Adel Khaled Abdelrahman", "Password": "1214", "Balance": "111000"},
            "201455998011": {"Name": "Saeed Amin Elsawy", "Password": "2001", "Balance": "1200"},
            "201122369851": {"Name": "Amir Salama Elgendy", "Password": "8935", "Balance": "178933"},
            "201356788002": {"Name": "Wael Mohamed Khairy", "Password": "3420", "Balance": "55000"},
            "203366789564": {"Name": "Mina Sameh Bishoy", "Password": "1179", "Balance": "18000"},
            "201236787812": {"Name": "Omnia Ahmed Awad", "Password": "1430", "Balance": "180350"}}

tries = {"215321701332": 0,
         "203659302214": 0,
         "126355700193": 0,
         "201455998011": 0,
         "201122369851": 0,
         "201356788002": 0,
         "203366789564": 0,
         "201236787812": 0}

current_acc_no = ""


def openDialog(msg, title="Message"):
    top = tkinter.Toplevel(main)
    top.geometry("300x80+600+350")
    top.title(title)
    lab = tkinter.Label(top, text=msg)
    lab.grid(row=0, column=0)
    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)
    top.mainloop()


def btn_check_accno(accNo):
    global main, current_acc_no
    if accNo in database.keys():
        current_acc_no = accNo
        main.destroy()
        main = create_pin_window()
        main.mainloop()
    else:
        openDialog('False Account No, please try again')


def btn_check_pin(pin):
    global main, current_acc_no
    if tries[current_acc_no] < 3:
        if pin == database[current_acc_no]["Password"]:
            openDialog('True Pin Code')
        else:
            tries[current_acc_no] += 1
            if tries[current_acc_no] >= 3:
                openDialog('Sorry you need to go to the closest bank branch')
            else:
                openDialog('False Account No, please try again\nTries left ' + str(3 - tries[current_acc_no]))
    else:
        openDialog('Sorry you need to go to the closest bank branch')



def create_accno_window():
    # Creating a window
    accno_windo = tkinter.Tk()
    accno_windo.title("Project")
    accno_windo.geometry("400x150+450+250")

    # adding the login button
    checkAccNoBtn = tkinter.Button(accno_windo, text='Check Account No',
                                   command=lambda: btn_check_accno(accnoEntry.get()), width=20, height=1)

    # Adding entry of username
    accnoEntry = tkinter.Entry(accno_windo, width=40)

    # Adding labels
    labAN = tkinter.Label(accno_windo, text='Account No:')

    # Griding
    labAN.grid(row=1, column=1)
    accnoEntry.grid(row=1, column=2)
    checkAccNoBtn.grid(row=2, column=2)
    accno_windo.columnconfigure(0, weight=1)
    accno_windo.rowconfigure(0, weight=1)
    accno_windo.columnconfigure(2, weight=1)
    accno_windo.rowconfigure(2, weight=1)
    return accno_windo


def create_pin_window():
    # Creating a window
    pin_windo = tkinter.Tk()
    pin_windo.title("Project")
    pin_windo.geometry("400x150+450+250")

    # adding the button
    checkAccNoBtn = tkinter.Button(pin_windo, text='Check PIN', command=lambda: btn_check_pin(entry.get()),
                                   width=20, height=1)

    # Adding entry of pin
    entry = tkinter.Entry(pin_windo, width=40, show="*")

    # Adding labels
    labAN = tkinter.Label(pin_windo, text='Pin Code:')

    # Griding
    labAN.grid(row=1, column=1)
    entry.grid(row=1, column=2)
    checkAccNoBtn.grid(row=2, column=2)
    pin_windo.columnconfigure(0, weight=1)
    pin_windo.rowconfigure(0, weight=1)
    pin_windo.columnconfigure(2, weight=1)
    pin_windo.rowconfigure(2, weight=1)
    return pin_windo

def  optionswindow():
	window = tk.Tk()
	window.geometry("300x300")
	window.title("choose an option")
	 
	global v
	v= tk.IntVar()
	
	radiobuttons = {"cash withdraw" : 1,
          "password change" : 2,
          "balance inquiry" : 3,
          "Fawry Service" : 4,
		  "exit" : 5}

	for (text, value) in radiobuttons.items():
		tk.Radiobutton(window, text = text, variable = v,value = value,command= whatwindow).grid(row= int(value), column=0)
	 
	return window
 

def cashwithdraw():

	window = tk.Tk()
	window.geometry("300x300")
	window.title("Cash withdraw")




def whatwindow():
	global v
	if v.get()==1:
		print("1 created successfully")
		cashwithdraw()
	elif v.get()==2:
		print("2 created successfully")
	elif v.get()==3:
		print("3 created successfully")
	elif v.get()==4:
		print("4 created successfully")
	elif v.get()==5:
		print("5 created successfully")
	

main = create_accno_window()
main.mainloop()