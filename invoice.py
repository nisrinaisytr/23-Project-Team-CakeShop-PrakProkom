import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import string
import os
from PIL import Image, ImageTk
import webbrowser
import subprocess
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
    elements.append(Paragraph("DETAIL TRANSAKSI", styles['Title']))
    elements.append(Paragraph("_____________________________________________", styles['Title']))

    # Customer Info
    elements.append(Paragraph(f"Nama: {nama}", styles['Normal']))
    elements.append(Paragraph(f"Telepon: {telepon}", styles['Normal']))
    elements.append(Paragraph(f"Kode pembayaran anda adalah: <b>{payment_code}</b>\n", styles['Normal']))
    elements.append(Paragraph("", styles['Title']))

    # Items Table
    table_data = [['Produk', 'Harga']]
    for item in items:
        table_data.append(item)
    table_data.append(['Total', f"Rp{total_harga:,}"])

    # Membuat objek Table dengan kolom yang lebih lebar dan baris yang lebih pendek
    table = Table(table_data, colWidths=[225, 225], rowHeights=[20] * len(table_data))  # Adjusting column widths and row heights

    # Menetapkan gaya tabel
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),  # Adjust padding to reduce row height
        ('TOPPADDING', (0, 1), (-1, -1), 6),    # Adjust padding to reduce row height
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6), # Adjust padding to reduce row height
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),  # Adjust font size
    ]))

    elements.append(table)

    # Messages
    elements.append(Paragraph("", styles['Title']))

    elements.append(Paragraph(message_line_1, styles['Normal']))
    elements.append(Paragraph(message_line_2, styles['Normal']))

    # Footer
    elements.append(Paragraph("", styles['Title']))
    elements.append(Paragraph("", styles['Title']))
    elements.append(Paragraph("Terima Kasih, Silahkan menikmati Kue anda!!", styles['Normal']))

    doc.build(elements)

    messagebox.showinfo("Print", f"Print berhasil dilakukan. PDF disimpan sebagai {pdf_file}.")
    webbrowser.open_new_tab(pdf_file)

    app.destroy()
    #import homepage
    subprocess.Popen(['python','homepage.py','main(app)'])
    #homepage.main()

#def go_back(app):
 #   for widget in app.winfo_children():
  #      widget.destroy()
   # import button
    #button.balik_ke_home(app)
  #  app.destroy()
   # import homepage
    #homepage.main()


def buat_invoice_page(app, nama, telepon, pilihan, jam, pembayaran, items, total_harga):
    app.geometry("1270x710")
    
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

    # Header Frame
    from button import balik_ke_home
    back_button = ctk.CTkButton(app, text="Back",text_color='white',fg_color='#DB7575', command=lambda:balik_ke_home(app))
    back_button.pack(side="top", padx=15, pady=30)
    back_button.place(rely=0.02,relx=0.01)

    # Invoice Frame
    invoice_frame = ctk.CTkFrame(app,fg_color='white', width=900, height=600)
    invoice_frame.place(relx=0.5, rely=0.4, anchor="center")
    invoice_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content


    title_label = ctk.CTkLabel(invoice_frame,text_color='#DB7575', text="KODE PEMBAYARAN", justify="center", font=("Arial", 30, "bold"))
    title_label.grid(row=2, column=0, columnspan=3, pady=(35,1), padx=120)

    line_label = ctk.CTkLabel(invoice_frame, text_color='#DB7575',text="_________________________________________________________________________________________________", justify="center", font=("Arial", 12, "bold"))
    line_label.grid(row=3, column=0, columnspan=3, pady=(0,13))


    greeting_label = ctk.CTkLabel(invoice_frame,text_color='#DB7575', text=f"Yth {nama}, Kode pembayaran anda adalah:", justify="center", font=("Arial", 16))
    greeting_label.grid(row=4, column=0, columnspan=3, pady=5)

    payment_code = generate_random_code()
    code_label = ctk.CTkLabel(invoice_frame, text=f"{payment_code}",text_color='#c9281c', justify="center", font=("Arial", 24, "bold"))
    code_label.grid(row=5, column=0, columnspan=3, pady=15)

    print_button = ctk.CTkButton(app, text="PRINT", command=lambda: print_invoice(app, nama, telepon, pilihan, jam, pembayaran, payment_code, items, total_harga, message_line_1, message_line_2), text_color='white',fg_color='#DB7575')
    print_button.place(relx=0.5, rely=0.7, anchor="center")  # Center confirm button at bottom
    

    print(f"Pilihan pada Invoice: {pilihan}")
    print(f"Pilihan pembayaran anda: {pembayaran}")

    # Conditional message based on selection and payment
    if pilihan == "DELIVERY":
        message_line_1 = f"Pesanan anda akan diantar pada pukul {jam}, estimasi pengiriman sekitar 30 menit."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tunai tagihan anda dengan menunjukkan kode pembayaran ini kepada driver anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking atau e-wallet anda dengan kode pembayaran berikut. \nWaktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    elif pilihan == "TAKEAWAY":
        message_line_1 = f"Pesanan anda dapat diambil pada pukul {jam}."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tagihan anda di kasir dengan menunjukkan kode pembayaran anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking atau e-wallet anda dengan kode pembayaran berikut. \nWaktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    elif pilihan == "DINE IN":
        message_line_1 = f"Pesanan anda akan siap pada pukul {jam}, silahkan datang ke tempat pada jam tersebut."
        if pembayaran == "Tunai":
            message_line_2 = "Silahkan bayar tagihan anda di kasir dengan menunjukkan kode pembayaran anda."
        else:
            message_line_2 = "Silahkan lakukan pembayaran melalui m-banking atau e-wallet anda dengan kode pembayaran berikut. \nWaktu maksimal pembayaran adalah 1x24 jam sejak kode diterima."
    
    message_label_1 = ctk.CTkLabel(invoice_frame, text=message_line_1,text_color='#DB7575', justify="center", font=("Arial", 16))
    message_label_1.grid(row=6, column=0, columnspan=3, pady=(15,0))
    message_label_2 = ctk.CTkLabel(invoice_frame, text=message_line_2,text_color='#DB7575', justify="center", font=("Arial", 16))
    message_label_2.grid(row=7, column=0, columnspan=3, pady=(10,50), padx=55)


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
