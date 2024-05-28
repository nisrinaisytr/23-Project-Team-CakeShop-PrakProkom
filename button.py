# button.py
import pemilihan
import pembayaran

def menuju_ke_pemilihan(app, pilihan, selected_products):
    pemilihan.buat_pemilihan_page(app, pilihan, selected_products)

def menuju_ke_pembayaran(app, products, pilihan):
    pembayaran.buat_pembayaran_page(app, products, pilihan)

# Fungsi-fungsi navigasi lainnya bisa ditambahkan di sini
def menuju_ke_breads(app):
    for widget in app.winfo_children():
        widget.destroy()
    import breads
    breads.buat_breads_page(app)

def balik_ke_home(app):
    for widget in app.winfo_children():
        widget.destroy()
    import homepage
    homepage.main()

def menuju_ke_cakes(app):
    from cakes import buat_cakes_page
    buat_cakes_page(app)

def menuju_ke_donuts(app):
    from donuts import buat_donuts_page
    buat_donuts_page(app)

def menuju_ke_pastry(app):
    from pastry import buat_pastry_page
    buat_pastry_page(app)
