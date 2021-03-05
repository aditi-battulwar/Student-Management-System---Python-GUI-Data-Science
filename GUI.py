from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import bs4
import requests
import socket
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

def f1():
	a.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	a.withdraw()

def f3():
	con = None
	try:
		con = connect("test.db")	# connect to dbms
		print("connected")
		rno = int(entrno.get())
		entrno.delete(0, END)
		name = entname.get()
		entname.delete(0, END)
		marks = float(entmarks.get())
		entmarks.delete(0, END)
		
		flag = False
		error = ""

		if(rno == 0):
			error +="Roll no. should be valid\n"	
			flag = True
		elif int(rno) < 0:
			error+="Roll no. should be positive\n"
			flag = True
	
		pattern = re.compile(r'^[a-zA-Z.]')
		if(len(name)==0):
			flag = True
			error += "Name should not be empty\n"	
		elif not(pattern.search(name)):
			flag = True
			error += "Invalid Name\n"	
		elif len(name) < 2:
			error+="Name too small\n"
			flag = True			

		if(float(marks) < 0 or float(marks) > 100):
			error+="enter valid marks\n"
			flag = True
		print(rno,"	",name,"	",marks)		

		
		if(not flag): # no error
			args = (rno, name, marks)
			cursor = con.cursor()	
			sql = "insert into student values('%d', '%s', '%f')"
			cursor.execute(sql % args)
			con.commit()
			showinfo("success", "record added")
		else:
			showerror('failure',error)	
	
					
	except Exception as e:
		#showerror("failure" , "insertion issue " + str(e))
		showerror("failure" , "Enter all details !")
		con.rollback()
	finally:
		if con is not None:
			con.close()	# close the connection
			print("disconnected")	

def f4():
	root.deiconify()
	v.withdraw()
def f5():
	stdata.delete(1.0, END)
	v.deiconify()
	root.withdraw()
	con = None
	try:
		con = connect("test.db")	# connect to dbms
		print("connected")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()		# list of tuples [(10,'amit'),(20,'ali')]
		info = ""
		for d in data:
			info = info + "rno: " + str(d[0]) + " name: " + str(d[1]) + " marks: " + str(d[2]) + "\n"	
		stdata.insert(INSERT, info)
	except Exception as e:
		print("selection issue ", e)
	finally:
		if con is not None:
			con.close()	# close the connection
			print("disconnected")	


def f6():
	root.deiconify()
	u.withdraw()
def f7():
	u.deiconify()
	root.withdraw()

def f8():
	con = None 
	try: 
		con = connect("test.db")	# connect to dbms 
		print("connected") 
		rno = int(erno.get())
		erno.delete(0, END)
		name = ename.get()
		ename.delete(0, END) 
		marks = float(emarks.get())
		emarks.delete(0, END)
		
		flag = False
		error = ""
		
		if(rno == 0):
			error +="Roll no. should be valid\n"	
			flag = True
		elif int(rno) < 0:
			error+="Roll no. should be positive\n"
			flag = True
	
		pattern = re.compile(r'^[a-zA-Z.]')
		if(len(name)==0):
			flag = True
			error += "Name should not be empty\n"	
		elif not(pattern.search(name)):
			flag = True
			error += "Invalid Name\n"	
		elif len(name) < 2:
			error+="Name too small\n"
			flag = True			

		if(float(marks) < 0 or float(marks) > 100):
			error+="enter valid marks\n"
			flag = True
		print(rno,"	",name,"	",marks)		

		
		if(not flag): # no error
			cursor = con.cursor() 
			cursor.execute("""update student set name = ?, marks = ? where rno = ? """, (name,marks,rno)) 
			if cursor.rowcount >= 1: 
				con.commit()
				showinfo("success", "record updated")	 
			else: 
 				print(rno, "does not exists ") 
		else:
			showerror('failure',error)

	except Exception as e: 
		# showerror("failure","updation issue " +str(e)) 
		showerror("failure" , "Enter all details !")
		con.rollback() 
	finally: 
		if con is not None: 
 			con.close() # close the connection
		print("disconnected")


def f9():
	root.deiconify()
	d.withdraw()

