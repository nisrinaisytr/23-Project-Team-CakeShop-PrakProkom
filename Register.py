from tkinter import *
from tkinter import messagebox
import os
import csv
import subprocess
from PIL import Image, ImageTk

database_path = os.path.join(os.getcwd(), 'database', 'akun.csv')

def open_signup_window():
    root.destroy()
    main('signup')

def open_signin_window():
    root.destroy()
    main('signin')

def open_homepage():
    root.destroy()  # Menutup jendela login
    subprocess.Popen(['python', 'homepage.py'])  # Membuka homepage

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file_exists = os.path.exists(database_path)

            with open(database_path, 'a+', newline='') as file:
                writer = csv.writer(file)
                
                if not file_exists:
                    writer.writerow(['Username', 'Password'])

                file.seek(0)
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if row and row[0] == username:
                        messagebox.showerror('Error', 'Username already exists')
                        return

            with open(database_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password])

            messagebox.showinfo('Sign up', 'Successfully signed up')
            open_signin_window()
        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {e}")
    else:
        messagebox.showerror('Invalid', "Passwords must match")

def signin():
    username = user.get()
    password = code.get()
    
    try:
        with open(database_path, newline='') as file:
            reader = csv.reader(file)
            credentials = {rows[0]: rows[1] for rows in reader}
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read data file: {e}")
        return
    
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        open_homepage()  # Buka homepage setelah login berhasil
    else:
        messagebox.showerror("Error", "Invalid username or password")

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

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

def main(action):
    global root, user, code, confirm_code
    root = Tk()
    root.title('SignIn' if action == 'signin' else 'Sign Up')
    root.geometry('1270x710')
    root.configure(bg="#FFDED9")
    root.resizable(True, True)  # Pastikan jendela bisa di-resize

    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", end_fullscreen)

    img_path = os.path.join('images', 'logo.png')
    if not os.path.exists(img_path):
        messagebox.showerror("Error", "Image file not found")
    else:
        img = Image.open(img_path)
        img = img.resize((360, 360), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        label_img = Label(root, image=img, border=0, bg='#FFDED9')
        label_img.image = img
        label_img.place(x=60, y=50)

    frame = Frame(root, width=560, height=360, bg='#FFDED9') if action == 'signup' else Frame(root, width=350, height=350, bg='#FFDED9')
    frame.place(x=480, y=50 if action == 'signup' else 70)

    heading = Label(frame, text='Sign Up' if action == 'signup' else 'Sign in', fg='#F16A6A', bg='#FFDED9', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100 if action == 'signup' else 100, y=5)

    user = Entry(frame, width=25 if action == 'signup' else 36, fg='black', border=0, bg='#FFDED9', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
    user.bind("<FocusOut>", lambda e: on_leave(e, user, 'Username'))
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25 if action == 'signup' else 36, fg='black', border=0, bg='#FFDED9', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
    code.bind("<FocusOut>", lambda e: on_leave(e, code, 'Password'))
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    if action == 'signup':
        confirm_code = Entry(frame, width=25, fg='black', border=0, bg='#FFDED9', font=('Microsoft YaHei UI Light', 11))
        confirm_code.place(x=30, y=220)
        confirm_code.insert(0, 'Confirm Password')
        confirm_code.bind("<FocusIn>", lambda e: on_enter(e, confirm_code, 'Confirm Password'))
        confirm_code.bind("<FocusOut>", lambda e: on_leave(e, confirm_code, 'Confirm Password'))
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        Button(frame, width=39, pady=7, text='Sign up', bg='#F16A6A', fg='#FFDED9', border=0, command=signup).place(x=35, y=280)
        label = Label(frame, text='Already have an account?', fg='black', bg='#FFDED9', font=('Microsoft YaHei UI Light', 9))
        label.place(x=70, y=340)
        signin_tombol = Button(frame, width=6, text="Sign in", border=0, bg='#FFDED9', cursor='hand2', fg='#57a1f8', command=open_signin_window)
        signin_tombol.place(x=215, y=341)
    else:
        Button(frame, width=39, pady=7, text='Sign in', bg='#F16A6A', fg='#FFDED9', border=0, command=signin).place(x=35, y=204)
        label = Label(frame, text="Don't have an account?", fg='black', bg='#FFDED9', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)
        sign_up = Button(frame, width=6, text='Sign up', border=0, bg='#FFDED9', cursor='hand2', fg='#57a1f8', command=open_signup_window)
        sign_up.place(x=215, y=270)

    root.mainloop()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'signin':
        main('signin')
    else:
        main('signup')  # Default behavior, jika tidak ada argumen maka membuka halaman sign-up
