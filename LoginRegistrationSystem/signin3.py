from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.geometry('990x660+50+50')
root.resizable(0, 0)
root.title('Login Page')

image_path = 'login.jpg'

try:
    loginImage = ImageTk.PhotoImage(Image.open(image_path))
except Exception as e:
    messagebox.showerror("Error", f"Unable to load image: {e}")
    root.destroy()  # Close the application if the image can't be loaded
else:
    bgLabel = Label(root, image=loginImage)
    bgLabel.place(x=0, y=0)

    heading = Label(root, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
                    bg='white', fg='#ffe4e1')
    heading.place(x=605, y=120)

root.mainloop()
