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

def menuju_ke_register(app):
    for widget in app.winfo_childern():
        widget.destroy()
        import Register
        Register.main()

def menuju_ke_cakes(app):
    for widget in app.winfo_children():
        widget.destroy()
    import cakes
    cakes.buat_cakes_page(app)

def menuju_ke_donuts(app):
    for widget in app.winfo_children():
        widget.destroy()
    import donuts
    donuts.buat_donuts_page(app)

def menuju_ke_pastry(app):
    for widget in app.winfo_children():
        widget.destroy()
    import pastry
    pastry.buat_pastry_page(app)