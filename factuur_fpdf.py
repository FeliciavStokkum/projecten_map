from fpdf import FPDF

naam = input("Naam van het bedrijf: ")
datum = input("Wat is de datum: ")
factuurnummer = input("Wat is het factuurnummer: ")
factuur_adres = input("Wat is het factuur adres: ")
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'
data = [['Beschrijving', 'Aantal', 'Eenheid', 'Tarief', 'BTW%', 'BTW', 'Totaal'],
        ['Werk', 'xxx', 'uur', '€xx', 'xx%', '€xx', '€xx'],
        ['Producten', 'xxx', 'stuk', '€xx', 'xx%', '€xx', '€xx']]

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
pdf.cell(200, 6, txt = f"{datum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Factuuradres: {factuur_adres}", ln = True, align = 'L')

pdf.set_y(40)
pdf.cell(190, 6, txt = f"Factuur Enzo", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"+31 6123456789", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo@help.com", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo.nl", ln = True, align = 'R')

pdf.ln(10)

# Adding table
for row in data:
    for item in row:
        # Add cell with padding
        pdf.cell(40, 10, txt=item, border=1)
    pdf.ln()

# Save the PDF
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)