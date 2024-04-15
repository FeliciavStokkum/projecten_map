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

pdf.set_font("Arial", size=25) 
pdf.cell(30, 10, txt = "Factuur", ln = True, align = 'C')

# Set font for the title
pdf.set_font("Arial", size = 12)

# Adding logo image
pdf.image(logo_afbeelding, x=155, y=-6, w=50)  # pas x, y, en w aan volgens je behoeften

pdf.ln(20)
# Add a paragraph
pdf.cell(200, 6, txt = f"Naam: {naam}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Datum: {datum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Factuuradres: {factuur_adres}", ln = True, align = 'L')

# Save the PDF
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)