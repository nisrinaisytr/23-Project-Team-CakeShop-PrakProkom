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
window.configure(bg='#fff')
window.resizable(False, False)

def open_signin_window():
    window.destroy()
    os.system('python LoginRegistrationSystem/SignIn.py')

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            # Check if CSV file exists
            file_exists = os.path.exists('datasheet.csv')
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

            # Open the sign-in window
            open_signin_window()
            
        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {e}")
            print(f"Error: {e}")
    else:
        messagebox.showerror('Invalid', "Passwords must match")
        print("Passwords do not match")



img_path = os.path.join('LoginRegistrationSystem', 'images', 'login.png')

# Load and resize the image using Pillow
if not os.path.exists(img_path):
    messagebox.showerror("Error", "Image file not found")
else:
    img = Image.open(img_path)
    img = img.resize((560, 360), Image.LANCZOS)  # Resize the image to fit the window
    img = ImageTk.PhotoImage(img)
    label_img = Label(window, image=img, border=0, bg='white')
    label_img.image = img  # Keep a reference to avoid garbage collection
    label_img.place(x=-10, y=50) # To change position based on X & Y coordinates

frame = Frame(window, width=560, height=360, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text="Sign Up", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
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

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
user.bind("<FocusOut>", lambda e: on_leave(e, user, 'Username'))

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
code.bind("<FocusOut>", lambda e: on_leave(e, code, 'Password'))

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", lambda e: on_enter(e, confirm_code, 'Confirm Password'))
confirm_code.bind("<FocusOut>", lambda e: on_leave(e, confirm_code, 'Confirm Password'))


Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text='Already have an account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=70, y=340)

signin = Button(frame, width=6, text="Sign in", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=open_signin_window)
signin.place(x=215, y=341)

window.mainloop()