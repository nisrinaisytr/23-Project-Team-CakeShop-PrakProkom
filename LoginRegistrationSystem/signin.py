from tkinter import * 
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root=Tk()
root.title('SignIn')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

img_path = 'D:/KULIAH/SEMESTER 2/PROJECT PROKOM/TUBES/LoginRegistrationSystem/login.png'

# Load and resize the image using Pillow
if not os.path.exists(img_path):
    messagebox.showerror("Error", "Image file not found")
else:
    img = Image.open(img_path)
    img = img.resize((560, 360), Image.LANCZOS)  # Resize the image to fit the window
    img = ImageTk.PhotoImage(img)
    label_img = Label(root, image=img, border=0, bg='white')
    label_img.image = img  # Keep a reference to avoid garbage collection
    label_img.place(x=-10, y=50) # To change position based on X & Y coordinates

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg='#544e4a',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

############----------------------------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

############----------------------------------------------------

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password') 

code=Entry(frame,width=36,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#################################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)

root.mainloop()