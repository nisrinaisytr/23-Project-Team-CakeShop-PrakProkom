import customtkinter as ctk
import tkinter as tk
import pembayaran
import csv
import os

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
    pemilihan_window.geometry("900x500")  # Sesuaikan ukuran jendela
    
    # Bring the pemilihan_window to the front
    pemilihan_window.attributes("-topmost", True)
    pemilihan_window.focus_force()

    def go_back():
        pemilihan_window.destroy()

    def confirm_selection():
        nama = name_entry.get()
        no_telp = phone_entry.get()
        alamat = address_entry.get() if pilihan == "Delivery" else ""
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
    
    header_frame = ctk.CTkFrame(pemilihan_window, fg_color="#FFD9CC")
    header_frame.grid(row=0, column=0, sticky="ew")

    back_button = ctk.CTkButton(header_frame, text="Back", command=go_back, fg_color="#FFADA1")
    back_button.grid(row=0, column=0, padx=10, pady=10)

    title_label = ctk.CTkLabel(header_frame, text=pilihan.upper(), justify="center", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=1, pady=15)
    
    form_frame = ctk.CTkFrame(pemilihan_window, fg_color="#FFD9CC")
    form_frame.grid(row=1, column=0, pady=50, padx=50)

    ctk.CTkLabel(form_frame, text="Informasi Pembeli", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
    ctk.CTkLabel(form_frame, text="NAMA :", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
    ctk.CTkLabel(form_frame, text="NO TELP :", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="e")
    
    time_label_text = "JAM KEDATANGAN :" if pilihan == "Dine In" else "JAM PENGANTARAN :" if pilihan == "Delivery" else "JAM PENGAMBILAN :"
    ctk.CTkLabel(form_frame, text=time_label_text, font=("Arial", 12)).grid(row=3, column=0, pady=5, sticky="e")

    address_label_text = "ALAMAT :" 
    if pilihan == "Delivery":
        ctk.CTkLabel(form_frame, text=address_label_text, font=("Arial", 12)).grid(row=4, column=0, pady=5, sticky="e")
        address_entry = ctk.CTkEntry(form_frame)
        address_entry.grid(row=4, column=1, pady=5, padx=10)
    else: 
        address_entry = None
    

    name_entry = ctk.CTkEntry(form_frame)
    phone_entry = ctk.CTkEntry(form_frame)
    time_entry = ctk.CTkEntry(form_frame)
    
    name_entry.grid(row=1, column=1, pady=5, padx=10)
    phone_entry.grid(row=2, column=1, pady=5, padx=10)
    time_entry.grid(row=3, column=1, pady=5, padx=10)
    
    confirm_button = ctk.CTkButton(pemilihan_window, text="CONFIRM", command=confirm_selection, fg_color="#FFADA1")
    confirm_button.grid(row=2, column=0, pady=20)

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Pemilihan")
    app.geometry("900x500")
    sample_products = [
        {'name': 'Choco Bun', 'quantity': 1, 'price': 11000},
        {'name': 'Korean Garlic Bread', 'quantity': 1, 'price': 20000},
    ]
    buat_pemilihan_page(app, "Dine In", sample_products)
    app.mainloop()
