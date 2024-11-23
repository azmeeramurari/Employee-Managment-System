from customtkinter import * # type: ignore
from PIL import Image # type: ignore
from tkinter import ttk,messagebox
import database
#functions


# def delete_all():
#     result=messagebox.askyesno('Confirm','Do you want to delete all records?')
#     if result:
#         database.deleteall_records()
    

def show_all():
    treeview_data()
    SearchEntry.delete(0,END)
    SearchBox.set('Search By')

def search_employee():
    if SearchEntry.get()=='':
        messagebox.showerror("Error","Enter value to search")
    elif SearchBox.get()=='Search By':
        messagebox.showerror("Error","Please select an option to search")
    else:
        searched_data=database.search(SearchBox.get(),SearchEntry.get())     
        tree.delete(*tree.get_children())
    for employee in searched_data:
        tree.insert('',END,values=employee) # type: ignore
        

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select an item to delete")
    else:
        database.delete(IDEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Employee deleted successfully")
        

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select any data to update")
    else:
       database.update(IDEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), SalaryEntry.get())
       treeview_data()
       clear()
       messagebox.showinfo('Success','Data is updated')


def selection(event):
    selection_item = tree.selection()  # Get the selected item(s)
    if selection_item:  # Ensure something is selected
        selected_item = selection_item[0]  # Get the first item from the selection
        row = tree.item(selected_item)['values']  # Access its values
        clear()#clear the prev data which is displayed in the text box
        IDEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        SalaryEntry.insert(0,row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    IDEntry.delete(0,END) # type: ignore
    nameEntry.delete(0,END) #type: ignore
    phoneEntry.delete(0,END) # type: ignore
    roleBox.set('Select')
    genderBox.set('Select')
    SalaryEntry.delete(0,END) # type: ignore

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee) # type: ignore
        
    
    

def add_employee():
    if IDEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or SalaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    
    elif database.id_exists(IDEntry.get()):
          messagebox.showerror("Error", "ID already exists.")
   
        
    else:
        database.insert(IDEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),SalaryEntry.get())
        treeview_data()
        clear() # type: ignore
        messagebox.showinfo('Success','Data is added')

window=CTk() # type: ignore
window.title("Employee Management System")
window.configure(fg_color='#ADD8E6')
window.geometry('930x580+100+100')
window.resizable(0,0)

logo=CTkImage(Image.open('bg.jpg'),size=(930,158)) # type: ignore
logoLabel=CTkLabel(window,image=logo,text='') # type: ignore
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#ADD8E6') # type: ignore
leftFrame.grid(row=1,column=0)

IDLabel=CTkLabel(leftFrame,text='   ID',font =('Arial',18,'bold')) # type: ignore
IDLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

IDEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180) # type: ignore
IDEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='NAME',font =('Arial',18,'bold')) # type: ignore
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180) # type: ignore
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='PHONE',font =('Arial',18,'bold')) # type: ignore
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180) # type: ignore
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='ROLE',font =('Arial',18,'bold')) # type: ignore
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=['Web Developer','Cloud Architect','Techinal Writer','Network Engineer','DevOps','Data Scientist','IT Manager','UX/UI Designer']



roleBox = CTkComboBox(leftFrame, values=role_options, width=180,font=('arial',15,'bold'),state='readonly') # type: ignore
roleBox.grid(row=3,column=1)
roleBox.set(["Select"])

genderLabel=CTkLabel(leftFrame,text='GENDER',font =('Arial',18,'bold')) # type: ignore
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female']
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180,font=('arial',15,'bold'),state='readonly') # type: ignore
genderBox.grid(row=4,column=1)
genderBox.set(["Select"])

SalaryLabel=CTkLabel(leftFrame,text='SALARY',font =('Arial',18,'bold')) # type: ignore
SalaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

SalaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180) # type: ignore
SalaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window) # type: ignore
rightFrame.grid(row=1,column=1)


Search_options = ['Id', 'Name', 'Role', 'Gender', 'Salary']
SearchBox = CTkComboBox(rightFrame, values=Search_options, state='readonly') # type: ignore
SearchBox.grid(row=0, column=0)
SearchBox.set('Search By')

SearchEntry=CTkEntry(rightFrame) # type: ignore
SearchEntry.grid(row=0,column=1)

SearchButton=CTkButton(rightFrame,text='Search',cursor='hand2',width=100,command=search_employee) # type: ignore
SearchButton.grid(row=0,column=2)

ShowallButton=CTkButton(rightFrame,text='Show All',cursor='hand2',width=100,command=show_all) # type: ignore
ShowallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='EMP ID')
tree.heading('Name',text='EMP NAME')
tree.heading('Phone',text='PHONE')
tree.heading('Role',text='ROLE')
tree.heading('Gender',text='GENDER')
tree.heading('Salary',text='SALARY')

tree.config(show='headings')
tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=100)
tree.column('Role',width=150)
tree.column('Gender',width=100)
tree.column('Salary',width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))
style.configure('Treeview',font=('arial',9,'bold'))

scrollbar=ttk.Scrollbar(rightFrame,orient='vertical',command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#add8e6') # type: ignore
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, cursor='hand2', corner_radius=15, command=lambda: clear(True))  # type: ignore
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,cursor='hand2',corner_radius=15,command=add_employee) # type: ignore
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,cursor='hand2',corner_radius=15,command=update_employee) # type: ignore
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,cursor='hand2',corner_radius=15,command=delete_employee) # type: ignore
deleteButton.grid(row=0,column=3,pady=5,padx=5)

# deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,cursor='hand2',corner_radius=15,command=delete_all) # type: ignore
# deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()

window.bind('<ButtonRelease>',selection)


window.mainloop()


