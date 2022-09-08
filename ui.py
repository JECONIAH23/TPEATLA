from tkinter import *
from functools import partial
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Login")
window.config(bg="#f07167")

lbl1=Label(window,text="Login",font=("Courier",30),fg="#fed9b7",bg="#f07167")
lbl1.pack(anchor="center")


lbl2=Label(window,text="Email:",font=("Georgia",20),fg="#fdfcdc",bg="#f07167")
lbl2.place(x=10,y=90)

ent1=Entry(window)
ent1.place(x=200,y=100)



lbl3=Label(window,text="Password:",font=("Georgia",20),fg="#fdfcdc",bg="#f07167")
lbl3.place(x=10,y=170)

ent3=Entry(window)
ent3.place(x=200,y=180)


loginbtn=Button(window,text="Login",font=("",15),bg="#f07167")
loginbtn.place(x=150,y=300)
window.mainloop()

#########
#Login 2#
#########
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=1, column=1)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=3)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=1)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=3)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=2)  


tkWindow.mainloop()

print("Main llop 1 exited")
