from customtkinter import * # type: ignore
from PIL import Image # type: ignore
from tkinter import filedialog, messagebox

def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror("Error", "Please fill in all fields")
    elif usernameEntry.get()=='admin' and passwordEntry.get()=='admin':
        messagebox.showinfo('Success ', 'Login Successful')
    else:
        messagebox .showerror("Error", "Invalid username or password")
        root.destroy()
        import ems

# Create the main window
root = CTk() # type: ignore
root.geometry('930x478')  # Corrected the window size format
root.resizable(0, 0)  # Prevent resizing
root.title('Login page')  # Set the window title
image = CTkImage(Image.open('cover.jpg'), size=(930, 478)) # type: ignore
imageLabel=CTkLabel(root,image=image,text ='') # type: ignore
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Managment System',bg_color="#fff",font=('Goudy Old Style',20,'bold'),text_color="dark blue") # type: ignore
headingLabel.place(x=30,y=100)

usernameEntry= CTkEntry(root,placeholder_text='Enter Your Username',width=180) # type: ignore
usernameEntry.place(x=70,y=150)

passwordEntry= CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*') # type: ignore
passwordEntry.place(x=70,y=200)

loginButton=CTkButton(root,text="Login",cursor='hand2',command=login) # type: ignore
loginButton.place(x=70,y=250)
# Start the application
root.mainloop()
