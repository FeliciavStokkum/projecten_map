from pypdf import *
from fpdf import *
from reportlab.pdfgen.canvas import Canvas

naam = ("Naam van het bedrijf: ")
datum = ("Wat is de datum: ")
factuurnummer = ("Wat is het factuurnummer: ")
factuur_adres = ("Wat is het factuur adres: ")
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font for the title
pdf.set_font("Arial", size = 12)

# Title
pdf.cell(200, 10, txt = "Factuur", ln = True, align = 'C')

# Adding logo image
pdf.image(logo_afbeelding, x=130, y=8, w=50)  # pas x, y, en w aan volgens je behoeften

# Add a paragraph
pdf.cell(200, 10, txt = f"Naam: {naam}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Datum: {datum}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Factuuradres: {factuur_adres}", ln = True, align = 'L')

# Add another paragraph
pdf.cell(200, 10, txt = "This is another paragraph in the PDF.", ln = True, align = 'L')

# Save the PDF
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)