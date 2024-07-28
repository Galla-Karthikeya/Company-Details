from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import database
import pymysql

# functionality part

def add_employee():
    if identry.get() == '' or nameentry.get() == '' or phoneentry.get() == '' or salaryentry.get() == '':
        messagebox.showerror(title = 'Error', message='All Fields are Required')
    elif not identry.get().startswith('E'):
        messagebox.showerror(title='Error', message='Invalid ID format use "E" followed by a number (e.g., "E285").')
    else:
        database.connect_database()
        database.datachecking(identry.get())
        database.insert(identry.get(), nameentry.get(), phoneentry.get(), rolebox.get(), genderbox.get(), salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo(title='Sucess', message='Data Added Sucessfully')

def clear(value = False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0, END)
    nameentry.delete(0, END)
    phoneentry.delete(0, END)
    salaryentry.delete(0, END)
    rolebox.set('Select')
    genderbox.set('Select')
# to remove the employees list from the input boxes

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values = employee)
# To insert the values from the box to the table


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        identry.insert(0, row[0])
        nameentry.insert(0, row[1])
        phoneentry.insert(0, row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryentry.insert(0, row[5])
# to print the values from table to the box

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror(title = 'Error', message='Select Data to update')
    else:
        database.update(identry.get(), nameentry.get(), phoneentry.get(), rolebox.get(), genderbox.get(), salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo(title = 'Sucess', message='Data has Updated')

def delete_employee():
    selected = tree.selection()
    if not selected:
        messagebox.showerror(title='Error', message='Select Data To delete')
    else:
        print(identry.get())
        database.delete_(identry.get())
        treeview_data()
        clear()
        messagebox.showinfo(title = "Sucess", message='Record Deleted Sucessfully')

def delete_all():
    result = messagebox.askyesno('Confirm', 'Do you really want to delete all the records?')
    if result:
        messagebox.showwarning(title='Warning', message='All Your records will be deleted Permanently')
        database.deleteall()
        treeview_data()
        messagebox.showinfo(title='Sucess', message='All the Records are Deleted')
    else:
        pass

def search_records():
    if searchentry.get() == '':
        messagebox.showerror(title='Error', message='Enter Value to Search')
    elif searchbox.get() == 'Search By':
        messagebox.showerror(title='Error', message='Select any field in Search Box')
    else:
        records = database.search(searchbox.get(), searchentry.get())
        if records:
            treeview_search()
            messagebox.showinfo(title='Sucess', message='Records Available')
        else:
            messagebox.showerror(title='Error', message='No records Found')


def treeview_search():
    employees = database.search(searchbox.get(), searchentry.get())
    tree.delete(*tree.get_children())
    print(employees)
    for employee in employees:
        print(employee)
        tree.insert('', END, values = employee)

def showAll():
    treeview_data()
    searchentry.delete(0, END)
    searchbox.set('Search By')


ems_window = CTk()
ems_window.title('Employee Mangament System')
ems_window.geometry('920x650+300+200')
ems_window.configure(fg_color='#181B20')
ems_window.resizable(False, False)
logo = CTkImage(Image.open(r'Images\1117_U1RVRElPIEtBVCAxMTctMTAcrop.jpg'), size=(900, 219))
logolabel = CTkLabel(ems_window, image=logo, text='')
logolabel.grid(row = 0, column = 0, columnspan = 2)

leftframe = CTkFrame(ems_window, fg_color='#181B20')
leftframe.grid(row = 1, column = 0)

idlabel = CTkLabel(leftframe, text= 'Id', font = ('arial', 18, 'bold'))
idlabel.grid(row = 0, column = 0, padx = (5, 20), pady = 15, sticky = 'w')
identry = CTkEntry(leftframe, font = ('arial', 12), bg_color='white', fg_color='black', width=180, border_color='black')
identry.grid(row = 0, column = 1, pady = 15, padx = (0, 10))

namelabel = CTkLabel(leftframe, text= 'Name', font = ('arial', 18, 'bold'))
namelabel.grid(row = 1, column = 0, padx = (5, 20), pady = 15, sticky = 'w')
nameentry = CTkEntry(leftframe, font = ('arial', 12), bg_color='white', fg_color='black', width=180, border_color='black')
nameentry.grid(row = 1, column = 1, pady = 15, padx = (0, 10))

phonelabel = CTkLabel(leftframe, text= 'Phone', font = ('arial', 18, 'bold'))
phonelabel.grid(row = 2, column = 0, padx = (5, 20), pady = 15, sticky = 'w')
phoneentry = CTkEntry(leftframe, font = ('arial', 12), bg_color='white', fg_color='black', width=180, border_color='black')
phoneentry.grid(row = 2, column = 1, pady = 15, padx = (0, 10))

rolelabel = CTkLabel(leftframe, text= 'Role', font = ('arial', 18, 'bold'))
rolelabel.grid(row = 3, column = 0, padx = (5, 20), pady = 15, sticky = 'w')
role_options = ['Select', 'Software Engineer', 'Full stack Developer', 'Python Developer', 'Machine Learning Engineer', 'AI Engineer', 'Data Scientist', 'Business Analysist', 'Cloud Architect', 'DevOps Engineer', 'Network Engineer', 'UX/UI Designer', 'HR Manager', 'Designer', 'Tester', 'Marketing', 'Project Manager']
rolebox = CTkComboBox(leftframe, values = role_options, width=180, bg_color='white', fg_color='black', font = ('arial', 12), state= 'readonly', border_color='black')
rolebox.grid(row = 3, column = 1)
rolebox.set(role_options[0])


genderlabel = CTkLabel(leftframe, text= 'Gender', font = ('arial', 18, 'bold'))
genderlabel.grid(row = 4, column = 0, padx = (5, 20), pady = 15, sticky = 'w')
gender_options = ['Select', 'Male', 'Female', 'Others']
genderbox = CTkComboBox(leftframe, values = gender_options, width=180, font=  ('arial', 12), bg_color='white', fg_color='black', state= 'readonly', border_color='black')
genderbox.grid(row = 4, column = 1)
genderbox.set(gender_options[0])

salarylabel = CTkLabel(leftframe, text= 'Salary', font = ('arial', 18, 'bold'))
salarylabel.grid(row = 5, column = 0, padx = (5, 20), pady = 15, sticky = 'w')
salaryentry = CTkEntry(leftframe, font = ('arial', 12), bg_color='white', fg_color='black', width=180, border_color='black')
salaryentry.grid(row = 5, column = 1, pady = 15, padx = (0, 10))

rightframe = CTkFrame(ems_window, bg_color='#D8D8D8', corner_radius=16, fg_color='#D8D8D8')
rightframe.grid(row = 1, column = 1)

search_options = ['Search By', 'ID', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchbox = CTkComboBox(rightframe, values = search_options, state='readonly')
searchbox.grid(row = 0, column = 0)
searchbox.set('Search By')

searchentry = CTkEntry(rightframe)
searchentry.grid(row = 0, column = 1)

searchbutton = CTkButton(rightframe, text='Search', fg_color='#1F6797', font=('arial', 15, 'bold'), command=search_records)
searchbutton.grid(row = 0, column = 2)

showallbutton = CTkButton(rightframe, text='Show All', fg_color='#1F6797', font=('arial', 15, 'bold'), command= showAll)
showallbutton.grid(row = 0, column = 3, pady = 5, padx = (0, 10), columnspan = 2)

tree = ttk.Treeview(rightframe, height= 10)
tree.grid(row = 1, column = 0, columnspan = 4)

tree['columns'] = ('Id', 'Name','Phone', 'Role', 'Gender', 'Salary')
tree.heading('Id', text = 'ID')
tree.heading('Name', text='Name')
tree.heading('Phone', text = 'Phone')
tree.heading('Role', text = 'Role')
tree.heading('Gender', text = 'Gender')
tree.heading('Salary', text = 'Salary')

tree.config(show = 'headings')
tree.column('Id', anchor=CENTER, width=70)
tree.column('Name', anchor=CENTER, width=120)
tree.column('Phone', anchor = CENTER, width = 100)
tree.column('Role', anchor=CENTER, width=120)
tree.column('Gender', anchor=CENTER, width=70)
tree.column('Salary', anchor=CENTER, width=80)

style = ttk.Style()
style.configure('Treeview.Heading', font = ('arial', 10, 'bold'), background = '#181B20')
style.configure('Treeview', font = ('arial', 10), rowheight = 26 ,background = 'black', foreground = 'white')

scrollbar = ttk.Scrollbar(rightframe, orient=VERTICAL, command=tree.yview)
scrollbar.grid(row = 1, column = 4, sticky = 'ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(ems_window, fg_color='#181B20')
buttonFrame.grid(row = 2, column = 0, columnspan = 2, pady = 15)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command= lambda: clear(True))
newButton.grid(row = 0, column = 0, pady = 5, padx = 5)

newButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=add_employee)
newButton.grid(row = 0, column = 1, pady = 5, padx = 5)

newButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command = update_employee)
newButton.grid(row = 0, column = 2, pady = 5, padx = 5)

newButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command = delete_employee)
newButton.grid(row = 0, column = 3, pady = 5, padx = 5)

newButton = CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, corner_radius=15, command = delete_all)
newButton.grid(row = 0, column = 4, pady = 5, padx = 5)

treeview_data()
# selection(True)
ems_window.bind('<ButtonRelease>',selection)
ems_window.mainloop()