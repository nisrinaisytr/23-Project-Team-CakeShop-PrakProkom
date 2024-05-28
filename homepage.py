import customtkinter as ctk
from PIL import Image, ImageTk
import os
import subprocess

def main():
    global app, slider_label, image_index, slider_images

    image_index = 0

    def next_image():
        global image_index
        image_index = (image_index + 1) % len(slider_images)
        slider_label.configure(image=slider_images[image_index])

    def prev_image():
        global image_index
        image_index = (image_index - 1) % len(slider_images)
        slider_label.configure(image=slider_images[image_index])

    def logout():
        app.destroy()
        subprocess.Popen(['python', 'register.py', 'signin'])

    app = ctk.CTk()
    app.geometry("900x600")
    app.title("23Bee Bakery")

    bg_color = "#FFEFE8"
    text_color = "#FF7A8A"
    button_color = "#FFADA1"
    menu_color = "#FFD9CC"
    font_title = ("Arial", 30, "bold")
    font_subtitle = ("Arial", 20, "bold")
    font_text = ("Arial", 12)

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    main_frame = ctk.CTkFrame(app, fg_color=bg_color)
    main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    image_folder = "images"
    image_files = ["bakery1.png", "bakery2.png", "bakery3.png"]
    image_paths = [os.path.join(image_folder, img) for img in image_files]

    slider_images = [ImageTk.PhotoImage(Image.open(img_path).resize((400, 300))) for img_path in image_paths]
    image_index = 0

    slider_label = ctk.CTkLabel(main_frame, image=slider_images[image_index], text="")
    slider_label.grid(row=0, column=0, columnspan=3, pady=10)

    prev_button = ctk.CTkButton(main_frame, text="<", width=30, command=prev_image, fg_color=button_color)
    next_button = ctk.CTkButton(main_frame, text=">", width=30, command=next_image, fg_color=button_color)

    prev_button.place(x=100, y=100)
    next_button.place(x=450, y=100)

    title_label = ctk.CTkLabel(main_frame, text="23Bee Bakery", font=font_title, text_color=text_color)
    title_label.grid(row=1, column=0, columnspan=3, pady=10)

    description_label = ctk.CTkLabel(main_frame, text="Welcome to 23Bee Bakery! Enjoy our fresh breads, scrumptious cakes, fluffy donuts, and delectable pastries. Crafted with the finest ingredients, every treat is a sweet adventure. Stop by for a delightful bite today!",
                                    wraplength=600, justify="center", text_color=text_color, font=font_text)
    description_label.grid(row=2, column=0, columnspan=3, pady=10)

    menu_image_paths = ["images/breads.png", "images/cakes.png", "images/donuts.png", "images/pastry.png"]
    menu_texts = ["BREADS", "CAKES", "DONUTS", "PASTRY"]

    menu_images = [ImageTk.PhotoImage(Image.open(img_path).resize((150, 150))) for img_path in menu_image_paths]

    import button
    menu_commands = [
        lambda: button.menuju_ke_breads(app),
        lambda: button.menuju_ke_cakes(app),
        lambda: button.menuju_ke_donuts(app),
        lambda: button.menuju_ke_pastry(app)
    ]

    menu_label = ctk.CTkLabel(main_frame, text="OUR MENU", font=font_subtitle, text_color=text_color)
    menu_label.grid(row=3, column=0, columnspan=4, pady=10)

    for i, (img, text, command) in enumerate(zip(menu_images, menu_texts, menu_commands)):
        frame = ctk.CTkFrame(main_frame)
        frame.grid(row=4, column=i, padx=10, pady=10)
        
        img_label = ctk.CTkLabel(frame, image=img, text="")
        img_label.pack(pady=(0, 10))

        btn = ctk.CTkButton(frame, text=text, text_color=text_color, fg_color=button_color, command=command)
        btn.pack()

    logout_button = ctk.CTkButton(app, text="Log Out", fg_color=button_color, command=logout)
    logout_button.place(x=700, y=20)

    app.mainloop()

if __name__ == "__main__":
    main()
