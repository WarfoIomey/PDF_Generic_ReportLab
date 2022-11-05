from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


pdfmetrics.registerFont(TTFont('Astra', 'PT-Astra-Serif_Regular.ttf'))
pdfmetrics.registerFont(TTFont('Astra-bold', 'PT-Astra-Serif_Bold.ttf'))


my_path = 'test_python.pdf'
width, height = A4
c = canvas.Canvas(my_path, pagesize=A4)

line1 = ('Наименование', 'Расходы', 'Выручка')
line2 = ('ИАТ', '10000', '100000')
line3 = ('ИРКАТ', '20000', '100000')
line4 = ('УРФУ', '25000', '500000')

elements = []
data = [line1, line2, line3, line4]

t = Table(data, colWidths=100, rowHeights=20)
t.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (1, -1), colors.black),
                       ('GRID', (0, 1), (-1, -1), 2, colors.black),
                       ('FONTNAME', (0, 1), (-1, -1), 'Astra'),
                       ('FONTNAME', (0, 0), (3, 0), 'Astra-bold')]))


my_Style_one = ParagraphStyle('My style 1',
                              fontName='Astra',
                              fontSize=14,
                              alignment=0)
my_Style_two = ParagraphStyle('My style 2',
                              fontName='Astra-bold',
                              fontSize=14,
                              alignment=1)
my_Style_three = ParagraphStyle('My style 3',
                                fontName='Astra',
                                fontSize=30,
                                aligment=1,
                                alpha=1)

p1 = Paragraph('<b>Hello</b>', my_Style_two)
p2 = Paragraph('Welcome to our online classes. We are learn python.'
               'We are creating PDF by using ReportLab. На данный '
               'я использую русский язык, чтобы проверить шрифт.',
               my_Style_one)

p1.wrapOn(c, 450, 50)
p1.drawOn(c, width - 500, height - 100)

p2.wrapOn(c, 450, 50)
p2.drawOn(c, width - 500, height - 150)

t.wrapOn(c, width, height)
t.drawOn(c, 150, 600)

c.rotate(45)
c.setFont('Astra', 100)
c.drawString(400, 150, 'Confidential')
c.save()
