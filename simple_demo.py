# -*- coding: utf-8 -*-
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=12)
pdf.cell(200, 10, txt='Welcome to hell', ln=1, align='C')
pdf.output('simple_demo.pdf')
