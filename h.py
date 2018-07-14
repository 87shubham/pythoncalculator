from tkinter import *
from tkinter import messagebox
root = Tk()
root.resizable(width=False, height=False)

opeation=""
def btnclick(number):
    global opeation
    opeation+=str(number)
    input_Text.set(opeation)
def clear():
 global opeation
 opeation=""
 input_Text.set(opeation)

def equal():
     global opeation
     sum=str(eval(opeation))
     input_Text.set(sum)
     opeation=""
def about():
    messagebox.showinfo("about","Simple calculator")
root.title("CALCULATOR")

menu1=Menu(root)
root.config(menu=menu1)
submenu=Menu(menu1)
menu1.add_cascade(label="Help",menu=submenu)
submenu.add_cascade(label="About", command =about)


input_Text=StringVar()
textfield=Entry(root,font=("Arial",20,"bold"),bd=30,fg="grey",bg="cyan",justify='right',textvariable=input_Text,insertwidth=3).grid(columnspan=4)

button1=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="7", padx="15",pady="15",command=lambda :btnclick(7)).grid(row=1,column=0,sticky="nsew")
button2=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="8", padx="15",pady="15",command=lambda :btnclick(8)).grid(row=1,column=1,sticky="nsew")
button3=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="9", padx="15",pady="15",command=lambda :btnclick(9)).grid(row=1,column=2,sticky="nsew")
button4=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="4", padx="15",pady="15",command=lambda :btnclick(4)).grid(row=2,column=0,sticky="nsew")
button5=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="5", padx="15",pady="15",command=lambda :btnclick(5)).grid(row=2,column=1,sticky="nsew")
button6=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="6", padx="15",pady="15",command=lambda :btnclick(6)).grid(row=2,column=2,sticky="nsew")
button7=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="1", padx="15",pady="15",command=lambda :btnclick(1)).grid(row=3,column=0,sticky="nsew")
button8=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="2", padx="15",pady="15",command=lambda :btnclick(2)).grid(row=3,column=1,sticky="nsew")
button9=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="3", padx="15",pady="15",command=lambda :btnclick(3)).grid(row=3,column=2,sticky="nsew")
button0=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="0", padx="15",pady="15",command=lambda :btnclick(0)).grid(row=4,column=0,sticky="nsew")

button10=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="=", padx="15",pady="15",command=equal).grid(row=4,column=3,sticky="nsew")
button=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text=".", padx="15",pady="15",command=lambda :btnclick(".")).grid(row=4,column=2,sticky="nsew")
buttondiv=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="/", padx="15",pady="15",command=lambda :btnclick("/")).grid(row=1,column=3,sticky="nsew")
buttonmul=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="*", padx="15",pady="15",command=lambda :btnclick("*")).grid(row=2,column=3,sticky="nsew")
buttonsum=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="+", padx="15",pady="15",command=lambda :btnclick("+")).grid(row=3,column=3,sticky="nsew")



button11=Button(root,font=("Arial",20,"bold"),bd=1,fg="black",text="clr", padx="15",pady="15",command=clear).grid(row=4,column=1,sticky="nsew")

root.mainloop()

