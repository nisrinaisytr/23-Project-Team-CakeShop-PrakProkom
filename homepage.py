import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import importlib

# Fungsi untuk mengganti gambar di slider
def next_image():
    global image_index
    image_index = (image_index + 1) % len(slider_images)
    slider_label.configure(image=slider_images[image_index])

def prev_image():
    global image_index
    image_index = (image_index - 1) % len(slider_images)
    slider_label.configure(image=slider_images[image_index])

def logout():
    app.quit()

# Inisialisasi aplikasi
app = ctk.CTk()
app.geometry("900x600")
app.title("23Bee Bakery")

# Warna dan Font
bg_color = "#FFEFE8"
text_color = "#FF7A8A"
button_color = "#FFADA1"
menu_color = "#FFD9CC"
font_title = ("Arial", 30, "bold")
font_subtitle = ("Arial", 20, "bold")
font_text = ("Arial", 12)

# Konfigurasi grid
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Frame Utama
main_frame = ctk.CTkFrame(app, fg_color=bg_color)
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Folder gambar
image_folder = "images"

# Gambar Slider
image_files = ["bakery1.png", "bakery2.png", "bakery3.png"]
image_paths = [os.path.join(image_folder, img) for img in image_files]

# Print paths for debugging
print("Image paths for slider images:")
for path in image_paths:
    print(path)

slider_images = [ImageTk.PhotoImage(Image.open(img_path).resize((400, 300))) for img_path in image_paths]
image_index = 0

slider_label = ctk.CTkLabel(main_frame, image=slider_images[image_index], text="")
slider_label.grid(row=0, column=0, columnspan=3, pady=10)

# Tombol untuk slider
prev_button = ctk.CTkButton(main_frame, text="<", width=30, command=prev_image, fg_color=button_color)
next_button = ctk.CTkButton(main_frame, text=">", width=30, command=next_image, fg_color=button_color)

prev_button.place(x=100, y=100)
next_button.place(x=450, y=100)

# Judul dan Deskripsi
font_title = ("Arial", 30, "bold")
title_label = ctk.CTkLabel(main_frame, text="23Bee Bakery", font=font_title, text_color=text_color)
title_label.grid(row=1, column=0, columnspan=3, pady=10)

description_label = ctk.CTkLabel(main_frame, text="Welcome to 23Bee Bakery! Enjoy our fresh breads, scrumptious cakes, fluffy donuts, and delectable pastries. Crafted with the finest ingredients, every treat is a sweet adventure. Stop by for a delightful bite today!",
                                wraplength=600, justify="center", text_color=text_color, font=font_text)
description_label.grid(row=2, column=0, columnspan=3, pady=10)

# Deklarasi menu
menu_image_paths = ["images/breads.png", "images/cakes.png", "images/donuts.png", "images/pastry.png"]
menu_texts = ["BREADS", "CAKES", "DONUTS", "PASTRY"]

def open_breads():
    breads = importlib.import_module('breads')
    breads.main()

def open_cakes():
    cakes = importlib.import_module('cakes')
    cakes.main()

def open_donuts():
    donuts = importlib.import_module('donuts')
    donuts.main()

def open_pastry():
    pastry = importlib.import_module('pastry')
    pastry.main()

menu_commands = [open_breads, open_cakes, open_donuts, open_pastry]  # Daftar fungsi yang sesuai

# Seksi Menu
menu_label = ctk.CTkLabel(main_frame, text="OUR MENU", font=font_subtitle, text_color=text_color)
menu_label.grid(row=3, column=0, columnspan=4, pady=10)

menu_buttons = []

for i, (img_path, text, command) in enumerate(zip(menu_image_paths, menu_texts, menu_commands)):
    image = ImageTk.PhotoImage(Image.open(img_path).resize((150, 150)))
    btn = ctk.CTkButton(main_frame, image=image, text=text, compound="bottom", text_color=text_color, fg_color=button_color, command=command)
    btn.grid(row=4, column=i, padx=10, pady=10)
    menu_buttons.append(btn)

# Tombol Logout
logout_button = ctk.CTkButton(app, text="Log Out", fg_color=button_color, command=logout)
logout_button.place(x=700, y=20)

# Jalankan aplikasi
app.mainloop()

