from fpdf import FPDF
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import io


# Assume this function generates and saves a QR code
def generate_qr_code(data, filename="qr_code.png"):
    import qrcode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

# Variables (just examples)
data = "Sample Data for QR"
generate_qr_code(data)

# Create instance of FPDF class and build your PDF (simplified)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Sample Invoice", ln=1, align='C')
pdf.cell(200, 10, "Sample Item", ln=1)
pdf.output("my_pdf_document.pdf")

# Read the newly created PDF
reader = PdfReader("my_pdf_document.pdf")
writer = PdfWriter()

# Load the QR code image
qr_image = Image.open("qr_code.png")

# Loop through all the pages and add the QR code to each page
for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    # Convert PyPDF2 page to a PIL Image (This requires additional setup; not directly possible as written)
    # Using a placeholder operation here
    pdf_page_image = Image.new('RGB', (210, 297), 'white')  # Assuming A4 size, convert dimensions appropriately
    pdf_page_image.paste(qr_image, (0, 0))  # Adjust position as needed

    # Save the modified page back to a new PDF
    pdf_bytes = io.BytesIO()
    pdf_page_image.save(pdf_bytes, format='0')
    pdf_bytes.seek(0)
    modified_page = PdfReader(pdf_bytes).pages[0]
    writer.add_page(modified_page)

# Save the output PDF
with open("output_with_qr.pdf", "wb") as f_out:
    writer.write(f_out)
