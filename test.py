from pypdf import *
from fpdf import *
from reportlab.pdfgen.canvas import Canvas

# naam = input("Naam van het bedrijf: ")
# datum = ("Wat is de datum: ")
# factuurnummer = ("Wat is het factuurnummer: ")
# factuur_adres = ("Wat is het factuur adres: ")

# canvas = Canvas("test.pdf")
# canvas.drawString(72, 72, "Hello, World!")s

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "b", "24")