import tkinter as tk
from tkinter import font

def check_fonts():
    root = tk.Tk()
    fonts = list(font.families())
    print("Available fonts:")
    for f in sorted(fonts):
        print(f)
    root.destroy()

check_fonts()

# Example of using these fonts in a Tkinter application
root = tk.Tk()
root.title("Tkinter Fonts Example")

label1 = tk.Label(root, text="Comic Sans MS", font=("Comic Sans MS", 20))
label1.pack(pady=10)

label2 = tk.Label(root, text="Papyrus", font=("Papyrus", 20))
label2.pack(pady=10)

label3 = tk.Label(root, text="Curlz MT", font=("Curlz MT", 20))
label3.pack(pady=10)

label4 = tk.Label(root, text="Jokerman", font=("Jokerman", 20))
label4.pack(pady=10)

label5 = tk.Label(root, text="Bradley Hand ITC", font=("Bradley Hand ITC", 20))
label5.pack(pady=10)

label6 = tk.Label(root, text="Kristen ITC", font=("Kristen ITC", 20))
label6.pack(pady=10)

label7 = tk.Label(root, text="Segoe Print", font=("Segoe Print", 20))
label7.pack(pady=10)

label8 = tk.Label(root, text="Segoe Script", font=("Segoe Script", 20))
label8.pack(pady=10)

label9 = tk.Label(root, text="Verdana", font=("Verdana", 20))
label9.pack(pady=10)



root.mainloop()
