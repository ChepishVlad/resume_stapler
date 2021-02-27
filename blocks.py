# -*- coding: utf-8 -*-
from fpdf import FPDF


def set_personal_info(pdf: FPDF,
                      location: str,
                      citizenship: str,
                      birth_date: str = '',
                      language: str = 'ru'):
    """
    :param pdf: required parameter
    :param location: required parameter
    :param citizenship: required parameter
    :param birth_date: not required parameter
    :param language: by default got value = 'ru'
    :return: pdf
    """
    block_name = {
        'ru': 'Персональная информация',
        'en': 'Personal information'
        }
    pdf.set_font('Century', size=12, style='B')
    pdf.cell(0, 8, txt=block_name[language], ln=1)
    pdf.set_font('Century', size=11)
    pdf.cell(0, 8, txt=f'Локация: {location}', ln=1)
    pdf.cell(0, 8, txt=f'Гражданство: {citizenship}', ln=1)
    if birth_date:
        pdf.cell(0, 8, txt=f'Дата рождения: {birth_date}', ln=1)
    pdf.cell(0, 8, txt='', ln=1)


def set_contact_info(pdf: FPDF,
                     email: str,
                     telegram: str = '',
                     github: str = '',
                     language: str = 'ru'):
    block_name = {
        'ru': 'Контактная информация',
        'en': 'Contact information'
        }
    pdf.set_font('Century', size=12, style='B')
    pdf.cell(0, 8, txt=block_name[language], ln=1)
    pdf.set_font('Century', size=11)
    pdf.cell(0, 8, txt=f'e-mail: {email}', ln=1)
    if telegram:
        pdf.cell(0, 8, txt=f'telegram: {telegram}', ln=1)
    if github:
        pdf.cell(0, 8, txt=f'github: {github}', ln=1)
    pdf.cell(0, 8, txt='', ln=1)


def set_work_experience(pdf: FPDF):
    pass


def set_education():
    pass
