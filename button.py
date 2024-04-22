#python application to create a simple button  
  
from tkinter import *   
  
  
top = Tk()  
  
top.geometry("600x100")  
  
b = Button(top,text = "Simple")  
  
b.pack()  
  
top.mainloop()  