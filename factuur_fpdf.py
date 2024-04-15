from fpdf import FPDF

naam = input("Naam van het bedrijf: ")
datum = input("Wat is de datum: ")
factuurnummer = input("Wat is het factuurnummer: ")
factuur_adres = input("Wat is het factuur adres: ")

# Create instance of FPDF class
pdf = FPDF()

# Add page
pdf.add_page()

# font for title
pdf.set_font("Arial", size = 12)

# Title
pdf.cell(200, 10, txt = "My PDF Document", ln = True, align = 'C')

# Add a paragraph
pdf.cell(200, 10, txt = f"name: {naam}", ln = True, align = 'L')

pdf.cell(200, 3, txt = f"date: {datum}", ln = True, align = 'L')

pdf.cell(200, 10, txt = f"document nummber: {factuurnummer}", ln = True, align = 'L')

pdf.cell(200, 3, txt = f"document adress: {factuur_adres}", ln = True, align = 'L')

# Save PDF
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)
