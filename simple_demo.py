# -*- coding: utf-8 -*-
import os

from fpdf import FPDF

from blocks import set_personal_info, set_contact_info


class CustomPDF(FPDF):
    def header(self):
        self.image(f'{os.getcwd()}/resources/logo.jpg', w=50, x=150)

    def footer(self):
        self.set_y(-30)
        self.set_font('Century', size=9, style='B')
        self.set_text_color(80, 80, 80)
        self.cell(0, 7, 'Our awesome company', ln=1)
        self.cell(w=12, txt='E-mail:')
        self.set_font('Century', size=9)
        self.cell(w=50, txt='some@awesome.mail', ln=1)
        self.set_font('Century', size=9, style='B')
        self.cell(h=7, w=28, txt='Phone (Moscow):')
        self.set_font('Century', size=9)
        self.cell(h=7, w=30, txt='+8 (111) 111-11-11', ln=1)
        self.set_font('Century', size=9, style='B')
        self.cell(w=40, txt='Phone (Saint-Petersburg):')
        self.set_font('Century', size=9)
        self.cell(w=30, txt='+8 (222) 222-25-22', ln=1)


def generating_file():
    pdf = CustomPDF()
    pdf.add_page()
    pdf.set_margins(30, 50, -1)
    pdf.add_font(
        'Century', '', f'{os.getcwd()}/fonts/11528.ttf', uni=True)
    pdf.add_font(
        'Century', 'B', f'{os.getcwd()}/fonts/8483.ttf', uni=True)

    fio = 'Иванов Иннокентий Полиморфович'
    location = 'г. Иваново'
    citizenship = 'РФ'
    birth_date = '01.01.1970'
    email = 'some@mail.com'
    telegramm = '@some_awesome_address'

    pdf.set_font('Century', size=14, style='B')
    pdf.cell(0, 10, txt=fio, ln=1)

    # Personal information block
    set_personal_info(pdf, location, citizenship, birth_date)

    # Contact information block
    set_contact_info(pdf, email, telegramm)


    # generation pdf file
    pdf.output('simple_demo.pdf')


if __name__ == '__main__':
    generating_file()
