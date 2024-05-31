import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import pembayaran
import csv
import os

font_title = ("Baskerville Old Face", 90, "bold")
font_subtitle = ("Baskerville", 20, "bold")
font_text = ("Baskerville", 13, "bold")
ourmenu=("Baskerville Old Face", 40, "bold")
button_color = "#FFADA1"

def simpan_data_pembeli(nama, no_telp, alamat, jam, pilihan):
    folder_path = 'database'
    file_path = os.path.join(folder_path, 'datapembeli.csv')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, no_telp, alamat, jam, pilihan])

def buat_pemilihan_page(app, pilihan, selected_products):
    pemilihan_window = ctk.CTkToplevel(app)
    pemilihan_window.title("Pemilihan")
    pemilihan_window.geometry("900x610")  # Sesuaikan ukuran jendela
    
    # Bring the pemilihan_window to the front
    pemilihan_window.attributes("-topmost", True)
    pemilihan_window.focus_force()
    
    # Load and set background image
    img_pathbread = os.path.join('images', 'homepage.png')
    imgbread = Image.open(img_pathbread)
    imgbread = imgbread.resize((2050, 1095), Image.LANCZOS)  # Adjust to fit the window size
    img1 = ImageTk.PhotoImage(imgbread)

    bg_label = ctk.CTkLabel(pemilihan_window, image=img1)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = img1  # Prevent image from being garbage collected
    bg_label.lower()

    def go_back():
        pemilihan_window.destroy()

    def confirm_selection():
        nama = name_entry.get()
        no_telp = phone_entry.get()
        alamat = address_entry.get() if pilihan == "DELIVERY" else ""
        jam = time_entry.get()
        print(f"Nama: {nama}, No Telp: {no_telp}, Alamat: {alamat}, Jam: {jam}, Opsi: {pilihan}")
        
        # Simpan data pembeli ke dalam file CSV
        simpan_data_pembeli(nama, no_telp, alamat, jam, pilihan)
        
        # Pastikan setiap produk memiliki kunci 'quantity'
        for product in selected_products:
            if 'quantity' not in product:
                product['quantity'] = 1  # Atur nilai default jika tidak ada 'quantity'

        # Tutup jendela pemilihan dan buka halaman pembayaran
        pemilihan_window.destroy()
        pembayaran.buat_pembayaran_page(app, selected_products, pilihan)

    pemilihan_window.configure(bg="#FFEFE8")
    
    # Header frame
    header_frame = ctk.CTkFrame(pemilihan_window, fg_color="#FFF", width=750, height=50)
    header_frame.place(relx=0.5, rely=0.1, anchor="center")
    header_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    back_button = ctk.CTkButton(header_frame, text="Back", command=go_back, fg_color="#FFADA1")
    back_button.pack(side="left", padx=10, pady=10)

    title_label = ctk.CTkLabel(header_frame, text=(f"{pilihan.upper()}"), justify="center",text_color='#DB7575', font=("Baskerville Old Face", 30, "bold"))
    title_label.pack(side="left", pady=10, padx=170)
    
    # Form frame
    form_frame = ctk.CTkFrame(pemilihan_window, fg_color="#FFF", width=750, height=500)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")
    form_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    ctk.CTkLabel(form_frame, text="Informasi Pembeli",text_color='#DB7575', font=("Baskerville Old Face", 40, "bold")).grid(row=0, column=0, columnspan=2, pady=(40, 40), padx=(90,90))
    ctk.CTkLabel(form_frame, text="NAMA :",text_color='#DB7575', font=("Baskerville", 25, "bold")).grid(row=1, column=0, pady=(0, 20),padx=(0,20), sticky="e")
    ctk.CTkLabel(form_frame, text="NO TELP :",text_color='#DB7575', font=("Baskerville", 25, "bold")).grid(row=2, column=0, pady=(0, 20),padx=(0,20), sticky="e")
    
    time_label_text = "JAM KEDATANGAN :" if pilihan == "DINE IN" else "JAM PENGANTARAN :" if pilihan == "DELIVERY" else "JAM PENGAMBILAN :"
    ctk.CTkLabel(form_frame, text=time_label_text,text_color='#DB7575', font=("Baskerville", 25, "bold")).grid(row=3, column=0, pady=(0, 40),padx=(90,20), sticky="e")

    if pilihan == "DELIVERY":
        ctk.CTkLabel(form_frame, text="ALAMAT :",text_color='#DB7575', font=("Baskerville", 24, "bold")).grid(row=4, column=0, pady=(0, 40), sticky="e")
        address_entry = ctk.CTkEntry(form_frame,fg_color='#EDDCD8')
        address_entry.grid(row=4, column=1, pady=(0, 40), padx=(0, 30))
    else: 
        address_entry = None
    
    name_entry = ctk.CTkEntry(form_frame,fg_color='#EDDCD8')
    phone_entry = ctk.CTkEntry(form_frame,fg_color='#EDDCD8')
    time_entry = ctk.CTkEntry(form_frame,fg_color='#EDDCD8')
    
    name_entry.grid(row=1, column=1, pady=(0, 20), padx=(0, 40))
    phone_entry.grid(row=2, column=1, pady=(0, 20), padx=(0, 40))
    time_entry.grid(row=3, column=1, pady=(0, 40), padx=(0, 40))
    
    confirm_button = ctk.CTkButton(pemilihan_window, text="CONFIRM",font=("Baskerville", 25, "bold"), command=confirm_selection, fg_color="#FFF",text_color='#DB7575')
    confirm_button.place(relx=0.5, rely=0.88, anchor="center")  # Center confirm button at bottom

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Pemilihan")
    sample_products = [
        {'name': 'Choco Bun', 'quantity': 1, 'price': 11000},
        {'name': 'Korean Garlic Bread', 'quantity': 1, 'price': 20000},
    ]
    buat_pemilihan_page(app, "DINE IN", sample_products)
    app.mainloop()
