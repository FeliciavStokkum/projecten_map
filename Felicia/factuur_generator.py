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
vervaldatum = datum
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'
data = [['Beschrijving', 'Aantal', 'Eenheid', 'Tarief', 'BTW%', 'BTW', 'Totaal'],
        ['Werk', 'xxx', 'uur', 'xx', 'xx%', 'xx', 'xx'],
        ['Producten', 'xxx', 'stuk', 'xx', 'xx%', 'xx', 'xx']]

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

pdf.set_font("Arial", size=25) 
pdf.cell(30, 10, txt = "Factuur", ln = True, align = 'C')

# Set font for the title
pdf.set_font("Arial", size = 12)

# Adding logo image
pdf.image(logo_afbeelding, x=155, y=-6, w=50)  # pas x, y, en w aan volgens je behoeften

pdf.ln(20)
# Add a paragraph
pdf.cell(200, 6, txt = f"{naam}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"{factuur_adres}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"{factuur_postcode}", ln = True, align = 'L')

pdf.set_y(40)
pdf.cell(190, 6, txt = f"Factuur Enzo", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"+31 6123456789", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo@help.com", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo.nl", ln = True, align = 'R')


pdf.cell(200, 6, txt = f"Datum: {datum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Relatienummer: {relatienummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Verval datum: {vervaldatum}", ln = True, align = 'L')

pdf.set_y(100)
for row in data:
    for item in row:
        # Add cell with padding
        pdf.cell(27, 10, txt=item, border=1)
    pdf.ln()

pdf.cell(170, 5, txt="Bedrag excl BTW: ", ln=True, align='R') 
pdf.cell(170, 5, txt="BTW: ", ln=True, align='R')
pdf.cell(170, 5, txt="Totaal bedrag: ", ln=True, align='R')

#Voegt een horizontale lijn onderaan de pagina toe
pdf.set_draw_color(0, 0, 0)  
y_position = 245 # De y-coördinaat voor de lijn (iets boven de onderkant van een A4-pagina, die 297 mm hoog is)
pdf.line(10, y_position, 200, y_position) 

# Stel de positie in net onder de getekende lijn
pdf.set_y(y_position + 5)
# Voeg tekst toe onder de lijn
pdf.set_font("Arial", 'B', 8)
pdf.cell(0, 5, 'Factuur enzo', ln=True)
pdf.set_font("Arial", size=8) 
pdf.cell(0, 5, 'Leerparkpromenade 100', ln=True) 
pdf.cell(0, 5, '3312 KW Dordrecht', ln=True)
pdf.cell(0, 5, 'BTW nummer: 111234567B01', ln=True)
pdf.cell(0, 5, 'KVK nummer: 9305 6589', ln=True)

pdf.set_y(y_position + 5) 
pdf.set_font("Arial", 'B', 8)
pdf.cell(0, 5, 'Contact informatie', ln=True, align='C')
pdf.set_font("Arial", size=8) 
pdf.cell(0, 5, 'contactpersonen: Felicia en Bent', ln=True, align='C') 
pdf.cell(0, 5, 'Telefoon: +31 6123456789', ln=True, align='C')
pdf.cell(0, 5, 'Email: factuurenzo@help.com', ln=True, align='C')
pdf.cell(0, 5, 'website: factuurenzo.nl', ln=True, align='C')

pdf.set_y(y_position + 5) 
pdf.set_font("Arial", 'B', 8)
pdf.cell(0, 5, 'Betaalgegevens', ln=True, align='R')
pdf.set_font("Arial", size=8) 
pdf.cell(0, 5, 'Bank: RaboBank', ln=True, align='R') 
pdf.cell(0, 5, 'BIC nummer: RABONL2U', ln=True, align='R')
pdf.cell(0, 5, 'IBAN nummer: NL44 RABO 0123 4567 89', ln=True, align='R')

# Assume this function generates and saves a QR code
def generate_qr_code(data, filename="qr_code.png"):
    import qrcode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

# Variables (just examples)
data = "Sample Data for QR"
generate_qr_code(data)

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

    # Save the modified page back to a new PDF
    pdf_bytes = io.BytesIO()
    pdf_page_image.save(pdf_bytes, format='0')
    pdf_bytes.seek(0)
    modified_page = PdfReader(pdf_bytes).pages[0]
    writer.add_page(modified_page)

# Save the output PDF
with open("output_with_qr.pdf", "wb") as f_out:
    writer.write(f_out)

#De PDF wordt opgeslagen
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)