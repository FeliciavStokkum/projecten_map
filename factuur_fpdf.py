from fpdf import FPDF

# naam = input("Naam van het bedrijf: ")
# datum = input("Wat is de datum: ")
# factuurnummer = input("Wat is het factuurnummer: ")
# factuur_adres = input("Wat is het factuur adres: ")
naam = ("pookie <3")
datum = ("vandaag")
factuurnummer = ("69")
factuur_adres = ("berkel")
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'
prijs = 0
prijs_totaal = 0

# Create instance of FPDF class
pdf = FPDF()

# Add page
pdf.add_page()

# title size
pdf.set_font("Arial", size = 25)
pdf.ln(10)
pdf.cell(200, 10, txt = "INVOICE", ln = True, align = 'L')

# font for title
pdf.set_font("Arial", size = 12)

# Adding logo image
pdf.image(logo_afbeelding, x=155, y=-6, w=50)  # pas x, y, en w aan volgens je behoeften

# Add space
pdf.ln(10)

# Add a paragraph

pdf.cell(200, 3, txt = f"date: {datum}", ln = True, align = 'L')

pdf.cell(195, 10, txt = "Factuur Enzo", ln = True, align = 'R')

pdf.cell(195, 10, txt = "Tell: +316 85 12 34 56", ln = True, align = 'R')

pdf.cell(200, 10, txt = f"name: {naam}", ln = True, align = 'L')

pdf.cell(200, 10, txt = f"document nummber: {factuurnummer}", ln = True, align = 'L')

pdf.cell(200, 3, txt = f"document adress: {factuur_adres}", ln = True, align = 'L')

pdf.ln(10)

data = [['aantal', 'omschrijving', 'prijs per eenheid', 'regeltotaal'],
        ['8 uur', 'consulancy', '€' + prijs, '€' + prijs_totaal],
        ['1', 'omderhoud boekhoudsysteem', '€' + prijs, '€' + prijs_totaal],
        ['product', 'flipover classic', '€' + prijs, '€' + prijs_totaal]]

for row in data:
    for item in row:
        # Add cell with padding
        pdf.cell(40, 10, txt=item, border=1)
    pdf.ln()

# Save PDF
pdf_output = "my_pdf_document.pdf"
pdf.output(pdf_output)