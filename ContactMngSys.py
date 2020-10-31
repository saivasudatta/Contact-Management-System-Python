from tkinter import *
from tkinter import messagebox
import sqlite3

def Display_Window():
	t.delete(1.0, END)
	conn = sqlite3.connect('Contacts.db')
	print ("Opened database successfully")


	cursor = conn.execute("SELECT * from Contacts order by name")
	for row in cursor:
		name = row[1]
		number = row[2]
		t.insert('insert', "%s:%s\n"%(name,number))

	conn.close()
	return

def Add_Window():
	s1=entry1_Root.get()
	s2=entry2_Root.get()

	#checks if Name is empty
	if s1 == "":
		messagebox.showerror("Contact Management", "Enter proper name")
		return    

	#Verifing if input number is correctly entered
	try:
		val = int(s2)
	except ValueError:
		messagebox.showerror("Contact Management", "Enter proper number")
		return

	conn = sqlite3.connect('Contacts.db')
	print ("Opened database successfully")

	conn.execute("INSERT INTO Contacts (NAME, NUMBER)  VALUES (?, ?)",(s1,s2));
	conn.commit()
	print ("Records created successfully")
	conn.close()
	entry1_Root.delete(0, 'end')
	entry2_Root.delete(0, 'end')
	

	Display_Window()
	messagebox.showinfo("Contact Management", "Name added successfully")

def Delete_Window():
	if var.get()==1:
		flag = 0
		s1 = entry1_Root.get()


		if s1 == "":
			messagebox.showerror("Contact Management", "Enter proper name")
			return

		conn = sqlite3.connect('Contacts.db')
		print ("Opened database successfully")

		cursor = conn.execute("SELECT * from Contacts order by name")
		for row in cursor:
			name = row[1]
			if s1 == name:
				conn.execute("DELETE from Contacts where NAME=(?)",(s1,))
				conn.commit()
				flag = 1
		        
		if flag == 1:
			messagebox.showinfo("Contact Management", "Deleted successfully")
		else:
			messagebox.showinfo("Contact Management", "Check entered name")
			
		conn.close()

	elif var.get()==2:
		flag = 0
		s1 = entry1_Root.get()
		s2 = entry2_Root.get()

		if s1 == "":
			messagebox.showerror("Contact Management", "Enter proper name")
			return

		try:
			val = int(s2)
		except ValueError:
			messagebox.showerror("Contact Management", "Enter proper number")
			return

		conn = sqlite3.connect('Contacts.db')
		print ("Opened database successfully")

		cursor = conn.execute("SELECT * from Contacts order by name")
		for row in cursor:
			name = row[1]
			number = str(row[2])
			num = str(s2)
			if (s1 == name) & (num == number) :
				conn.execute("DELETE from Contacts where NAME=(?) AND NUMBER=(?)",(s1,s2))
				conn.commit()
				flag = 1

		if flag == 1:
			messagebox.showinfo("Contact Management", "Deleted successfully")
		else:
			messagebox.showinfo("Contact Management", "Check entered details")
		    
		conn.close()


	Display_Window()
	return

def Search_Window():
	t.delete(1.0, END) 

	flag = 0
	s1 = entry1_Root.get()
	conn = sqlite3.connect('Contacts.db')
	print ("Opened database successfully")


	cursor = conn.execute("SELECT * from Contacts order by name")
	for row in cursor:
		name = row[1]
		number = row[2]
		if s1 == name:
			t.insert('insert', "%s:%s\n"%(name,number))
			flag = 1

	if flag == 0:
		t.insert('insert', "NO SUCH CONTACT")

	conn.close()
	return

def Edit_Window():
	print(str(var.get()))
	print(str(checkVar.get()))
	if var.get()==1:
		flag = 0
		s1 = entry1_Root.get()
		s2 = entry2_Root.get()


		if s1 == "":
			messagebox.showerror("Contact Management", "Enter proper name")
			return

		conn = sqlite3.connect('Contacts.db')
		print ("Opened database successfully")

		conn.execute("UPDATE Contacts set NAME = (?) where NAME = (?)",(s2,s1))
		conn.commit()
		flag=1
		        
		if flag == 1:
			messagebox.showinfo("Contact Management", "Edited successfully")
		else:
			messagebox.showinfo("Contact Management", "Check entered name")
			
		conn.close()


	elif var.get()==2:
		flag = 0
		s1 = entry1_Root.get()
		s2 = entry2_Root.get()
		s3 = entry3_Root.get()


		if s1 == "":
			messagebox.showerror("Contact Management", "Enter proper name")
			return

		conn = sqlite3.connect('Contacts.db')
		print ("Opened database successfully")

		conn.execute("UPDATE Contacts set NUMBER = (?) where NAME = (?) and NUMBER = (?)",(s3,s1,s2))
		conn.commit()
		flag=1
		        
		if flag == 1:
			messagebox.showinfo("Contact Management", "Edited successfully")
		else:
			messagebox.showinfo("Contact Management", "Check entered name")
			
		conn.close()


	Display_Window()
	return

