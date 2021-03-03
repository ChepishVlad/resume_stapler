# -*- coding: utf-8 -*-
import os

import json
from fpdf import FPDF

from blocks import set_personal_info, set_contact_info, set_work_experience
from dicts._localization import RU


fio = 'Иванов Иннокентий Полиморфович'
location = 'г. Иваново'
citizenship = 'РФ'
birth_date = '01.01.1970'
email = 'some@mail.com'
telegramm = '@some_awesome_address'
works = {
    "work_1": {
        "date_start": "01.01.1970",
        "date_and": "01.01.1971",
        "company": "ООО Рога и Копыта",
        "position": "Java developer",
        "duties": "Писать public static void main =)"
        }
    }


class CustomPDF(FPDF):
    def header(self):
        self.image(f'{os.getcwd()}/resources/logo.jpg', w=40, x=160)

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
    pdf.set_auto_page_break(auto=True, margin=30)
    pdf.set_text_color(44, 62, 80)
    pdf.set_left_margin(15)
    pdf.add_font(
        'Century', '', f'{os.getcwd()}/fonts/11528.ttf', uni=True)
    pdf.add_font(
        'Century', 'B', f'{os.getcwd()}/fonts/8483.ttf', uni=True)

    pdf.set_font('Century', size=14, style='B')
    pdf.cell(0, 20, txt=fio, ln=1)

    # Personal information block
    set_personal_info(pdf, location, citizenship, birth_date)

    # Contact information block
    set_contact_info(pdf, email, telegramm)

    # experience
    set_work_experience(pdf, works)



    # generation pdf file
    pdf.output('simple_demo.pdf')


if __name__ == '__main__':
    generating_file()
