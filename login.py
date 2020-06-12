from tkinter import*
from tkinter import messagebox
import mysql.connector
from functools import partial

win=Tk()
win.title("Signin")
win.geometry('400x400')
win.configure(bg='black')

def login(lx,x1,x2):
	email=x1.get()
	pwd=x2.get()
	mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="Your db password",
			database="db name"
		)

	mycursor= mydb.cursor()
	#create database
	sql="select name from Userdetails where EmailID = %s and Password = %s"
	val=(email,pwd,)
	mycursor.execute(sql,val)
	c=0
	for i in mycursor:
		c+=1
	if c>0:
		lx.config(text='Logged In Successfully',fg='yellow')
	else:
		lx.config(text='Invalid EmailID or Password',fg='red')
	return

def open():
	win2=Toplevel(win)
	win2.title("SignUp")
	win2.geometry('600x600')
	win2.configure(bg='grey')

	def insert(l7,x1,x2,x3,x4,x5,ch):
		fn=x1.get()
		p=x2.get()
		e=x3.get()
		g=x4.get()
		a=x5.get()
		c=ch.get()
		mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="Your db Password",
			database="Your db name"
		)

		mycursor= mydb.cursor()
		if fn and p and e and g and a:

			if c==True:
				#Create database
				mycursor.execute("CREATE TABLE IF NOT EXISTS Userdetails (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Password VARCHAR(255), EmailID VARCHAR(255), Gender VARCHAR(255),Age VARCHAR(255))")

				sql="INSERT INTO Userdetails (Name,Password,EmailID,Gender,Age) VALUES (%s,%s,%s,%s,%s)"
				val=(fn,p,e,g,a)
				mycursor.execute(sql,val)

				mydb.commit()

				l7.config(text="Registration Successful!")
				return
			else:
				messagebox.showinfo('Warning','You have to agree the terms and policies')
				return
		else:
			messagebox.showinfo('Warning','All fields are required')
			return

	l1=Label(win2,text='SignUp',font=("bold", 30),bg='black',fg='white')
	l1.pack(fill=X,pady=20)

	fm1=Frame(win2,bg='grey')
	fm1.pack(pady=10)
	fm2=Frame(win2,bg='grey')
	fm2.pack(pady=10)
	fm3=Frame(win2,bg='grey')
	fm3.pack(pady=10)
	fm4=Frame(win2,bg='grey')
	fm4.pack(pady=10)
	fm5=Frame(win2,bg='grey')
	fm5.pack(pady=10)
	fm6=Frame(win2,bg='grey')
	fm6.pack(pady=10)
	fm7=Frame(win2,bg='grey')
	fm7.pack(pady=10)
	fm8=Frame(win2,bg='grey')
	fm8.pack(pady=10)

	x1=StringVar()
	x2=StringVar()
	x3=StringVar()
	x4=StringVar()
	x5=StringVar()

	l2=Label(fm1,text='FullName',font=("bold", 15),bg='grey')
	l2.pack(side=LEFT)
	e2=Entry(fm1,textvariable=x1,bd=5,width=50,font=('ariel' ,10,'bold'))
	e2.pack(padx=20)

	l3=Label(fm2,text='Password',font=("bold", 15),bg='grey')
	l3.pack(side=LEFT)
	e3=Entry(fm2,textvariable=x2,bd=5,width=50,font=('ariel' ,10,'bold'),show="*")
	e3.pack(padx=20)

	l4=Label(fm3,text='Email',font=("bold", 15),bg='grey')
	l4.pack(padx=20,side=LEFT)
	e4=Entry(fm3,textvariable=x3,bd=5,width=50,font=('ariel' ,10,'bold'))
	e4.pack(padx=30)

	l5=Label(fm4,text='Gender',font=("bold", 15),bg='grey')
	l5.pack(padx=15,side=LEFT)
	e5=Entry(fm4,textvariable=x4,bd=5,width=50,font=('ariel' ,10,'bold'))
	e5.pack(padx=45)


	l6=Label(fm5,text='Age',font=("bold", 15),bg='grey')
	l6.pack(padx=30,side=LEFT)
	e6=Entry(fm5,textvariable=x5,bd=5,width=50,font=('ariel' ,10,'bold'))
	e6.pack(padx=40)

	l7=Label(fm7,font=('ariel' ,20,'bold'),fg='green',bg='grey')
	l7.pack()

	chk_state=BooleanVar()
	chk_state.set(False)
	chk=Checkbutton(fm6,text='I agree to the terms and policies',var=chk_state,bd=5,fg='navy',bg='grey')
	chk.pack(pady=10)


	insert=partial(insert,l7,x1,x2,x3,x4,x5,chk_state)

	Button(fm8, text='Submit',width=10,bg='brown',fg='white',command=insert,font=("bold", 15)).pack()

	win2.mainloop()

x1=StringVar()
x2=StringVar()

label=Label(win,text='Sign-in',font=("Times", "30", "bold italic"),bg='green',fg='yellow')
label.pack(fill=X)

fm1=Frame(win,bg='black')
fm1.pack(pady=20)
fm2=Frame(win,bg='black')
fm2.pack(pady=20)
fm3=Frame(win,bg='black')
fm3.pack(pady=20)

l1=Label(fm1,text='EmailID',font=('ariel' ,10,'bold'),bg='black',fg='white')
l1.pack(side=LEFT,padx=20)
e1=Entry(fm1,bd=5,font=('ariel' ,10,'bold'),width=25,textvariable=x1)
e1.pack()

l2=Label(fm2,text='Password',font=('ariel' ,10,'bold'),bg='black',fg='white')
l2.pack(side=LEFT,padx=20)
e2=Entry(fm2,bd=5,font=('ariel' ,10,'bold'),width=25,textvariable=x2,show='*')
e2.pack()

l3=Label(fm3,text='New user? SignUp',bg='black',fg='green',font=("Times", "15", "bold italic"))
l3.pack(side=LEFT)
Button(fm3,text='Here',bg='green',fg='white',font=('ariel' ,10,'bold'),command=open).pack()

lx=Label(win,bg='black',fg='yellow',font=('ariel' ,20,'bold'))
lx.pack(pady=10)

login=partial(login,lx,x1,x2)

Button(win,text='Login',bg='red',fg='white',font=('ariel' ,10,'bold'),width=10,command=login).pack()

win.mainloop()
