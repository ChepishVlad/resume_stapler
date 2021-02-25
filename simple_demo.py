# -*- coding: utf-8 -*-
import os

from fpdf import FPDF


class CustomPDF(FPDF):
    def header(self):
        self.image(f'{os.getcwd()}/resources/logo.jpg', w=50, x=150)

    def footer(self):
        info = dict()
        info.update({'E-mail:': 'some@awesome.mail',
                     'Phone (Moscow):': '+8 (111) 111-11-11',
                     'Phone (Saint-Petersburg):': '+8 (222) 222-25-22'})
        self.set_y(-35)
        self.set_font('Century', size=9, style='B')
        self.cell(0, 5, 'Our awesome company', ln=1)
        for key, val in info.items():
            self.set_font('Century', size=9, style='B')
            self.cell(h=5, w=30, txt=key)
            self.set_font('Century', size=9)
            self.cell(h=5, w=50, txt=val, ln=1)

        # self.cell(w=12, txt='E-mail:')
        # self.set_font('Century', size=9)
        # self.cell(w=50, txt='some@awesome.mail', ln=1)
        # self.cell(h=10, w=12, txt='Phone (Moscow):')
        # self.cell(h=10, w=50, txt='+8 (111) 111-11-11', ln=1)
        # self.cell(w=12, txt='Phone (Saint-Petersburg):')
        # self.cell(w=50, txt='+8 (222) 222-25-22', ln=1)


def generating_file():
    pdf = CustomPDF()
    pdf.add_page()
    pdf.add_font(
        'Century', '', f'{os.getcwd()}/fonts/11528.ttf', uni=True)
    pdf.add_font(
        'Century', 'B', f'{os.getcwd()}/fonts/8483.ttf', uni=True)

    fio = 'Ivanov Ivan Ivanovich'
    location = 'New York'
    citizenship = 'Russia'
    birth_date = '01.01.1970'
    email = 'some@mail.com'
    telegramm = '@some_awesome_address'

    pdf.set_font('Century', size=14, style='B')
    pdf.cell(200, 10, txt=fio, ln=1, align='L')
    pdf.output('simple_demo.pdf')


if __name__ == '__main__':
    generating_file()
