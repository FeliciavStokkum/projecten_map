from fpdf import FPDF
import json
from datetime import *
import os
import shutil

pdf = FPDF()
pdf.add_page()
naam_factuur = f"2000-248.json"
input_json_pad = 'Felicia/JSON_IN/test_set_PC/'
data_json = json.load(open(f'Felicia/JSON_IN/test_set_PC/{naam_factuur}'))

# datum factuur
dag, maand, jaar = data_json["factuur"]["factuurdatum"].split('-')
dag = int(dag)
maand = int(maand)
jaar = int(jaar)
datum = datetime(jaar, maand, dag)

# klanrt factuur info/data
naam = data_json["factuur"]["klant"]["naam"]
kvk_nummer = data_json["factuur"]["klant"]["KVK-nummer"]
factuurnummer = data_json["factuur"]["factuurnummer"]
factuur_adres = data_json["factuur"]["klant"]["adres"]
factuur_postcode = data_json["factuur"]["klant"]["postcode"]
factuur_stad = data_json["factuur"]["klant"]["stad"]

# tijd
betaaltermijn_str = data_json["factuur"]["betaaltermijn"]
betaaltermijn_dagen = int(betaaltermijn_str.split('-')[0])

# bedragen berekening
# bedrag_excl_btw = 0
# bedrag_btw = 0
# bedrag_totaal = 0

y_position_verti = 110
y_pos = 110

vervaldatum = datum + timedelta(days=betaaltermijn_dagen)

# data
logo_afbeelding = 'afbeeldingen/factuur_enzo_logo.png'
data = [['Beschrijving', '  Aantal', 'Product', 'BTW%', 'BTW', 'excl BTW', 'Totaal']]

for item in data_json["factuur"]["producten"]:
    y_position_verti += 10
    y_pos += 10

    data.append(['Producten', item["aantal"], f'{item["productnaam"]}', round(100 / item["prijs_per_stuk_excl_btw"] * item["btw_per_stuk"], 2), item["btw_per_stuk"], item["prijs_per_stuk_excl_btw"], round(item["aantal"] * (item["prijs_per_stuk_excl_btw"] + item["btw_per_stuk"]), 2)])

data.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
data.append([' ', ' ', ' ', ' ', 'Bedrag excl BTW:', ' ', data_json["factuur"]["totaal_excl_btw"]])
data.append([' ', ' ', ' ', ' ', 'BTW:', ' ', data_json["factuur"]["totaal_btw"]])
data.append([' ', ' ', ' ', ' ', 'Totaal bedrag:', ' ', data_json["factuur"]["totaal_incl_btw"]])


#fonts en overal tekst
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
pdf.cell(190, 6, txt = "Factuur Enzo", ln = True, align = 'R')
pdf.cell(190, 6, txt = "+31 6123456789", ln = True, align = 'R')
pdf.cell(190, 6, txt = "factuurenzo@help.com", ln = True, align = 'R')
pdf.cell(190, 6, txt = "www.factuurenzo.nl", ln = True, align = 'R')

# haalt de 00:00:00 achter de datum weg
datum = str(datum)
vervaldatum = str(vervaldatum)
datum, y = datum.split(" ")
vervaldatum, y = vervaldatum.split(" ")

pdf.set_y(70)
pdf.cell(200, 6, txt = f"Datum: {datum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"factuurnummer: {factuurnummer}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"Verval datum: {vervaldatum}", ln = True, align = 'L')
pdf.cell(200, 6, txt = f"KVK nummer: {kvk_nummer}", ln = True, align = 'L')

# tabel
counter = 0
plaats = 'C'
pdf.set_y(100)
for row in data:
    for item in row:
        if isinstance(item, str):
            pdf.set_font("Arial", 'B',  size=12)
            if len(item) >= 14:
                if counter >= len(data_json["factuur"]["producten"]):
                    plaats = 'L'
                    pass
                else:
                    pdf.set_font("Arial", size=9)
                    counter += 1
        else:
            pdf.set_font("Arial", size=12)
            item = str(item)
        # Add cell als border wilt = border=1
        pdf.cell(27, 10, txt=item, align = plaats)
    pdf.ln()

