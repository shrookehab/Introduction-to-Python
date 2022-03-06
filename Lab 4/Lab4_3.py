from tkinter import *

def Btn1_func():
	print("print your name")
	
def Btn2_func():
	print("OK")
	
	
root = Tk()  
root.geometry('250x150')  
root.title('Playing with buttons3')

Button1 = Button(root, text="Print_Name", bg='blue', command=Btn1_func).place(x=30, y=10)  
Button2 = Button(root, text="OK", bg='green', command=Btn2_func).place(x=70, y=90)  
Button3 = Button(root, text="Close", bg='red', command=root.destroy).place(x=120, y=90)  


root.mainloop()