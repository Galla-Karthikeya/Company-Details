from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Functionality
def on_email(value, emailentry):
    if emailentry.get() == 'Enter Your EmailID':
        emailentry.delete(0, END)
def on_enter(value, userentry):
    if userentry.get() == 'Enter Your Name':
        userentry.delete(0, END)

def on_pass(value, passentry):
    if passentry.get() == 'Enter Your Password':
        passentry.delete(0, END)
        passentry.config(show='*')


def toggle_password(show_password, passentry, eyeButton, open_eye, close_eye):
    if show_password[0]:
        passentry.config(show='')
        eyeButton.config(image=open_eye)
    else:
        passentry.config(show='*')
        eyeButton.config(image=close_eye)
    show_password[0] = not show_password[0]


def login():
    if(userentry.get() == '' or passentry.get() == '' or userentry.get() == 'Enter Your Name' or passentry.get() == 'Enter Your Password'):
        messagebox.showerror(title='Error', message='All Fields are required to login')
    else:
        try:
            conn = pymysql.connect(host = 'localhost', user='root', password='karthi')
            mycursor = conn.cursor()
        except:
            messagebox.showerror(title="Error", message='Connection is not establish Try Again')
            return

        try:
            query = 'create database higherroles'
            mycursor.execute(query)
            mycursor.execute('use higherroles')
            query = 'create table signin_details(ID int auto_increment primary key not null, EmailID varchar(50), Username varchar(50), password varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use higherroles')

        query = 'select Username, password from signin_details where EmailID = %s'
        mycursor.execute(query, args = emailentry.get())

        record = mycursor.fetchone()
        mycursor.close()
        conn.close()
        if (record != None):
            db_username, db_password = record
            if(db_username == userentry.get()):
                if (db_password == passentry.get()):
                    messagebox.showinfo(title='Sucess', message='Login Sucessfull')
                    root.destroy()
                    import ems
                else:
                    messagebox.showerror(title='Error', message='Incorrect Password')
            else:
                messagebox.showerror(title='Error', message='Incorrect Username')
        else:
            messagebox.showerror(title='Error', message='Details are Incorrect')

root = Tk()
root.title('Login')
root.geometry('870x500+300+200')
root.configure(bg='white')
root.resizable(False, False)

# Create a white background frame
bg_frame = Frame(master=root, width=900, height=540, bg='white')
bg_frame.place(x=0, y=0)

# Load and place the login image
img_open = Image.open(r'C:\Users\A\PycharmProjects\Company Project\Images\login.png')
img = ImageTk.PhotoImage(img_open)
imglabel = Label(master=root, image=img, bd=0)
imglabel.place(x=50, y=80)

# Heading label
headinglabel = Label(root, text='Employee Management System', bd=0, bg='white',
                     font=('Goudy Old Style', 18, 'bold'), fg='#5D4BBE')
headinglabel.place(x=470, y=80)

#email entry
emailentry = Entry(root, width=26, font=('Microsoft Yahei UI Light', 12))
emailentry.place(x = 500, y = 160)
emailentry.insert(0, 'Enter Your EmailID')
emailentry.bind('<FocusIn>', lambda event: on_email(event, emailentry))

# User entry
userentry = Entry(root, width=26, font=('Microsoft Yahei UI Light', 12))
userentry.place(x=500, y=220)
userentry.insert(0, 'Enter Your Name')
userentry.bind('<FocusIn>', lambda event: on_enter(event, userentry))

# Password entry
passentry = Entry(root, width=26, font=('Microsoft Yahei UI Light', 12))
passentry.place(x=500, y=280)
passentry.insert(0, 'Enter Your Password')
passentry.bind('<FocusIn>', lambda event: on_pass(event, passentry))


# Creating the eye button for toggling password visibility
show_password = [False]

open_eye_img = Image.open(r'C:\Users\A\PycharmProjects\Company Project\Images\file.jpg')
open_eye = ImageTk.PhotoImage(open_eye_img, size=(50, 50))

close_eye_img = Image.open(r'C:\Users\A\PycharmProjects\Company Project\Images\file1.jpg')
close_eye = ImageTk.PhotoImage(close_eye_img, size=(50, 50))

eyeButton = Button(root, image=close_eye ,bg='white', bd=0, cursor='hand2', activebackground='white',
                   command=lambda: toggle_password(show_password, passentry, eyeButton, open_eye, close_eye))
eyeButton.place(x=750, y=270)

# Login button
login = Button(root, text='Login', font=('Microsoft Yahei UI Light', 12, 'bold'), bg='#2F93F3',
               width=20, height=1, fg='white', bd=0, activebackground='white', activeforeground='#2F93F3', command=login)
login.place(x=510, y=340)

root.mainloop()