def f10():
	d.deiconify()
	root.withdraw()

def f11():
	pass
	
	con = None 
	try: 
		con = connect("test.db") # connect to dbms 
		print("connected") 
		rno = int(enrno.get())
		enrno.delete(0, END)

		flag = False
		error = ""
		
		if(rno == 0):
			error +="Roll no. should be valid\n"	
			flag = True
		elif int(rno) < 0:
			error+="Roll no. should be positive\n"
			flag = True

		if(not flag): # no error
			args = (rno) 
			cursor = con.cursor() 
			sql = "delete from student where rno = '%d' " 
			cursor.execute(sql % args)  
			if cursor.rowcount >= 1: 
				con.commit() 
				showinfo("success", "record deleted")	
			else: 
				print(rno, "does not exists ")
		else:
			showerror('failure',error) 

	except Exception as e: 
		# showerror("failure","deletion issue " +str(e)) 
		showerror("failure" , "Enter all details !")
		con.rollback() 
	finally: 
		if con is not None: 
			con.close()  # close the connection 
		print("disconnected")
  

def showChart():
	con = None
	try:
		con = connect("test.db")	# connect to dbms
		print("connected")
		cursor = con.cursor()
		sql = "select name, marks from student order by marks desc limit 5"
		cursor.execute(sql)

		with open("out.txt", "w") as csv_file:  # Python 3 version
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow([col[0] for col in cursor.description]) # write headers
			for row in cursor:
				csv_writer.writerow(row)
		mydata = pd.read_csv("E:\\Python\\demo_Python\\Python\\Project\\out.txt", sep =",")
		# E:\\Python\\demo_Python\\Python\\Project\\out.txt
		print(mydata)
		#create a bar chart
		n = mydata['name'].tolist()
		s = mydata['marks'].tolist()
		print(n)
		print(s)
		plt.bar(n, s, color=['red','green','blue','red','green'])
		plt.title("Batch Information !")
		plt.xlabel("Names")
		plt.ylabel("Markss")
		plt.show()

	except Exception as e:
		print("selection issue ", e)
	finally:
		if con is not None:
			con.close()	# close the connection
			print("disconnected")


def location_label(lblLoc):
	def location():
		try:
			socket.create_connection( ("www.google.com", 80))
			#print("u r connected")
			res = requests.get("https://ipinfo.io/")
			#print(res)
			data = res.json()	# dict { K1:V1 , K2:V2}
			#print(data)
			ip = data['ip']
			#print("ip address ", ip)
			global city_name
			city_name = data['city']
			#print("city name ", city_name)
			
			lblLoc.config(text= " Location: " + city_name + "\n")
			lblLoc.after(1000, location)
			
		except OSError as e:
			print("issue ", e)
	location()


def temp_label(lblTemp):
	def temp():
		try:
			socket.create_connection( ("www.google.com", 80))
			# city = input("enter location name ")

			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2 = "&q=" + city_name 
			a3 = "&appid=c6e315d09197cec231495138183954bd"

			api_address =  a1 + a2  + a3 		
			res = requests.get(api_address)
			#print(res)
	
			data = res.json()
			#print(data)
		
			#main = data['main']
			#print("main --> ", main)
			#temp1 = main['temp']
			#print("temp1 --> ", temp1)

			temp2 = data['main']['temp']
			#print("temp2 --> ", temp2)
			
			lblTemp.config(text= "Temp: " + str(temp2) + " 'C " "\n")
			lblTemp.after(2000, temp)
	
		except OSError as e:
			print("issue ", e)
	temp()	


def quote_label(lblQuote):
	def quote():
		try:
			socket.create_connection(("www.google.com", 80))
			#print("u r connected")

			res = requests.get("https://www.brainyquote.com/quote_of_the_day")
			#print(res)
	
			soup = bs4.BeautifulSoup(res.text, "lxml")
			#print(soup)
	
			data = soup.find("img", {"class": "p-qotd"})
			#print(data)

			global motd
			motd = data['alt']	
			# print("motd: ",motd)
			
			lblQuote.config(text= "QOTD: "+ motd + "\n")
			lblQuote.after(3000, quote)
		
		except Exception as e:
			print("issue", e)
	quote()


