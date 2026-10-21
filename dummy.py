from tkinter import *
screen=Tk() 
screen.config(relief="ridge",border=20)
screen.geometry("400x400")
Label(screen,text="welcome",fg="blue").pack(pady=30)
Entry(screen).pack(pady=10)
Button(screen,text="click here").pack()
screen.mainloop()