# ## Ini buat convert ke pdf, harus install pdfkit dulu
# ## kalo gamau dipake, bisa dikomen aja semuanya hihi

# import pdfkit
# import os

# def print_receipt():
#     # Define input HTML file path
#     html_file = 'database/customer_receipt.html'

#     # Define output PDF file path
#     output_pdf = 'customer_receipt.pdf'

#     options = {
#     'page-width': '55mm',
#     'dpi': 72,
#     'margin-top': '0mm',
#     'margin-right': '0mm',
#     'margin-bottom': '0mm',
#     'margin-left': '0mm',
#     'encoding': "UTF-8",
#     'no-outline': None
# }


#     # Convert HTML to PDF
#     pdfkit.from_file(html_file, output_pdf,options=options)

#     # os.remove("database/data_pesanan.html")

#     print(f'PDF saved to: {output_pdf}')
