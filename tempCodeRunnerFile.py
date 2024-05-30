import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def convert_txt_to_pdf(file_path, pdf_path):
    
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading1'],
        alignment=1,  # Center alignment
        fontSize=18,
        spaceAfter=10
    )
    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        alignment=1,  # Center alignment
        fontSize=10,
        textColor=colors.grey
    )

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Add title
    elements.append(Paragraph("Struk Pembelian", header_style))
    elements.append(Spacer(1, 12))

    for line in lines:
        elements.append(Paragraph(line.strip(), normal_style))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Terima kasih telah berbelanja di Toko Kami!", footer_style))

    doc.build(elements)


    # Menghapus file teks
    os.remove(txt_file)

if __name__ == "__main__":
    # Lokasi file teks yang akan dikonversi
    txt_file = "database/data_pesanan.txt"
    # Lokasi file PDF hasil konversi
    pdf_file = "customer_receipt.pdf"

    # Melakukan konversi
    convert_txt_to_pdf(txt_file, pdf_file)
