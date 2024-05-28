import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import string
import os

# Function to generate random payment code
def generate_random_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def print_invoice(app):
    # Implement print functionality here
    # For now, we just simulate print action
    messagebox.showinfo("Print", "Print berhasil dilakukan, selamat menikmati kue anda.")
    app.destroy()
    import homepage
    homepage.main()

def go_back(app):
    app.destroy()
    import pembayaran
    pembayaran.main()

def buat_invoice_page(app, nama, pilihan, jam, pembayaran):
    app.geometry("900x500")
    
    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Header Frame
    header_frame = ctk.CTkFrame(app)
    header_frame.grid(row=0, column=0, sticky="nw")

    back_button = ctk.CTkButton(header_frame, text="Back", command=lambda: go_back(app), fg_color="#FFADA1")
    back_button.grid(row=0, column=0, padx=10, pady=10)

    # Invoice Frame
    invoice_frame = ctk.CTkFrame(app, width=700, height=450)
    invoice_frame.grid(row=0.5, column=0.5, columnspan=2, pady=20,anchor=tk.CENTER)

    title_label = ctk.CTkLabel(invoice_frame, text="KODE PEMBAYARAN", justify="center", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=15)

    greeting_label = ctk.CTkLabel(invoice_frame, text=f"Yth {nama}, Kode pembayaran anda adalah:", justify="center", font=("Arial", 16))
    greeting_label.grid(row=1, column=0, columnspan=2, pady=5)

    payment_code = generate_random_code()
    code_label = ctk.CTkLabel(invoice_frame, text=f"{payment_code}", justify="center", font=("Arial", 24, "bold"))
    code_label.grid(row=2, column=0, columnspan=2, pady=15)

    # Conditional message based on selection and payment
    if pilihan == "Delivery":
        message_line_1 = f"Pesanan anda akan diantar pada pukul {jam}, estimasi pengiriman sekitar 30 menit."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tunai tagihan anda dengan menunjukkan kode pembayaran ini kepada driver anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking dan e-wallet anda dengan kode pembayaran berikut. Waktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    elif pilihan == "Take Away":
        message_line_1 = f"Pesanan anda dapat diambil pada pukul {jam}."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tagihan anda di kasir dengan menunjukkan kode pembayaran anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking dan e-wallet anda dengan kode pembayaran berikut. Waktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    elif pilihan == "Dine In":
        message_line_1 = f"Pesanan anda akan siap pada pukul {jam}, silahkan datang ke tempat pada jam tersebut."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tagihan anda di kasir dengan menunjukkan kode pembayaran anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking dan e-wallet anda dengan kode pembayaran berikut. Waktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    
    message_label_1 = ctk.CTkLabel(invoice_frame, text=message_line_1, justify="center", font=("Arial", 12))
    message_label_1.grid(row=3, column=0, columnspan=2, pady=5)
    message_label_2 = ctk.CTkLabel(invoice_frame, text=message_line_2, justify="center", font=("Arial", 12))
    message_label_2.grid(row=4, column=0, columnspan=2, pady=5)

    print_button = ctk.CTkButton(app, text="PRINT", command=lambda: print_invoice(app), fg_color="#FFADA1")
    print_button.grid(row=2, column=0, columnspan=2, pady=20)

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Cakeshop - Invoice")
    # Example usage
    buat_invoice_page(app, "Nama Pengguna", "delivery", "10:00 AM", "tunai")
    app.mainloop()
