from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk
import os
import csv
import subprocess

window = Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg='#FFDED9')
window.resizable(False, False)


def halaman_signup(app):
    for widget in app.winfo_children():
        widget.destroy()
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            # Check if CSV file exists
            cwd = os.getcwd()
            file_exists = os.path.exists('{}\\datasheet.csv'.format(cwd))
            print(f"File exists: {file_exists}")

            # Open the CSV file in append mode
            with open('datasheet.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                
                # If the file does not exist, write the header
                if not file_exists:
                    writer.writerow(['Username', 'Password'])
                    print("Header written to file")

                file.seek(0)  # Move cursor to the beginning of the file
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row if it exists
                for row in reader:
                    if row and row[0] == username:
                        messagebox.showerror('Error', 'Username already exists')
                        return

            # Append the new user data
            with open('datasheet.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password])
                print(f"New user {username} written to file")

            messagebox.showinfo('Sign up', 'Successfully signed up')

        
            
        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {e}")
            print(f"Error: {e}")
    else:
        messagebox.showerror('Invalid', "Passwords must match")
        print("Passwords do not match")
    halaman_signup(app)


img_path = os.path.join('23-Project-Team-CakeShop-PrakProkom','images', 'logo.png')

# Load and resize the image using Pillow
if not os.path.exists(img_path):
    messagebox.showerror("Error", "Image file not found")
else:
    img = Image.open(img_path)
    img = img.resize((360, 360), Image.LANCZOS)  # Resize the image to fit the window
    img = ImageTk.PhotoImage(img)
    label_img = Label(window, image=img, border=0, bg='#FFDED9')
    label_img.image = img  # Keep a reference to avoid garbage collection
    label_img.place(x=60, y=50) # To change position based on X & Y coordinates

frame = Frame(window, width=560, height=360, bg='#FFDED9')
frame.place(x=480, y=50)

heading = Label(frame, text="Sign Up", fg="#F16A6A", bg='#FFDED9', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e, widget, placeholder):
    if widget.get() == placeholder:
        widget.delete(0, 'end')
        if widget == code or widget == confirm_code:
            widget.config(show='*')

def on_leave(e, widget, placeholder):
    if widget.get() == '':
        widget.insert(0, placeholder)
        if widget == code or widget == confirm_code:
            widget.config(show='')

user = Entry(frame, width=25, fg='black', border=0, bg='#FFDED9', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
user.bind("<FocusOut>", lambda e: on_leave(e, user, 'Username'))

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg='#FFDED9', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
code.bind("<FocusOut>", lambda e: on_leave(e, code, 'Password'))

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

confirm_code = Entry(frame, width=25, fg='black', border=0, bg='#FFDED9', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", lambda e: on_enter(e, confirm_code, 'Confirm Password'))
confirm_code.bind("<FocusOut>", lambda e: on_leave(e, confirm_code, 'Confirm Password'))


Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign up', bg='#F16A6A', fg='#FFDED9', border=0, command=halaman_signup).place(x=35, y=280)
label = Label(frame, text='Already have an account?', fg='black', bg='#FFDED9', font=('Microsoft YaHei UI Light', 9))
label.place(x=70, y=340)

signin = Button(frame, width=6, text="Sign in", border=0, bg='#FFDED9', cursor='hand2', fg='#57a1f8', command=halaman_signup)
signin.place(x=215, y=341)

window.mainloop()


root=Tk()
root.title('SignIn')
root.geometry('925x500+300+200')
root.configure(bg="#FFDED9")
root.resizable(False,False)

def open_signup_window():
    root.destroy()
    os.system('python Register.py/signup')


def signin():
    username = user.get()
    password = code.get()
    path = os.getcwd() + '\\datasheet.csv'
    # Load the data from the datasheet.csv file
    try:
        
        with open(path, newline='') as file:
            reader = csv.reader(file)
            credentials = {rows[0]: rows[1] for rows in reader}
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read data file: {e}")
        return
    
    # Check if the entered username and password match the data
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

img_path = os.path.join( '23-Project-Team-CakeShop-PrakProkom','images', 'logo.png')

# Load and resize the image using Pillow
if not os.path.exists(img_path):
    messagebox.showerror("Error", "Image file not found")
else:
    img = Image.open(img_path)
    img = img.resize((360, 360), Image.LANCZOS)  # Resize the image to fit the window
    img = ImageTk.PhotoImage(img)
    label_img = Label(root, image=img, border=0, bg='#FFDED9')
    label_img.image = img  # Keep a reference to avoid garbage collection
    label_img.place(x=60, y=50) # To change position based on X & Y coordinates

frame=Frame(root,width=350,height=350,bg='#FFDED9')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg='#F16A6A',bg='#FFDED9',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

############----------------------------------------------------

# def on_enter(e, widget, placeholder):
#     user.delete(0,'end')


def on_enter(e, widget, placeholder):
    if widget.get() == placeholder:
        widget.delete(0, 'end')
        if widget == code:
            widget.config(show='*')

def on_leave(e, widget, placeholder):
    if widget.get() == '':
        widget.insert(0, placeholder)
        if widget == code:
            widget.config(show='')

# def on_leave(e):
#     name=user.get()
#     if name=='':
#         user.insert(0,'Username')

user=Entry(frame,width=36,fg='black',border=0,bg='#FFDED9',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)
user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
user.bind("<FocusOut>", lambda e: on_leave(e, user, 'Username'))

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

############----------------------------------------------------

# def on_enter(e):
#     code.delete(0,'end')

# def on_leave(e):
#     name=code.get()
#     if name=='':
#         code.insert(0,'Password') 

code=Entry(frame,width=36,fg='black',border=0,bg='#FFDED9',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
# code.bind('<FocusIn>', on_enter)
# code.bind('<FocusOut>', on_leave)
code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
code.bind("<FocusOut>", lambda e: on_leave(e, code, 'Password'))

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#################################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#F16A6A',fg='#FFDED9',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='#FFDED9',font=('Microsoft YaHei UI Light', 9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='#FFDED9',cursor='hand2',fg='#57a1f8', command=open_signup_window)
sign_up.place(x=215,y=270)

root.mainloop()