def Edit_Changer():
	if checkVar.get()==1 and var.get()==1:
		print("YES")
		label1_Root.config(text="Enter Old Name:")
		label2_Root.config(text="Enter New Name:")
		label3_Root.config(text="",state="disabled")
		entry3_Root.config(state="disabled")

	elif checkVar.get()==1 and var.get()==2:
		label1_Root.config(text="Enter Name:")
		label2_Root.config(text="Enter Old Number:")
		label3_Root.config(text="Enter New Number:",state="normal")
		entry3_Root.config(state="normal")

	elif checkVar.get()==0:
		print("NO")
		label1_Root.config(text="Enter Name:")
		label2_Root.config(text="Enter Number:")
		label3_Root.config(text="",state="disabled")
		entry3_Root.config(state="disabled")

	return


root=Tk()
var=IntVar()
checkVar=IntVar()

root.title("Contacts Management")
root.geometry("470x335")
root.configure(background="gray24")
root.wm_iconbitmap('if_ic_perm_contact_cal_48px_352586.ico')
main_label_Root= Label(root,text="Contacts Management",font = "Calibri 14 bold underline ",bg='gray24',fg='thistle1' )
main_label_Root.grid(row=0,sticky="S",columnspan=2)

label1_Root= Label(root,text="Enter Name:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
label1_Root.grid(row=1,sticky='S',column=0)
entry1_Root= Entry(root) 
entry1_Root.grid(row=1 , column=1)
label2_Root = Label(root,text="Enter Number:",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
label2_Root.grid(row=2,sticky='S',column=0)
entry2_Root= Entry(root) 
entry2_Root.grid(row=2 , column=1)
label3_Root = Label(root,text="",font = "Calibri 10 ",bg='gray24',fg='thistle1' )
label3_Root.grid(row=3,sticky='S',column=0)
entry3_Root= Entry(root) 
entry3_Root.grid(row=3 , column=1)

label3_Root.config(state="disabled")
entry3_Root.config(state="disabled")

radio1_Root = Radiobutton(root, text="Name", variable=var, value=1,command=Edit_Changer)
radio2_Root = Radiobutton(root, text="Number", variable=var, value=2,command=Edit_Changer)
radio1_Root.grid(row=5, column=0)
radio2_Root.grid(row=5, column=1)

check1_Root = Checkbutton(root, text = "Edit", variable = checkVar, onvalue = 1, offvalue = 0, command=Edit_Changer)
check1_Root.grid(row=12, column=0)

'''Button creation and addition'''
button1_Root = Button(root , text="Add" ,command=Add_Window,font = "Calibri 10 bold ",bg='gray40',fg='white' ,width=16,height=2)
button2_Root = Button(root , text="Delete",command=Delete_Window,font = "Calibri 10 bold ",bg='gray40',fg='white'  ,width=16,height=2)
button3_Root = Button(root , text="Search" ,command=Search_Window,font = "Calibri 10 bold ",bg='gray40',fg='white', width=16,height=2)
button4_Root = Button(root , text="Edit" ,command=Edit_Window,font = "Calibri 10 bold ",bg='gray40',fg='white',width=16,height=2)
button5_Root = Button(root, text="Quit",command=root.destroy,bg='gray40', font = "Calibri 10 bold ",fg='white',width=16,height=2)
button6_Root = Button(root , text="Display" ,command=Display_Window,font = "Calibri 10 bold ",bg='gray40',fg='white', width=16,height=2)

button1_Root.grid(row=6, column=0)
button2_Root.grid(row=6, column=1)
button3_Root.grid(row=8, column=0)
button4_Root.grid(row=8, column=1)
button5_Root.grid(row=10, column=0)
button6_Root.grid(row=10, column=1)

root.grid_rowconfigure(5, minsize=20)
root.grid_rowconfigure(7, minsize=20)
root.grid_rowconfigure(9, minsize=20)
root.grid_rowconfigure(11, minsize=20)

s = Scrollbar(root)
t = Text(root , height=15, width=25)

t.grid(row=0,column=3,rowspan=11)
s.grid(row=0,column=4,rowspan=11,sticky='ns')
s.config(command=t.yview)
t.config(yscrollcommand=s.set)

Display_Window()


root.mainloop()