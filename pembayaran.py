import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os
import invoice
import csv

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


# Ini pake data paling bawah dari db datapembeli.csv buat nentuin nama, alamat, etc
def get_latest_data_from_csv(file_path):
    latest_data = None
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            latest_data = row
    return latest_data

# def save_order(nama_pengguna, nomor_telepon, pilihan, jam, produk):
#     folder_path = 'database'
#     file_path = os.path.join(folder_path, 'data_pesanan.txt')

#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     # Gabungkan item yang sama
#     product_dict = {}
#     for item in produk:
#         name = item['name']
#         if name in product_dict:
#             product_dict[name]['quantity'] += item.get('quantity', 1)
#             product_dict[name]['price'] += item['price'] * item.get('quantity', 1)
#         else:
#             product_dict[name] = {
#                 'quantity': item.get('quantity', 1),
#                 'price': item['price'] * item.get('quantity', 1)
#             }

#     # Hitung total harga
#     total_harga = sum(item['price'] for item in product_dict.values())

#     # Tulis ke file
#     with open(file_path, mode='a') as file:
#         file.write(f"Nama Pengguna: {nama_pengguna}\n")
#         file.write(f"Nomor Telepon: {nomor_telepon}\n")
#         file.write(f"Pilihan: {pilihan}\n")
#         file.write(f"Jam: {jam}\n")
#         file.write("Daftar Pembelian:\n")
#         for name, details in product_dict.items():
#             # Gunakan format string dengan lebar tetap
#             file.write(f"    {name:<30} {details['quantity']:<10} {details['price']:<10}\n")
#         file.write(f"\nTotal Harga: {total_harga}\n")
#         file.write("\n")

import os

def save_order(nama_pengguna, nomor_telepon, pilihan, jam, produk):
    folder_path = 'database'
    file_path = os.path.join(folder_path, 'customer_receipt.html')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    nama_pengguna = nama_pengguna
    nomor_telepon = nomor_telepon
    pilihan = pilihan
    jam = jam

    # Gabungkan item yang sama
    product_dict = {}
    for item in produk:
        name = item['name']
        if name in product_dict:
            product_dict[name]['quantity'] += item.get('quantity', 1)
            product_dict[name]['price'] += item['price'] * item.get('quantity', 1)
        else:
            product_dict[name] = {
                'quantity': item.get('quantity', 1),
                'price': item['price'] * item.get('quantity', 1)
            }

    # Hitung total harga
    total_harga = sum(item['price'] for item in product_dict.values())

    # Tulis ke file HTML
    with open(file_path, mode='w') as file:
        file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Invoice</title>
<style>
        
        #invoice-POS{
  box-shadow: 0 0 1in -0.25in rgba(0, 0, 0, 0.5);
  padding:2mm;
  margin: 0 auto;
  width: 55mm;
  background: #FFF;
  
  
h1{
  font-size: 1.5em;
  color: #222;
}
h2{font-size: .9em;}
h3{
  font-size: 1.2em;
  font-weight: 300;
  line-height: 2em;
}
p{
  font-size: .7em;
  color: #666;
  line-height: 1.2em;
}
 
#top, #mid,#bot{ /* Targets all id with 'col-' */
  border-bottom: 1px solid #EEE;
}

#top{min-height: 100px;}
#mid{min-height: 80px;} 
#bot{ min-height: 50px;}

.clientlogo{
  float: left;
	height: 60px;
	width: 60px;
	background: url(http://michaeltruong.ca/images/client.jpg) no-repeat;
	background-size: 60px 60px;
  border-radius: 50px;
}
.info{
  display: block;
  float:left;
  margin-left: 0;
}
.title{
  float: right;
}
.title p{text-align: right;} 
table{
  width: 100%;
  border-collapse: collapse;
}
td{
  padding: 5px 0 5px 15px;
  border: 1px solid #EEE
}
.tabletitle{
  padding: 5px;
  font-size: .5em;
  background: #EEE;
}
.service{border-bottom: 1px solid #EEE;}
.item{width: 24mm;}
.itemtext{font-size: .5em;}

#legalcopy{
  margin-top: 5mm;
}

  
  
}
</style>
</head>
<body>
    <div id="invoice-POS">
        <div class="mid">
            <h2>23Bee Bakery</h2>
        </div>
        """)
        file.write(f"""<div id="mid">
            <div class="info">
                <hr>
                <p>
                    Nama Pengguna : {nama_pengguna}<br>
                    Nomor Telepon : {nomor_telepon}<br>
                    Pilihan : {pilihan}<br>
                    Jam : {jam}<br>
                </p>
            </div>
        </div>

        <div id="bot">
            <div id="table">
                <table>
                    <tr class="tabletitle">
                        <td class="item"><h2>Item</h2></td>
                        <td class="Hours"><h2>Qty</h2></td>
                        <td class="Rate"><h2>Sub Total</h2></td>
                    </tr>
        
        """)
        for name, details in product_dict.items():
            file.write(f"""
                    <tr class="service">
                        <td class="tableitem"><p class="itemtext">{name}</p></td>
                        <td class="tableitem"><p class="itemtext">{details['quantity']}</p></td>
                        <td class="tableitem"><p class="itemtext">Rp{details['price']}</p></td>
                    </tr>
            """)
        
        file.write(f"""
                    <tr class="tabletitle">
                        <td></td>
                        <td class="Rate"><h2>Total</h2></td>
                        <td class="payment"><h2>Rp{total_harga}</h2></td>
                    </tr>
                </table>
            </div>

            <div id="legalcopy">
                <p class="legal"><strong>Thank you for coming!</strong> Have a great day :D</p>
            </div>
        </div>
    </div>
</body>
</html>
""")


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
        # Baca file datapembeli.csv dan ambil data terbaru
        latest_data = get_latest_data_from_csv("database/datapembeli.csv")
        if latest_data:
            nama_pengguna = latest_data[0].capitalize()  # Ambil nama dari file CSV dan kapitalkan
            no_telp = latest_data[1]
            jam_input = latest_data[3].strip()  # Ambil jam dari file CSV
        else:
            # Jika tidak ada data dalam CSV, atur default
            nama_pengguna = "Unknown User"
            jam_input = "10:00 AM"
        
        metode_pembayaran = payment_var.get()
        save_order(nama_pengguna, no_telp, pilihan, jam_input, selected_products) ## COMMENT INI KALO GAMAU SAVE KE TXT
        invoice.buat_invoice_page(app, nama_pengguna, selected_pilihan.upper(), jam_input, metode_pembayaran)

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
    buat_pembayaran_page(app, sample_products, "DINE IN")
    app.mainloop()
