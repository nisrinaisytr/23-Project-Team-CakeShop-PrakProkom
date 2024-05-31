import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import invoice
import csv

# Global variables to store selected products and total cost
selected_products = []
selected_pilihan = ""
total_cost = 0
total_cost_label = None  # Define total_cost_label globally

def update_total_cost():
    global total_cost, total_cost_label
    total_cost = sum(product['price'] * product['quantity'] for product in selected_products)
    if total_cost_label:
        total_cost_label.configure(text=f"RP {total_cost},-")

def remove_product(index):
    global selected_products
    del selected_products[index]
    display_orders()

def display_orders():
    for widget in orders_frame.winfo_children():
        widget.destroy()

    for index, product in enumerate(selected_products):
        product_label = ctk.CTkLabel(orders_frame,text_color='#C27767', text=f"{product['name']} x {product.get('quantity', 1)}")
        product_label.grid(row=index, column=0, padx=10, pady=5)

        price_label = ctk.CTkLabel(orders_frame,text_color='#C27767', text=f"Rp {product['price'] * product.get('quantity', 1)}")
        price_label.grid(row=index, column=1, padx=10, pady=5)

        remove_button = ctk.CTkButton(orders_frame,text_color='white', text="Remove", command=lambda i=index: remove_product(i), fg_color="#C27767")
        remove_button.grid(row=index, column=2, padx=10, pady=5)

    update_total_cost()

def go_back(app):
    for widget in app.winfo_children():
        widget.destroy()
        os.system('python homepage.py')

# This function reads the latest data from the CSV file
def get_latest_data_from_csv(file_path):
    latest_data = None
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            latest_data = row
    return latest_data

def save_order(nama_pengguna, nomor_telepon, pilihan, jam, produk):
    pass  # This function is no longer needed since we're not saving to an HTML file

def buat_pembayaran_page(app, products, pilihan):
    global selected_products, selected_pilihan, total_cost_label
    selected_products = products
    selected_pilihan = pilihan

    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()
    img_pathbread = os.path.join('images', 'background.png')
    imgbread = Image.open(img_pathbread)
    imgbread = imgbread.resize((2050, 1095), Image.LANCZOS)  # Adjust to fit the window size
    img1 = ImageTk.PhotoImage(imgbread)

    bg_label = ctk.CTkLabel(app, image=img1, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = img1  # Prevent image from being garbage collected
    bg_label.lower()

    main_frame = ctk.CTkFrame(app,fg_color='white', width=900, height=600)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")
    main_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    # Header Frame
    header_frame = ctk.CTkFrame(main_frame, fg_color="#FFF", width=600, height=50)
    header_frame.place(relx=0.58, rely=0.1, anchor="center")
    header_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    from button import balik_ke_home
    back_button = ctk.CTkButton(app, text="Batal", command=lambda:balik_ke_home(app), fg_color="#FFADA1")
    back_button.pack(side="top", padx=15, pady=30)
    back_button.place(rely=0.02,relx=0.01)
    #back_button.pack_propagate(False) 

    title_label = ctk.CTkLabel(header_frame, text="TOTAL PESANAN ANDA", justify="center",text_color='#DB7575', font=("Baskerville Old Face", 35, "bold"))
    title_label.pack(side="left", pady=10, padx=40)

    # Orders Frame
    global orders_frame
    orders_frame = ctk.CTkFrame(main_frame, fg_color="#ffe3de", width=900, height=500)
    orders_frame.place(relx=0.12, rely=0.18)
    orders_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    display_orders()

    # Payment Frame
    payment_frame = ctk.CTkFrame(main_frame, fg_color="#ffe3de", width=750, height=500)
    payment_frame.place(relx=0.63, rely=0.18)
    payment_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    payment_label = ctk.CTkLabel(payment_frame, text="PEMBAYARAN\nPilih Opsi Pembayaran",text_color='#DB7575', justify="center", font=("Arial", 18, "bold"))
    payment_label.grid(row=0, column=0, padx=20,pady=20)

    payment_var = tk.StringVar(value="Tunai")

    tunai_radio = ctk.CTkRadioButton(payment_frame, text="Tunai",hover_color='#DB7575',fg_color='#DB7575',text_color= '#DB7575', variable=payment_var, value="Tunai")
    tunai_radio.grid(row=1, column=0, padx=10, pady=(15,20))

    non_tunai_radio = ctk.CTkRadioButton(payment_frame,hover_color='#DB7575',fg_color='#DB7575', text="Non Tunai",text_color= '#DB7575',variable=payment_var, value="Non Tunai")
    non_tunai_radio.grid(row=2, column=0, padx=10, pady=(10,50))
    

    def checkout():
        # Read the latest data from datapembeli.csv
        latest_data = get_latest_data_from_csv("database/datapembeli.csv")
        if latest_data:
            nama_pengguna = latest_data[0].capitalize()  # Take name from CSV file and capitalize
            no_telp = latest_data[1]
            jam_input = latest_data[3].strip()  # Take time from CSV file
        else:
            # Default if no data in CSV
            nama_pengguna = "Unknown User"
            no_telp = "0000000000"
            jam_input = "10:00 AM"
        
        metode_pembayaran = payment_var.get()

        # Prepare items for invoice
        items = [(product['name'], product['price'] * product['quantity']) for product in selected_products]
        total_harga = sum(item[1] for item in items)

        invoice.buat_invoice_page(app, nama_pengguna, no_telp, selected_pilihan.upper(), jam_input, metode_pembayaran, items, total_harga)

    # Total and Checkout
    total_cost_label = ctk.CTkLabel(main_frame, text=(f"Total Pesanan Rp {total_cost}"),text_color='#DB7575', font=("Arial", 16, "bold"))
    total_cost_label.place(relx=0.14, rely=0.87 , anchor="nw")

    checkout_button = ctk.CTkButton(main_frame, text="checkout",font=("Baskerville", 25, "bold"), command=checkout, fg_color="#ffe3de",text_color='#DB7575')
    checkout_button.place(relx=0.87, rely=0.91, anchor="center")  # Center confirm button at bottom

    # Update the total cost initially
    update_total_cost()

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Cakeshop - Pembayaran")
    app.geometry("1270x710")
    sample_products = [
        {'name': 'Choco Bun', 'quantity': 1, 'price': 11000},
        {'name': 'Korean Garlic Bread', 'quantity': 1, 'price': 20000},
    ]
    buat_pembayaran_page(app, sample_products, "DINE IN")
    app.mainloop()
