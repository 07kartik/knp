from tkinter import *
import tkinter.ttk as ttk

mainWindow = Tk()
mainWindow.geometry('300x200')
mainWindow.resizable(0,0)
mainWindow.title('Project Management')
# mainWindow.mainloop()

# loginFrame = Frame(mainWindow)
viewFrame   = Frame(mainWindow)
insertFrame = Frame(mainWindow)
updateFrame = Frame(mainWindow)
deleteFrame = Frame(mainWindow)



def openViewFrame   () :
	if (insertFrame) :
		insertFrame.grid_forget()
	if (updateFrame) :
		updateFrame.grid_forget()
	if (deleteFrame) :
		deleteFrame.grid_forget()

	classNameViewLabel= ttk.Label(viewFrame, text='Class')
	classNameViewLabel.grid(row='2', column='0')
	classNameViewEntry = ttk.Entry(viewFrame)
	classNameViewEntry.grid(row='2', column='1')

	rollNumberViewLabel= ttk.Label(viewFrame, text='Roll No')
	rollNumberViewLabel.grid(row='3', column='0')
	rollNumberViewEntry = ttk.Entry(viewFrame)
	rollNumberViewEntry.grid(row='3', column='1')

	classNameViewFrameValue = classNameViewEntry.get()
	rollNumberViewFrameValue = rollNumberViewEntry.get()

	viewViewButton = ttk.Button(viewFrame, text='View')
	viewViewButton.grid(row='7', columnspan='2')
	viewFrame.grid()

def openInsertFrame () :
	if (viewFrame) :
		viewFrame.grid_forget()
	if (updateFrame) :
		updateFrame.grid_forget()
	if (deleteFrame) :
		deleteFrame.grid_forget()
	# insertFrame = Frame(mainWindow)
	fnameInsertLabel= ttk.Label(insertFrame, text='First Name')
	fnameInsertLabel.grid(row='0', column='0')
	fnameInsertEntry = ttk.Entry(insertFrame)
	fnameInsertEntry.grid(row='0', column='1')

	lnameInsertLabel= ttk.Label(insertFrame, text='Last Name')
	lnameInsertLabel.grid(row='1', column='0')
	lnameInsertEntry = ttk.Entry(insertFrame)
	lnameInsertEntry.grid(row='1', column='1')

	classNameInsertLabel= ttk.Label(insertFrame, text='Class')
	classNameInsertLabel.grid(row='2', column='0')
	classNameInsertEntry = ttk.Entry(insertFrame)
	classNameInsertEntry.grid(row='2', column='1')

	rollNumberInsertLabel= ttk.Label(insertFrame, text='Roll No')
	rollNumberInsertLabel.grid(row='3', column='0')
	rollNumberInsertEntry = ttk.Entry(insertFrame)
	rollNumberInsertEntry.grid(row='3', column='1')

	projectNameInsertLabel= ttk.Label(insertFrame, text='Project Name')
	projectNameInsertLabel.grid(row='4', column='0')
	projectNameInsertEntry = ttk.Entry(insertFrame)
	projectNameInsertEntry.grid(row='4', column='1')

	contactNumberInsertLabel= ttk.Label(insertFrame, text='Contact No')
	contactNumberInsertLabel.grid(row='5', column='0')
	contactNumberInsertEntry = ttk.Entry(insertFrame)
	contactNumberInsertEntry.grid(row='5', column='1')

	emailIdInsertLabel= ttk.Label(insertFrame, text='Email ID')
	emailIdInsertLabel.grid(row='6', column='0')
	emailIdInsertEntry = ttk.Entry(insertFrame)
	emailIdInsertEntry.grid(row='6', column='1')

	fnameInsertFrameValue = fnameInsertEntry.get()
	lnameInsertFrameValue = lnameInsertEntry.get()
	classNameInsertFrameValue = classNameInsertEntry.get()
	rollNumberInsertFrameValue = rollNumberInsertEntry.get()
	projectNameInsertFrameValue = projectNameInsertEntry.get()
	contactNumberInsertFrameValue = contactNumberInsertEntry.get()
	emailIdInsertFrameValue = emailIdInsertEntry.get()

	insertInsertButton = ttk.Button(insertFrame, text='Insert')
	insertInsertButton.grid(row='7', columnspan='2')
	insertFrame.grid()

def openUpdateFrame () :
	if (viewFrame) :
		viewFrame.grid_forget()
	if (insertFrame) :
		insertFrame.grid_forget()
	if (deleteFrame) :
		deleteFrame.grid_forget()
	classNameUpdateLabel= ttk.Label(updateFrame, text='Class')
	classNameUpdateLabel.grid(row='2', column='0')
	classNameUpdateEntry = ttk.Entry(updateFrame)
	classNameUpdateEntry.grid(row='2', column='1')

	rollNumberUpdateLabel= ttk.Label(updateFrame, text='Roll No')
	rollNumberUpdateLabel.grid(row='3', column='0')
	rollNumberUpdateEntry = ttk.Entry(updateFrame)
	rollNumberUpdateEntry.grid(row='3', column='1')

	classNameUpdateFrameValue = classNameUpdateEntry.get()
	rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()

	okkkkkUpdateButton = ttk.Button(updateFrame, text='Okkkkk')
	okkkkkUpdateButton.grid(row='7', columnspan='2')
	updateFrame.grid()

def openDeleteFrame () :
	if (viewFrame) :
		viewFrame.grid_forget()
	if (insertFrame) :
		insertFrame.grid_forget()
	if (updateFrame) :
		updateFrame.grid_forget()
	fnameDeleteLabel= ttk.Label(deleteFrame, text='First Name')
	fnameDeleteLabel.grid(row='0', column='0')
	fnameDeleteEntry = ttk.Entry(deleteFrame)
	fnameDeleteEntry.grid(row='0', column='1')

	lnameDeleteLabel= ttk.Label(deleteFrame, text='Last Name')
	lnameDeleteLabel.grid(row='1', column='0')
	lnameDeleteEntry = ttk.Entry(deleteFrame)
	lnameDeleteEntry.grid(row='1', column='1')

	classNameDeleteLabel= ttk.Label(deleteFrame, text='Class Name')
	classNameDeleteLabel.grid(row='2', column='0')
	classNameDeleteEntry = ttk.Entry(deleteFrame)
	classNameDeleteEntry.grid(row='2', column='1')

	rollNumberDeleteLabel= ttk.Label(deleteFrame, text='Roll No')
	rollNumberDeleteLabel.grid(row='3', column='0')
	rollNumberDeleteEntry = ttk.Entry(deleteFrame)
	rollNumberDeleteEntry.grid(row='3', column='1')

	fnameDeleteFrameValue = fnameDeleteEntry.get()
	lnameDeleteFrameValue = lnameDeleteEntry.get()
	classNameDeleteFrameValue = classNameDeleteEntry.get()
	rollNumberDeleteFrameValue = rollNumberDeleteEntry.get()

	deleteDeleteButton = ttk.Button(deleteFrame, text='Delete')
	deleteDeleteButton.grid(row='4', columnspan='2')
	deleteFrame.grid()



menubar = Menu(mainWindow)
menubar.add_command(label='View', command=openViewFrame)
menubar.add_command(label='Insert', command=openInsertFrame)
menubar.add_command(label='Update', command=openUpdateFrame)
menubar.add_command(label='Delete', command=openDeleteFrame)
mainWindow.config(menu=menubar)
 


mainWindow.mainloop()