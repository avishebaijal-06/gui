from tkinter import *
from tkinter.ttk import *
screen=Tk() 
screen.config(relief="sunken",border=20)
screen.geometry("600x600")
def abc():
  print(name.get())  
  result.config(text=name.get())
  p["value"]+=20
Label(screen,text="toy shop").pack(pady=20)
name=Entry(screen)
name.pack(pady=10,side=LEFT, anchor="nw")
Button(screen,text="click here",command=abc).pack(side=RIGHT,anchor="ne")
result=Label(screen,text="result",font="ariel 24 bold")
result.pack()
s=Spinbox(screen,from_=1,to=30,font="ariel 30 ",state="readonly")
s.pack(side="bottom",anchor="sw")
p=Progressbar(screen,cursor="hand1",mode="indeterminate",orient="vertical")
p.pack()
t=Text(screen,width=50,height=4)
t.pack()
screen.mainloop()