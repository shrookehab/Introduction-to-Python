from tkinter import *
from functools import partial

def Login(username, password):
	if username.get() == "shrook" and password.get() == "12345":
		window = Toplevel()
		window.title('Welcome')
		toplevelLabel = Label(window, text="Welcome Shrook").grid(row=0, column=0)
		Button1 = Button(window, text="Close", command=window.destroy).grid(row=1, column=0)
		window.mainloop()
	else:
		window = Toplevel()
		window.title('Welcome')
		toplevelLabel = Label(window, text="Wrong Input").grid(row=0, column=0)
		Button1 = Button(window, text="Close", command=window.destroy).grid(row=1, column=0)
		window.mainloop()

root = Tk()  
root.geometry('250x150')  
root.title('User Login Form :)')

usernameLabel = Label(root, text="Username").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)  

passwordLabel = Label(root,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)  

LoginCommand = partial(Login, username, password)
loginButton = Button(root, text="Login", command=LoginCommand).grid(row=5, column=1)  

root.mainloop()