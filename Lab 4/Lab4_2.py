from tkinter import *

def Btn_func():
	print("button pressed")
	
root = Tk()  
root.geometry('250x150')  
root.title('Playing with buttons2')

Button1 = Button(root, text="Button1").place(x=0, y=0)  
Button2 = Button(root, text="Button2").place(x=20, y=25)  
Button3 = Button(root, text="Button3").place(x=40, y=50)  
Button4 = Button(root, text="Button4").place(x=60, y=75)  

root.mainloop()