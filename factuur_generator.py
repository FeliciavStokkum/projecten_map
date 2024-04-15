from fpdf import FPDF
from tkinter import *

def create_pdf(input_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=input_text, ln=True, align='C')
    pdf.output("MyPDF2.pdf")
    label_result.config(text="PDF gegenereerd met de tekst: " + input_text)

def get_input():
    user_input = entry.get()
    create_pdf(user_input)

# Maak het hoofdvenster
root = Tk()
root.title("PDF Generator")

# Voeg een label toe
label = Label(root, text="Voer tekst in voor het PDF-document:")
label.pack(pady=10)

# Voeg een tekstveld toe
entry = Entry(root, width=50)
entry.pack(pady=10)

# Voeg een knop toe
button = Button(root, text="Genereer PDF", command=get_input)
button.pack(pady=20)

# Voeg een resultaat label toe
label_result = Label(root, text="")
label_result.pack(pady=10)

# Start de GUI
root.mainloop()0