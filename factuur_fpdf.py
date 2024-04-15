from fpdf import FPDF

naam = input("Naam van het bedrijf: ")
datum = ("Wat is de datum: ")
factuurnummer = ("Wat is het factuurnummer: ")
factuur_adres = ("Wat is het factuur adres: ")

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font for the title
pdf.set_font("Arial", size = 12)

# Title
pdf.cell(200, 10, txt = "My PDF Document", ln = True, align = 'C')

# Add a paragraph
pdf.cell(200, 10, txt = f"name: {naam}", ln = True, align = 'L')

# Add another paragraph
pdf.cell(200, 10, txt = "This is another paragraph in the PDF.", ln = True, align = 'L')

# Save the PDF
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)
