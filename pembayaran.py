import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os
import invoice

# Global variables to store selected products and total cost
selected_products = []
selected_pilihan= ""
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
        product_label = ctk.CTkLabel(orders_frame, text=f"{product['name']} x {product.get('quantity', 1)}")
        product_label.grid(row=index, column=0, padx=10, pady=5)

        price_label = ctk.CTkLabel(orders_frame, text=f"Rp {product['price'] * product.get('quantity', 1)}")
        price_label.grid(row=index, column=1, padx=10, pady=5)

        remove_button = ctk.CTkButton(orders_frame, text="Remove", command=lambda i=index: remove_product(i), fg_color="#FFADA1")
        remove_button.grid(row=index, column=2, padx=10, pady=5)

    update_total_cost()

def go_back(app):
    for widget in app.winfo_children():
        widget.destroy()
        os.system('python homepage.py')

def buat_pembayaran_page(app, products, pilihan):
    global selected_products, selected_pilihan, total_cost_label
    selected_products = products
    selected_pilihan = pilihan
    
    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Header Frame
    header_frame = ctk.CTkFrame(app)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

    back_button = ctk.CTkButton(header_frame, text="Batal", command=lambda: go_back(app), fg_color="#FFADA1")
    back_button.grid(row=0, column=0, padx=10, pady=10)

    title_label = ctk.CTkLabel(header_frame, text="Total Pesanan Anda", justify="center", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=1, pady=15)

    # Orders Frame
    global orders_frame
    orders_frame = ctk.CTkFrame(app)
    orders_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

    display_orders()

    # Payment Frame
    payment_frame = ctk.CTkFrame(app)
    payment_frame.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

    payment_label = ctk.CTkLabel(payment_frame, text="PEMBAYARAN\nPilih Opsi Pembayaran", justify="center", font=("Arial", 18, "bold"))
    payment_label.grid(row=0, column=0, pady=10)

    payment_var = tk.StringVar(value="Tunai")

    tunai_radio = ctk.CTkRadioButton(payment_frame, text="Tunai", variable=payment_var, value="Tunai")
    tunai_radio.grid(row=1, column=0, padx=10, pady=5)

    non_tunai_radio = ctk.CTkRadioButton(payment_frame, text="Non Tunai", variable=payment_var, value="Non Tunai")
    non_tunai_radio.grid(row=2, column=0, padx=10, pady=5)


    def checkout():
        nama_pengguna = "Nama Pengguna"  # Ambil nama dari input pengguna
        jam_input = "10:00 AM"  # Ambil jam dari input pengguna
        metode_pembayaran = payment_var.get()
        invoice.buat_invoice_page(app, nama_pengguna, pilihan, jam_input, metode_pembayaran)

    # Total and Checkout
    total_cost_label = ctk.CTkLabel(app, text="RP 0,-", font=("Arial", 16, "bold"))
    total_cost_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")

    checkout_button = ctk.CTkButton(app, text="Check Out", command=checkout, fg_color="#FFADA1")
    checkout_button.grid(row=2, column=1, pady=10, padx=10, sticky="e")

    # Update the total cost initially
    update_total_cost()

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Cakeshop - Pembayaran")
    app.geometry("900x500")
    sample_products = [
        {'name': 'Choco Bun', 'quantity': 1, 'price': 11000},
        {'name': 'Korean Garlic Bread', 'quantity': 1, 'price': 20000},
    ]
    buat_pembayaran_page(app, sample_products, "dine_in")
    app.mainloop()
