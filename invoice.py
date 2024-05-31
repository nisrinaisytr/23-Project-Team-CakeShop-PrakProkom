import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import string
import os
import webbrowser
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Function to generate random payment code
def generate_random_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def print_invoice(app, nama, telepon, pilihan, jam, pembayaran, payment_code, items, total_harga, message_line_1, message_line_2):
    pdf_file = f"Tiket_{payment_code}.pdf"
    
    # Create PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("KODE PEMBAYARAN", styles['Title']))

    # Customer Info
    elements.append(Paragraph(f"Yth {nama}", styles['Normal']))
    elements.append(Paragraph(f"Telepon\t\t: {telepon}", styles['Normal']))
    elements.append(Paragraph(f"Kode pembayaran anda adalah\t: <b>{payment_code}</b>\n", styles['Normal']))

    # Items Table
    table_data = [['Produk', 'Harga']]
    for item in items:
        table_data.append(item)
    table_data.append(['Total', f"Rp{total_harga:,}"])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Messages
    elements.append(Paragraph(message_line_1, styles['Normal']))
    elements.append(Paragraph(message_line_2, styles['Normal']))

    # Footer
    elements.append(Paragraph("Terima Kasih, Silahkan menikmati Kue anda!!", styles['Normal']))

    doc.build(elements)

    messagebox.showinfo("Print", f"Print berhasil dilakukan, selamat menikmati kue anda. PDF disimpan sebagai {pdf_file}.")
    webbrowser.open_new_tab(pdf_file)

    app.destroy()
    import homepage
    homepage.main()

#def go_back(app):
 #   for widget in app.winfo_children():
  #      widget.destroy()
   # import button
    #button.balik_ke_home(app)
  #  app.destroy()
   # import homepage
    #homepage.main()

def buat_invoice_page(app, nama, telepon, pilihan, jam, pembayaran, items, total_harga):
    app.geometry("900x500")
    
    # Clear previous widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Header Frame
    header_frame = ctk.CTkFrame(app)
    header_frame.grid(row=0, column=0, sticky="nw")
    from button import balik_ke_home
    back_button = ctk.CTkButton(header_frame, text="Back", command=lambda:balik_ke_home(app), fg_color="#FFADA1")
    back_button.grid(row=0, column=0, padx=10, pady=10)

    # Invoice Frame
    invoice_frame = ctk.CTkFrame(app, width=900, height=650)
    invoice_frame.grid(row=1, column=0, columnspan=2, padx=90 ,pady=20)

    title_label = ctk.CTkLabel(invoice_frame, text="KODE PEMBAYARAN", justify="center", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=15)

    greeting_label = ctk.CTkLabel(invoice_frame, text=f"Yth {nama}, Kode pembayaran anda adalah:", justify="center", font=("Arial", 16))
    greeting_label.grid(row=1, column=0, columnspan=2, pady=5)

    payment_code = generate_random_code()
    code_label = ctk.CTkLabel(invoice_frame, text=f"{payment_code}", justify="center", font=("Arial", 24, "bold"))
    code_label.grid(row=2, column=0, columnspan=2, pady=15)

    print_button = ctk.CTkButton(app, text="PRINT", command=lambda: print_invoice(app, nama, telepon, pilihan, jam, pembayaran, payment_code, items, total_harga, message_line_1, message_line_2), fg_color="#FFADA1")
    print_button.grid(row=2, column=0, columnspan=2, pady=20)

    print(f"Pilihan pada Invoice: {pilihan}")
    print(f"Pilihan pembayaran anda: {pembayaran}")

    # Conditional message based on selection and payment
    if pilihan == "DELIVERY":
        message_line_1 = f"Pesanan anda akan diantar pada pukul {jam}, estimasi pengiriman sekitar 30 menit."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tunai tagihan anda dengan menunjukkan kode pembayaran ini kepada driver anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking dan e-wallet anda dengan kode pembayaran berikut. Waktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    elif pilihan == "TAKEAWAY":
        message_line_1 = f"Pesanan anda dapat diambil pada pukul {jam}."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tagihan anda di kasir dengan menunjukkan kode pembayaran anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking dan e-wallet anda dengan kode pembayaran berikut. Waktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    elif pilihan == "DINE IN":
        message_line_1 = f"Pesanan anda akan siap pada pukul {jam}, silahkan datang ke tempat pada jam tersebut."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tagihan anda di kasir dengan menunjukkan kode pembayaran anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking dan e-wallet anda dengan kode pembayaran berikut. Waktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    
    message_label_1 = ctk.CTkLabel(invoice_frame, text=message_line_1, justify="center", font=("Arial", 16))
    message_label_1.grid(row=3, column=0, columnspan=2, pady=5)
    message_label_2 = ctk.CTkLabel(invoice_frame, text=message_line_2, justify="center", font=("Arial", 16))
    message_label_2.grid(row=4, column=0, columnspan=2, pady=5)


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Cakeshop - Invoice")
    # Example usage
    items = [
        ["Kue Coklat", 50000],
        ["Kue Keju", 60000],
        ["Kue Strawberry", 70000],
    ]
    total_harga = sum(item[1] for item in items)
    buat_invoice_page(app, "Nama Pengguna", "081234567890", "TAKEAWAY", "10:00 AM", "Tunai", items, total_harga)
    app.mainloop()
