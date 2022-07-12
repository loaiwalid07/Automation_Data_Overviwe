from fpdf import FPDF ,HTMLMixin
import pandas as pd

df = pd.read_csv("Stores.csv")
class PDF(FPDF,HTMLMixin):
    def header(self):
        # Logo
        self.image('logo_pb.png', 8, 5, 28)
        # Arial bold 15
        self.set_font('Arial', 'B', 18)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Data Overviwe Report', 0, 1, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
for i in range(1, 41):
    pdf.cell(5, 10, 'Printing line number ' + str(i), 0, 1)
    if i == 10:
        pdf.set_font('Arial', '', 12)
        # Background color
        pdf.set_fill_color(200, 220, 255)
        #Title
        pdf.cell(0, 6, 'Chapter %d'%(i), 0, 1, 'L', 1)
        # Line break
        pdf.ln(1)
pdf.write(df)
pdf.image('logo_pb.png',w=200)

pdf.output('Report.pdf', 'F')