# design of root window --> SMS

root = Tk()
root.title("S.M.S")
root.geometry("1210x450+100+100")


btnAdd = Button(root, text="Add", font=("arial", 18, "bold"), width=10, command=f1)
btnView = Button(root, text="View", font=("arial", 18, "bold"), width=10, command=f5)

btnUpdate = Button(root, text="Update", font=("arial", 18, "bold"), width=10, command=f7)
btnDelete = Button(root, text="Delete", font=("arial", 18, "bold"), width=10, command=f10)
btnCharts = Button(root, text="Charts", font=("arial", 18, "bold"), width=10, command=showChart)
lblLoc = Label(root, font=("arial", 18, "bold"), width= 16)
lblTemp = Label(root, font=("arial", 18, "bold"), width= 50)
lblQuote = Label(root, font=("arial", 18, "bold"), width=80)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)

lblLoc.place(y=360)
location_label(lblLoc)

lblTemp.place(x=390,y=360)
temp_label(lblTemp)

lblQuote.place(x=1,y=400)
quote_label(lblQuote)


# design of a window --> Add Student

a = Toplevel(root)
a.title("Add Student")
a.geometry("500x400+400+200")
a.withdraw()

lblrno = Label(a, text="enter no", font=("arial", 18, "bold"))
entrno = Entry(a, bd=5, font=("arial", 18, "bold"))
lblname = Label(a, text="enter name", font=("arial", 18, "bold"))
entname = Entry(a, bd=5, font=("arial", 18, "bold"))

lblmarks = Label(a, text="enter marks", font=("arial", 18, "bold"))
entmarks = Entry(a, bd=5, font=("arial", 18, "bold"))

btnsave = Button(a, text="Save", font=("arial", 18, "bold"), command = f3)
btnback = Button(a, text="Back", font=("arial", 18, "bold"), command = f2)

lblrno.pack(pady=5)
entrno.pack(pady=5)
lblname.pack(pady=5)
entname.pack(pady=5)

lblmarks.pack(pady=5)
entmarks.pack(pady=5)

btnsave.pack(pady=5)
btnback.pack(pady=5)

# design of v window --> View Student

v = Toplevel()
v.title("View Student")
v.geometry("500x400+400+200")
v.withdraw()

stdata = ScrolledText(v, width = 50, height = 20)
btnvback = Button(v, text="Back", font=("arial", 18, "bold"), command = f4)

stdata.pack(pady=10)
btnvback.pack(pady=10)


# design of u window --> Update Student

u = Toplevel()
u.title("Update Student")
u.geometry("500x400+400+200")
u.withdraw()

lrno = Label(u, text="enter no", font=("arial", 18, "bold"))
erno = Entry(u, bd=5, font=("arial", 18, "bold"))
lname = Label(u, text="enter name", font=("arial", 18, "bold"))
ename = Entry(u, bd=5, font=("arial", 18, "bold"))
lmarks = Label(u, text="enter marks", font=("arial", 18, "bold"))
emarks = Entry(u, bd=5, font=("arial", 18, "bold"))
bsave = Button(u, text="Save", font=("arial", 18, "bold"), command= f8)
bback = Button(u, text="Back", font=("arial", 18, "bold"), command = f6)

lrno.pack(pady=5)
erno.pack(pady=5)
lname.pack(pady=5)
ename.pack(pady=5)
lmarks.pack(pady=5)
emarks.pack(pady=5)
bsave.pack(pady=5)
bback.pack(pady=5)


# design of d window --> Delete Student

d = Toplevel(root)
d.title("Delete Student")
d.geometry("500x400+400+200")
d.withdraw()

lbrno = Label(d, text="enter no", font=("arial", 18, "bold"))
enrno = Entry(d, bd=5, font=("arial", 18, "bold"))
btsave = Button(d, text="Save", font=("arial", 18, "bold"), command=f11)
btback = Button(d, text="Back", font=("arial", 18, "bold"), command=f9)

lbrno.pack(pady=5)
enrno.pack(pady=5)
btsave.pack(pady=5)
btback.pack(pady=5)


root.mainloop()