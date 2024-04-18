#Calculaties
#Qr code maken
#opmaak verbeteren
#inputs werk en producten

from fpdf import FPDF
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import io

naam = ("Naam: ")
datum = ("Datum van vandaag: ")
factuurnummer = ("Factuurnummer: ")
factuur_adres = ("Factuur adres:  ")
factuur_postcode = ("Postcode: ")
relatienummer = ("Relatienummer: ")
uren = input("Hoeveel uur: ")
producten = input("Hoeveel producten: ")
vervaldatum = datum
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'

data = [['Beschrijving', 'Aantal', 'Eenheid', 'Tarief', 'BTW%', 'BTW', 'Totaal'],
        ['Uren', 'xxx', 'uur', 'xx', 'xx%', 'xx', 'xx'],
        ['Producten', 'xxx', 'stuk', 'xx', 'xx%', 'xx', 'xx'],
        ['Uren', uren, 'uur', 'xx', '21%', 'xx', 'xx'],
        ['Producten', producten, 'stuk', 'xx', '21%', 'xx', 'xx']]

# Create instance of FPDF class
pdf = FPDF()

pdf.cell(190, 6, txt = f"factuurenzo@help.com", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo.nl", ln = True, align = 'R')


pdf.cell(200, 6, txt = f"Datum: {datum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Relatienummer: {relatienummer}", ln = True, align = 'L')

pdf.cell(0, 5, 'BIC nummer: RABONL2U', ln=True, align='R')
pdf.cell(0, 5, 'IBAN nummer: NL44 RABO 0123 4567 89', ln=True, align='R')

# Assume this function generates and saves a QR code
# def generate_qr_code(data, filename="qr_code.png"):
#     import qrcode
#     qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
#     qr.add_data(data)
#     qr.make(fit=True)
#     img = qr.make_image(fill='black', back_color='white')
#     img.save(filename)

# # Variables (just examples)
# data = "Sample Data for QR"
# generate_qr_code(data)

# Create instance of FPDF class and build your PDF (simplified)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Sample Invoice", ln=1, align='C')
pdf.cell(200, 10, "Sample Item", ln=1)
pdf.output("my_pdf_document.pdf")

# Read the newly created PDF
reader = PdfReader("my_pdf_document.pdf")
writer = PdfWriter()

# Load the QR code image
qr_image = Image.open("qr_code.png")

# Loop through all the pages and add the QR code to each page
for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    # Convert PyPDF2 page to a PIL Image (This requires additional setup; not directly possible as written)
    # Using a placeholder operation here
    pdf_page_image = Image.new('RGB', (210, 297), 'white')  # Assuming A4 size, convert dimensions appropriately
    pdf_page_image.paste(qr_image, (0, 0))  # Adjust position as needed

    # # Save the modified page back to a new PDF
    # pdf_bytes = io.BytesIO()
    # pdf_page_image.save(pdf_bytes, format='0')
    # pdf_bytes.seek(0)
    # modified_page = PdfReader(pdf_bytes).pages[0]
    # writer.add_page(modified_page)

# Save the output PDF
with open("output_with_qr.pdf", "wb") as f_out:
    writer.write(f_out)

#De PDF wordt opgeslagen
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)