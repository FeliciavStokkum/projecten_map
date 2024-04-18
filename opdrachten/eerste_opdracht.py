from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=25) 

tekst = input("wat wil je in je pdf?: ")

pdf.cell(200, 6, f"{tekst}", ln = True, align = 'L')

pdf.output("eerste_opdracht.pdf")