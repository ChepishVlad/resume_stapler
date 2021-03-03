# -*- coding: utf-8 -*-
import os
from fpdf import FPDF


fio = 'Иванов Иннокентий Полиморфович'
location = 'г. Иваново'
citizenship = 'РФ'
birth_date = '01.01.1970'
email = 'some@mail.com'
telegramm = '@some_awesome_address'
works = {
    'work_1': {
        'date_start': '01.01.1970',
        'date_and': '01.01.1971',
        'company': 'ООО Рога и Копыта',
        'position': 'Java developer',
        'duties': 'Писать public static void main =)'
        },
    'work_2': {
        'date_start': 'январь 1980',
        'date_and': 'январь 1981',
        'company': 'ООО Рога',
        'position': 'Java',
        'duties': 'Lorem Ipsum - это текст-"рыба", часто используемый в печати'
                  ' и вэб-дизайне. Lorem Ipsum является стандартной "рыбой"'
                  ' для текстов на латинице с начала XVI века. В то время'
                  ' некий безымянный печатник создал большую коллекцию'
                  ' размеров и форм шрифтов, используя Lorem Ipsum для'
                  ' распечатки'
        },
    'work_3': {
        'date_start': 'январь 1980',
        'date_and': 'по настоящий момент',
        'company': 'Неебически длинное название типа нии-хуи технологии '
                   'трах бам бумс комерц',
        'position': 'Java',
        'duties': 'Lorem Ipsum - это текст-"рыба", часто используемый в печати'
                  ' и вэб-дизайне. Lorem Ipsum является стандартной "рыбой"'
                  ' для текстов на латинице с начала XVI века. В то время'
                  ' некий безымянный печатник создал большую коллекцию'
                  ' размеров и форм шрифтов, используя Lorem Ipsum для'
                  ' распечатки'
        },
    'work_4': {
        'date_start': 'январь 1980',
        'date_and': 'по настоящий момент',
        'company': 'Неебически длинное название типа нии-хуи технологии '
                   'трах бам бумс комерц',
        'position': 'Java',
        'duties': '- add some info \n'
                  '- correct some info\n'
                  '- add some info\n'
                  '- correct some info'}
    }
education = {
    'ed_1': {
        'years': '2014 - 2016',
        'name': 'Институт системного программирования Российской академии '
                'Аспирант, Прикладная математика',
        'grade': 'Аспирант, Прикладная математика'
        },
    'ed_2': {
        'years': '2014 - 2016',
        'name': 'Институт системного программирования Российской академии '
                'Аспирант, Прикладная математика',
        'grade': 'Аспирант, Прикладная математика'
        }
    }


class CustomPDF(FPDF):
    def header(self):
        self.image(f'{os.getcwd()}/resources/logo.jpg', w=40, x=160)

    def footer(self):
        self.set_y(-28)
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

    def set_personal_info(self,
                          _location: str,
                          _citizenship: str,
                          _birth_date: str = ''):
        self.set_font('Century', size=12, style='B')
        self.cell(0, 8, txt='Персональная информация', ln=1)
        self.set_font('Century', size=11)
        self.cell(0, 8, txt=f'Локация: {_location}', ln=1)
        self.cell(0, 8, txt=f'Гражданство: {_citizenship}', ln=1)
        if _birth_date:
            self.cell(0, 8, txt=f'Дата рождения: {_birth_date}', ln=1)
        self.cell(0, 8, txt='', ln=1)

    def set_contact_info(self,
                         _email: str,
                         _telegram: str = '',
                         _github: str = ''):
        self.set_font('Century', size=12, style='B')
        self.cell(0, 8, txt='Контактная информация', border='B', ln=1)
        self.ln(3)
        self.set_font('Century', size=11)
        self.cell(0, 8, txt=f'e-mail: {_email}', ln=1)
        if _telegram:
            self.cell(0, 8, txt=f'telegram: {_telegram}', ln=1)
        if _github:
            self.cell(0, 8, txt=f'github: {_github}', ln=1)
        self.cell(0, 8, txt='', ln=1)

    def set_work_experience(self, _works: dict):
        self.set_font('Century', size=12, style='B')
        self.cell(0, 8, txt="Опыт работы", border='B', ln=1)
        self.ln(3)
        for key in _works:
            place = _works[key]
            self.ln(3)

            col_width = self.w / 4.5
            self.set_font('Century', size=11)
            data = [
                [f'{place["date_start"]} - {place["date_and"]}', place['company']],
                ['', place['position']],
                ['', place['duties']],
                ]
            self.multi_cell(
                col_width, 8, txt=data[0][0], border=0, ln=3, align='L')
            self.multi_cell(
                col_width * 2.8, 8, txt=data[0][1], border=0, align='L')
            self.ln(0)
            self.set_font('Century', size=11, style='B')
            self.multi_cell(
                col_width, 8, txt=data[1][0], border=0, ln=3, align='L')
            self.multi_cell(
                col_width * 2.8, 8, txt=data[1][1], border=0, align='L')
            self.ln(0)
            self.set_font('Century', size=11)
            self.multi_cell(
                col_width, 8, txt=data[2][0], border=0, ln=3, align='L')
            self.multi_cell(
                col_width * 2.8, 8, txt=data[2][1], border=0, align='L')
            self.ln(0)

    def set_education(self, _education: dict):
        self.set_font('Century', size=12, style='B')
        self.cell(0, 8, txt="Образование", border='B', ln=1)
        self.ln(3)


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
    pdf.set_personal_info(
        _location=location, _citizenship=citizenship, _birth_date=birth_date)

    # Contact information block
    pdf.set_contact_info(
        _email=email, _telegram=telegramm)

    # experience
    pdf.set_work_experience(_works=works)



    # generation pdf file
    pdf.output('simple_demo.pdf')


if __name__ == '__main__':
    generating_file()