# Add totals below the table with proper alignment
pdf.set_y(140)  # Aanpassen van de y-positie na de tabel
pdf.set_font("Arial", 'B',  size=12) 

right_column_width = 40  # Stel de breedte van de rechterkolom in
left_column_width = 150  # Stel de breedte van de linkerkolom in

#Voegt een horizontale lijn onderaan de pagina toe
pdf.set_draw_color(0, 0, 0)  
y_position = 245 # De y-coördinaat voor de lijn (iets boven de onderkant van een A4-pagina, die 297 mm hoog is)
pdf.line(10, y_position, 200, y_position)
# pdf.set_draw_color(255, 120, 214)
# pdf.line(10, 110, 200, 110)
# pdf.line(37.1, 100, 37.1, y_position_verti)
# pdf.line(115, y_pos, 185, y_pos)

# Stel de positie in net onder de getekende lijn
pdf.set_y(y_position + 5)
# Voeg tekst toe onder de lijn
pdf.set_font("Arial", 'B', 8)
pdf.cell(0, 5, 'Factuur enzo', ln=True)
pdf.set_font("Arial", size=8) 
pdf.cell(0, 5, 'Leerparkpromenade 100', ln=True) 
pdf.cell(0, 5, '3312 KW Dordrecht', ln=True)
pdf.cell(0, 5, 'BTW nummer: NL 111234567B01', ln=True)
pdf.cell(0, 5, 'KVK nummer: 9305 6589', ln=True)

pdf.set_y(y_position + 5) 
pdf.set_font("Arial", 'B', 8)
pdf.cell(0, 5, 'Contact informatie', ln=True, align='C')
pdf.set_font("Arial", size=8) 
pdf.cell(0, 5, 'contactpersonen: Felicia Van Stokum en Bent Bon', ln=True, align='C') 
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

output_json_pad = "Felicia/INVOICE/"

json_output_path = os.path.join(output_json_pad, f"JSON_factuur: {naam_factuur}.json")
with open(os.path.join(output_json_pad, naam_factuur), 'w') as json_file:
    json.dump(data_json, json_file, indent=4)

if not os.path.exists(output_json_pad):
    os.makedirs(output_json_pad)

pdf_output_pad = "Felicia/INVOICE/"
if not os.path.exists(pdf_output_pad):
    os.makedirs(pdf_output_pad)
pdf.output(os.path.join(pdf_output_pad, naam_factuur.replace('.json', '.pdf')))

verwerkingsmap = "Felicia/JSON_PROCESSED"
if not os.path.exists(verwerkingsmap):
    os.makedirs(verwerkingsmap)
    shutil.move(os.path.join(input_json_pad, naam_factuur), os.path.join(verwerkingsmap, naam_factuur))

#Hier staan de JSON documenten
json_pad = "C:/School/Code/projecten_map/Felicia/JSON_IN/test_set_PC"

#Hier gaan de JSON documenten heen
verwerkingsmap = "C:/School/Code/projecten_map/Felicia/JSON_PROCESSED"

#naam van het bestand
json_bestand = f"{naam_factuur}"

#hier wordt het bestand toegevoegd aan het pad
json_volledig_pad = os.path.join(json_pad, json_bestand)

#Lees het JSON bestand
with open(json_volledig_pad, 'r') as file:
    data = json.load(file)

#verplaats het gemaakte factuur naar de map invoice
doelmap = "C:/School/Code/projecten_map/Felicia/INVOICE"
if not os.path.exists(doelmap):
    os.makedirs(doelmap)
volledig_pad = os.path.join(doelmap, naam_factuur)

#Verplaats het bestand naar de map PROCESSED
shutil.move(f"Felicia/JSON_IN/test_set_PC/{naam_factuur}", f"Felicia/JSON_PROCESSED/{naam_factuur}")

#Hier wordt de pdf aangemaakt en naar de map invoice verplaatst
pdf.output(f"Felicia/INVOICE/{naam_factuur.replace('.json', '.pdf')}")