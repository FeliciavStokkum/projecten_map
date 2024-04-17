#Calculaties
#Qr code maken
#opmaak verbeteren
#inputs werk en producten

from fpdf import FPDF

naam = ("Naam: ")
datum = ("Datum van vandaag: ")
factuurnummer = ("Factuurnummer: ")
factuur_adres = ("Factuur adres:  ")
factuur_postcode = ("Postcode: ")
relatienummer = ("Relatienummer: ")
uren = int(input("Hoeveel uur: "))
producten = int(input("Hoeveel producten: "))

kosten_uren = 60
kosten_product = 106

uren_prijs = uren * kosten_uren
producten_prijs = producten * kosten_product
uren_btw = round(uren_prijs * 0.21, 2)
producten_btw = round(producten_prijs * 0.21, 2)
uren_prijs_totaal = uren_prijs + uren_btw
producten_prijs_totaal = producten_prijs + producten_btw
beide_prijs = round(uren_prijs + producten_prijs,2 )
beide_btw = round(uren_btw + producten_btw, 2)
beide_prijs_totaal = round(uren_prijs_totaal + producten_prijs_totaal, 2)

vervaldatum = datum
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'
data = [['Beschrijving', 'Aantal', 'Eenheid', 'Tarief', 'BTW%', 'BTW', 'Totaal'],
        ['Uren', f'{uren}', 'uur', f'{kosten_uren} EUR', '21%', f'{uren_btw} EUR', f'{uren_prijs_totaal} EUR'],
        ['Producten', f'{producten}', 'stuk', f'{kosten_product} EUR', '21%', f'{producten_btw} EUR', f'{producten_prijs_totaal} EUR']]

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

pdf.cell(170, 5, txt=f"Bedrag excl BTW: {beide_prijs} EUR", ln=True, align='R') 
pdf.cell(170, 5, txt=f"BTW: {beide_btw} EUR", ln=True, align='R')
pdf.cell(170, 5, txt=f"Totaal bedrag: {beide_prijs_totaal} EUR", ln=True, align='R')

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

#De PDF wordt opgeslagen
pdf_output = "factuur_bent_editie.pdf"
pdf.output(pdf_output)