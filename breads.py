import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk
import os

# Warna dan Font
bg_color = "#FFEFE8"
text_color = "#FF7A8A"
button_color = "#FFADA1"
menu_color = "#FFD9CC"
font_title = ("Arial", 30, "bold")
font_subtitle = ("Arial", 20, "bold")
font_text = ("Arial", 12)

# Fungsi untuk memuat produk dari file CSV
def load_products(file_path):
    products = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'name': row['name'],
                'image': os.path.join('images', row['image']),  # Sesuaikan jalur gambar
                'price': int(row['price'])
            })
    return products

# Fungsi untuk memilih produk dan memperbarui jumlah dan total harga
def select_product(product):
    global selected_products, total_cost
    selected_products.append(product)
    total_cost += product['price']
    update_display()

# Fungsi untuk memperbarui tampilan jumlah produk yang dipilih dan total harga
def update_display():
    global selected_count_label, total_cost_label
    selected_count_label.configure(text=f"Jumlah produk yang dipilih: {len(selected_products)}")
    total_cost_label.configure(text=f"Rp {total_cost}")

# Fungsi untuk kembali ke halaman utama
def go_back():
    root.destroy()
    os.system('python homepage.py')

# Fungsi untuk menampilkan menu produk
def display_menu(csv_file):
    products = load_products(os.path.join('database', csv_file))
    
    product_frame = ctk.CTkFrame(root)
    product_frame.pack(pady=18, padx=12, expand=True, fill=tk.BOTH)
    
    for index, product in enumerate(products):
        row = index // 5
        column = index % 5

        product_card = ctk.CTkFrame(product_frame)
        product_card.grid(row=row, column=column, padx=18, pady=12)

        image = Image.open(product['image'])
        image = image.resize((150, 150), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)

        img_label = ctk.CTkLabel(product_card, image=img)
        img_label.pack()

        button = ctk.CTkButton(product_card, text=f"Rp {product['price']}", command=lambda p=product: select_product(p), fg_color=button_color)
        button.pack()

# Fungsi main untuk memanggil display_menu() saat modul ini dieksekusi
def main():
    global root, selected_products, total_cost, selected_count_label, total_cost_label
# Membuat jendela utama aplikasi
    root = ctk.CTk()
    root.title("Cakeshop - Breads")
    root.geometry("900x500")

    selected_products = []
    total_cost = 0

    # Frame untuk header (judul dan tombol back)
    header_frame = ctk.CTkFrame(root)
    header_frame.pack(fill=tk.X)

    back_button = ctk.CTkButton(header_frame, text="Back", command=go_back, fg_color=button_color)
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

    title_label = ctk.CTkLabel(header_frame, text="BREADS",justify="center", font=font_title)
    title_label.pack(side=tk.TOP, pady=15)

    # Menampilkan menu produk dari database/breads.csv
    display_menu('breads.csv')

    # Membuat frame bawah untuk total dan tombol aksi
    bottom_frame = ctk.CTkFrame(root)
    bottom_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)

    selected_count_label = ctk.CTkLabel(bottom_frame, text="Jumlah produk yang dipilih: 0")
    selected_count_label.pack(side=tk.LEFT, padx=20)

    total_cost_label = ctk.CTkLabel(bottom_frame, text="Rp 0")
    total_cost_label.pack(side=tk.RIGHT, padx=20)

    # Tombol aksi
    action_frame = ctk.CTkFrame(bottom_frame)
    action_frame.pack(pady=10)

    takeaway_button = ctk.CTkButton(action_frame, text="TAKEAWAY",fg_color=button_color, command=lambda: messagebox.showinfo("Takeaway", "Takeaway option selected"))
    takeaway_button.grid(row=0, column=0, padx=5)

    delivery_button = ctk.CTkButton(action_frame, text="DELIVERY",fg_color=button_color, command=lambda: messagebox.showinfo("Delivery", "Delivery option selected"))
    delivery_button.grid(row=0, column=1, padx=5)

    dinein_button = ctk.CTkButton(action_frame, text="DINE IN",fg_color=button_color, command=lambda: messagebox.showinfo("Dine In", "Dine In option selected"))
    dinein_button.grid(row=0, column=2, padx=5)

    root.mainloop()
# Panggil fungsi main jika modul ini dieksekusi secara langsung
if __name__ == "__main__":
    main()