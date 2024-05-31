import customtkinter as ctk
from PIL import Image, ImageTk
import os
import subprocess

def main(app):
    global slider_label, image_index, slider_images

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

    def delete_cart():
        try:
            os.remove('database/cart.csv')
        except FileNotFoundError:
            pass
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", delete_cart)

    bg_color = "#FFEFE8"
    text_color = "#FF7A8A"
    button_color = "#FFADA1"
    menu_color = "#FFD9CC"
    font_title = ("Baskerville Old Face", 90, "bold")
    font_subtitle = ("Baskerville", 20, "bold")
    font_text = ("Baskerville", 13, "bold")
    ourmenu=("Baskerville Old Face", 40, "bold")

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    main_frame = ctk.CTkFrame(app, fg_color=bg_color)
    main_frame.grid(row=0, column=0, rowspan=6, columnspan=5, sticky="nsew", padx=35, pady=25)

    img_pathbread = os.path.join('images', 'homepage.png')
    imgbread = Image.open(img_pathbread)
    imgbread = imgbread.resize((2050, 1095), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(imgbread)

    bg_label = ctk.CTkLabel(app, image=img1)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = img1
    bg_label.lower()

    image_folder = "images"
    image_files = ["logohome.png","bakery1.png", "bakery2.png", "bakery3.png", "bakery4.png", "bakery5.png"]
    image_paths = [os.path.join(image_folder, img) for img in image_files]

    slider_images = [ImageTk.PhotoImage(Image.open(img_path).resize((600, 400))) for img_path in image_paths]
    image_index = 0

    slider_label = ctk.CTkLabel(main_frame, image=slider_images[image_index], text="")
    slider_label.place(relx=0.09, rely=0.07)

    prev_button = ctk.CTkButton(main_frame, text="<", width=30, command=prev_image, fg_color=button_color)
    next_button = ctk.CTkButton(main_frame, text=">", width=30, command=next_image, fg_color=button_color)

    prev_button.place(relx=0.073, rely=0.265, anchor='center')
    next_button.place(relx=0.441, rely=0.265, anchor='center')

    title_label = ctk.CTkLabel(main_frame, text="23Bee Bakery", justify="right", font=font_title, text_color=text_color)
    title_label.place(relx=0.499, rely=0.1)

    description_label = ctk.CTkLabel(main_frame, text="Welcome to 23Bee Bakery! Enjoy our fresh breads, scrumptious cakes, fluffy donuts, and delectable pastries. Crafted with the finest ingredients, every treat is a sweet adventure. Stop by for a delightful bite today!",
                                    wraplength=600, justify="right", text_color=text_color, font=font_subtitle)
    description_label.place(relx=0.492, rely=0.275)

    menu_image_paths = ["images/breads.png", "images/cakes.png", "images/donuts.png", "images/pastry.png"]
    menu_texts = ["BREADS", "CAKES", "DONUTS", "PASTRY"]

    menu_images = [ImageTk.PhotoImage(Image.open(img_path).resize((250, 250))) for img_path in menu_image_paths]

    import button
    menu_commands = [
        lambda: button.menuju_ke_breads(app),
        lambda: button.menuju_ke_cakes(app),
        lambda: button.menuju_ke_donuts(app),
        lambda: button.menuju_ke_pastry(app)
    ]

    menu_label = ctk.CTkLabel(main_frame, text="                                       OUR MENU                                     ", font=ourmenu, text_color='white', fg_color=button_color)
    menu_label.place(relx=0.5, rely=0.54, anchor='center')

    menu_frame = ctk.CTkFrame(main_frame, fg_color=bg_color)
    menu_frame.place(relx=0.5, rely=0.78, anchor='center')

    for i, (img, text, command) in enumerate(zip(menu_images, menu_texts, menu_commands)):
        frame = ctk.CTkFrame(menu_frame,fg_color=bg_color )
        frame.grid(row=0, column=i, padx=60, pady=25)
        
        img_label = ctk.CTkLabel(frame, image=img, text="")
        img_label.pack(pady=(0, 10))

        btn = ctk.CTkButton(frame, text=text, font=font_text,text_color='white', fg_color=button_color, command=command)
        btn.pack(padx=(1,1))

    logout_button = ctk.CTkButton(app, text="Log Out", fg_color=button_color, command=logout)
    logout_button.place(relx=0.95, rely=0.05, anchor='ne')

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("1270x710")
    app.title("23Bee Bakery")
    main(app)
    app.mainloop()
