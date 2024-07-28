import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


# # Functionality
# def on_email(value, emailentry):
#     if emailentry.get() == 'Enter Your EmailID':
#         emailentry.delete(0, END)
# def on_enter(value, userentry):
#     if userentry.get() == 'Enter Your Name':
#         userentry.delete(0, END)
#
# def on_pass(value, passentry):
#     if passentry.get() == 'Enter Your Password':
#         passentry.delete(0, END)
#         passentry.config(show='*')


def signin():
    if(emailentry.get() == '' or userentry.get() == '' or passentry.get() == ''):
        messagebox.showerror(title='Error', message='All Fields are required to login')
    else:
        try:
            conn = pymysql.connect(host='localhost', user='root', password='karthi')
            mycursor = conn.cursor()
        except:
            messagebox.showerror(title="Error", message='Connection is not establish Try Again')
            return

        print('Connection Done')

        try:
            query = 'create database higherroles'
            mycursor.execute(query)
            mycursor.execute('use higherroles')
            query = 'create table signin_details(ID int auto_increment primary key not null, EmailID varchar(50), Username varchar(50), password varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use higherroles')

        query = 'select * from signin_details where EmailID = %s'
        mycursor.execute(query, args = emailentry.get())

        email = mycursor.fetchone()
        if (email != None):
            messagebox.showerror(title='Error', message='Email ID is already Exist')

        else:
            query = 'insert into signin_details(EmailID, Username, Password) values(%s, %s, %s)'
            mycursor.execute(query, args=(emailentry.get(), userentry.get(), passentry.get()))

            conn.commit()
            conn.close()
            mycursor.close()
            messagebox.showinfo(title='Sucess', message='Registration is Sucessfull')
            signin_window.destroy()

            import login


signin_window = Tk()
signin_window.title('SignIn')
signin_window.resizable(False, False)
signin_window.geometry('900x540+50+50')
signin_window.config(bg='white')

img = Image.open(r'C:\Users\A\PycharmProjects\Company Project\Images\rescale.jpg')
img_fix = ImageTk.PhotoImage(img)
imagelabel = Label(signin_window, image=img_fix, bd=0, bg='white')
imagelabel.place(x= 50, y = 100)


#email entry
emaillabel = Label(signin_window, text='EmailID', font=('Microsoft Yahei UI Light', 12, 'bold'), bd = 0, bg='white', fg='#5456A3')
emaillabel.place(x = 450, y = 90)
emailentry = Entry(signin_window, width=26, font=('Microsoft Yahei UI Light', 12), bd = 0)
emailentry.place(x = 450, y = 130)
# emailentry.insert(0, 'Enter Your EmailID')
# emailentry.bind('<FocusIn>', lambda event: on_email(event, emailentry))
frame = Frame(width=250, height=2, bg= '#CAD9E5').place(x = 450, y = 156)

# User entry
userlabel = Label(signin_window, text='Username', font=('Microsoft Yahei UI Light', 12, 'bold'), bd = 0, bg='white', fg='#5456A3')
userlabel.place(x = 450, y = 180)
userentry = Entry(signin_window, width=26, font=('Microsoft Yahei UI Light', 12), bd=0)
userentry.place(x=450, y=220)
# userentry.insert(0, 'Enter Your Name')
# userentry.bind('<FocusIn>', lambda event: on_enter(event, userentry))
frame = Frame(width=250, height=2, bg= '#CAD9E5').place(x = 450, y = 246)

# Password entry
passlabel = Label(signin_window, text='Password', font=('Microsoft Yahei UI Light', 12, 'bold'), bd = 0, bg='white', fg='#5456A3')
passlabel.place(x = 450, y = 270)
passentry = Entry(signin_window, width=26, font=('Microsoft Yahei UI Light', 12), bd=0)
passentry.place(x=450, y=310)
# passentry.insert(0, 'Enter Your Password')
# passentry.bind('<FocusIn>', lambda event: on_pass(event, passentry))
frame = Frame(width=250, height=2, bg= '#CAD9E5').place(x = 450, y = 336)

signin = Button(signin_window, text='Sign In' ,width=20, height=1, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='#00519F', fg='white', activeforeground='black',activebackground='#00A0FF', command=signin)
signin.place(x = 470, y = 400)
signin_window.mainloop()