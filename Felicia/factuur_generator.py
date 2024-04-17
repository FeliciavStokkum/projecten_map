#Qr code maken
#opmaak verbeteren
from fpdf import FPDF
import json
import datetime

pdf = FPDF()
pdf.add_page()
data_json = json.load(open("Felicia/test_set_PC/2020-375.json"))


naam = data_json["factuur"]["klant"]["naam"]
datum = datetime.date.today()
kvk_nummer = data_json["factuur"]["klant"]["KVK-nummer"]
factuurnummer = data_json["factuur"]["factuurnummer"]
factuur_adres = data_json["factuur"]["klant"]["adres"]
factuur_postcode = data_json["factuur"]["klant"]["postcode"]
factuur_stad = data_json["factuur"]["klant"]["stad"]
betaaltermijn_str = data_json["factuur"]["betaaltermijn"]
betaaltermijn_dagen = int(betaaltermijn_str.split('-')[0])
bedrag_excl_btw = 0
bedrag_btw = 0
bedrag_totaal = 0

kosten_uren = 60
kosten_product = 106

vervaldatum = datum + datetime.timedelta(days=betaaltermijn_dagen)
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'
data = [['Beschrijving', 'Aantal', 'Eenheid', 'BTW%', 'BTW', 'pr excl BTW', 'Totaal']]
        #['Uren', f'{uren}', 'uur', f'{kosten_uren} EUR', '21%', f'{uren_btw} EUR', f'{uren_prijs_totaal} EUR']]

for item in data_json["factuur"]["producten"]:
    productnaam = item["productnaam"][:11-3] + "..."
    bedrag_excl_btw += item["prijs_per_stuk_excl_btw"]
    bedrag_btw += item["btw_per_stuk"]
    data.append(['Producten', f'{item["aantal"]}', f'{productnaam}', f'{round(100 / item["prijs_per_stuk_excl_btw"] * item["btw_per_stuk"], 2)}', f'{item["btw_per_stuk"]}', f'{item["prijs_per_stuk_excl_btw"]}', f'{round(item["aantal"] * (item["prijs_per_stuk_excl_btw"] + item["btw_per_stuk"]), 2)}'])
bedrag_btw = round(bedrag_btw, 2)
bedrag_totaal = round(bedrag_excl_btw + bedrag_btw, 2)

pdf.set_font("Arial", size=25) 
pdf.cell(30, 10, txt = "Factuur", ln = True, align = 'C')

# Set font for the title
pdf.set_font("Arial", size = 12)

# Adding logo image
pdf.image(logo_afbeelding, x=155, y=-6, w=50)  # pas x, y, en w aan volgens je behoeften

pdf.ln(10)
# Add a paragraph
pdf.cell(200, 6, txt = f"{naam}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"{factuur_adres}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"{factuur_postcode}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"{factuur_stad}", ln = True, align = 'L')

pdf.set_y(40)
pdf.cell(190, 6, txt = f"Factuur Enzo", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"+31 6123456789", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo@help.com", ln = True, align = 'R')
pdf.cell(190, 6, txt = f"factuurenzo.nl", ln = True, align = 'R')

pdf.set_y(70)
pdf.cell(200, 6, txt = f"Datum: {datum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Verval datum: {vervaldatum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"KVK nummer: {kvk_nummer}", ln = True, align = 'L')

pdf.set_y(100)
for row in data:
    for item in row:
        # Add cell with padding
        pdf.cell(27, 10, txt=item)
    pdf.ln()

# Add totals below the table with proper alignment
pdf.set_y(140)  # Aanpassen van de y-positie na de tabel
pdf.set_font("Arial", 'B',  size=12) 

right_column_width = 40  # Stel de breedte van de rechterkolom in
left_column_width = 150  # Stel de breedte van de linkerkolom in

# Bedrag exclusief BTW
pdf.cell(left_column_width, 10, txt="Bedrag excl. BTW:", align='R')
pdf.set_font("Arial", size=12) 
pdf.cell(right_column_width, 10, txt=f"{bedrag_excl_btw}", ln=True, align='R')

# BTW
pdf.set_font("Arial", 'B',  size=12) 
pdf.cell(left_column_width, 10, txt="BTW:", align='R')
pdf.set_font("Arial", size=12)
pdf.cell(right_column_width, 10, txt=f"{bedrag_btw}", ln=True, align='R')

# Totaal bedrag
pdf.set_font("Arial", 'B',  size=12) 
pdf.cell(left_column_width, 10, txt="Totaal bedrag:", align='R')
pdf.set_font("Arial", size=12)
pdf.cell(right_column_width, 10, txt=f"{bedrag_totaal}", ln=True, align='R')

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
pdf_output = "my_pdf_Felicia.pdf"
pdf.output(pdf_output)