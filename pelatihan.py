import pandas as pd
import customtkinter as ctk
from PIL import Image, ImageTk
from tombol_balik import balik_ke_home

def baca_detail_produk():
    def buat_product_page(app):
        for widget in app.winfo_children():
            widget.destroy()
        
        frame1 = ctk.CTkFrame(master=app, width=450, height=255, corner_radius=15)
        frame1.place(relx=0.695, rely=0.385, anchor="sw")

        harga_produk = ctk.CTkLabel(master=frame1, text="HARGA PRODUK", font=ctk.CTkFont(size=30, weight="bold"))
        harga_produk.place(relx=0.05 , rely=0.07)

        merkmodel_produk = ctk.CTkLabel(master=frame1, text="MERK - MODEL", font=ctk.CTkFont(size=30, family="Arial"))
        merkmodel_produk.place(relx=0.05, rely=0.27)

        tahun_produk = ctk.CTkLabel(master=frame1, text="TAHUN", font=ctk.CTkFont(size=25, family="Arial"))
        tahun_produk.place(relx=0.05, rely=0.47)

        km_produk = ctk.CTkLabel(master=frame1, text="JARAK TEMPUH", font=ctk.CTkFont(size=25, family="Arial"))
        km_produk.place(relx=0.05, rely=0.63)

        lokasi_produk = ctk.CTkLabel(master=frame1, text="PROVINSI - KOTA - KECAMATAN", font=ctk.CTkFont(size=20, family="Arial"))
        lokasi_produk.place(relx=0.05 , rely=0.8)

        frame2 = ctk.CTkFrame(master=app, width=450, height=200, corner_radius=15)
        frame2.place(relx=0.695, rely=0.69, anchor="sw")

        gmail_penjual = ctk.CTkLabel(master=frame2, text="GMAIL", font=ctk.CTkFont(size=30, weight="bold"))
        gmail_penjual.place(relx=0.05, rely=0.25)

        nomorwa_penjual = ctk.CTkLabel(master=frame2, text="NOMOR WA", font=ctk.CTkFont(size=30, weight="bold"))
        nomorwa_penjual.place(relx=0.05, rely=0.55)

        frame3 = ctk.CTkFrame(master=app, width=1000, height=500, corner_radius=15)
        frame3.place(x=50, y=50)

        image_path = "tubes\\FOTO PRODUK\\MONSTER.jpg"
        original_image = Image.open(image_path)

        panjang_baru = 500  # New width
        lebar_baru = 300    # New height
        resized_image = original_image.resize((panjang_baru, lebar_baru), Image.LANCZOS)

        gambar1 = ctk.CTkImage(light_image=resized_image, size=(panjang_baru, lebar_baru))

        memuat_gambar1 = ctk.CTkLabel(master=frame3, image=gambar1, text="")
        memuat_gambar1.place(relx=0.5, rely=0.5, anchor="center")

        frame4 = ctk.CTkFrame(master=app, width=1000, height=200, corner_radius=15)
        frame4.place(x=50, y=575)

        judul_frame4 = ctk.CTkLabel(master=frame4, text="DETAIL MOTOR", font=ctk.CTkFont(size=30, weight="bold"))
        judul_frame4.place(relx=0.01, rely=0.05)

        deskripsi_produk = ctk.CTkLabel(master=frame4, text="DESKRIPSI", font=ctk.CTkFont(size=20))
        deskripsi_produk.place(relx=0.01, rely=0.25)

        tombol_kembali = ctk.CTkButton(master=app, text="Kembali", command=lambda: balik_ke_home(app))
        tombol_kembali.place(relx=0.01, rely=0.01)

    app = ctk.CTk()
    buat_product_page(app)
    app.mainloop()

if __name__ == "__main__":
    baca_detail_produk()
