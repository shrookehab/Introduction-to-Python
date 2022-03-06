from tkinter import *

def Btn_func():
	print("button pressed")
	
root = Tk()  
root.geometry('250x150')  
root.title('Playing with buttons')

Button1 = Button(root, text="Button1").grid(row=0, column=1)  
Button2 = Button(root, text="Button2").grid(row=1, column=0)  
Button3 = Button(root, text="Button3").grid(row=1, column=2)  
Button4 = Button(root, text="Button4").grid(row=2, column=1)  

root.mainloop()