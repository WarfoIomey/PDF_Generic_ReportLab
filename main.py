from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.units import mm
from copy import deepcopy




pdfmetrics.registerFont(TTFont('Astra', 'PT-Astra-Serif_Regular.ttf'))
pdfmetrics.registerFont(TTFont('Astra-bold', 'PT-Astra-Serif_Bold.ttf'))


def main():

    doc = SimpleDocTemplate("test_python.pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18
                            )
    styleSheet = getSampleStyleSheet()
    style = styleSheet["Normal"]
    style.fontName = "Astra"
    style.fontSize = 12
    # расстояние между строк
    style.leading = 12
    style.spaceAfter = 0 * mm
    style.alignment = TA_JUSTIFY
    # отступ
    style.firstLineIndent = 15
    styleRight = deepcopy(style)
    styleRight.fontSize = 12
    styleRight.leading = 12
    styleRight.spaceAfter = 0 * mm
    styleRight.alignment = TA_RIGHT
    styleRight.firstLineIndent = 0

    styleBold = deepcopy(style)
    styleBold.fontName = "Astra-bold"

    styleCenterBold = deepcopy(styleBold)
    styleCenterBold.alignment = TA_CENTER
    styleCenterBold.fontSize = 12
    styleCenterBold.leading = 15



    flowables = []
    pks_19_2 = "ПКС-19-2"
    PKS_19_1 = "ПКС-19-1"
    name1 = "Иванов Иван Иванович"
    reason1 = "проспал"
    reason2 = "заболел"
    reason3 = "по семейным обстоятельствам"

    str1 = "Директору ГБПОУ \"ИАТ\"" + "<br/>" + "Якубовскому А.Н." + "<br/>" + "От студента группы {}" + "<br/>" + "{}"
    p1 = Paragraph(str1.format(pks_19_2, name1), styleRight)
    flowables.append(p1)

    str2 = "<br/>" + "<br/>" + "<br/>" + "<br/>" + "Объяснительная"
    p2 = Paragraph(str2, styleCenterBold)
    flowables.append(p2)

    str3 = "<br/>"+"<br/>" + "Я не пришел на пары по причине {} "
    p3 = Paragraph(str3.format(reason3), style)
    flowables.append(p3)
    doc.build(flowables, onFirstPage=first_page)


def first_page(canvas, document):
    # c = canvas.Canvas("test_python.pdf")
    # title.setFont("Astra-bold", 12)
    # title.drawString(250, 600, "Объяснительная")
    canvas.saveState()
    canvas.setFont("Astra", 12)
    canvas.drawString(160 * mm, 10 * mm, 'Подпись ___________')
    canvas.drawString(40 * mm, 10 * mm, 'Дата ___________')
    canvas.restoreState()

    # def first_page(canvases, document):
    #     canvases = canvas.Canvas(document)
    #     canvases.setFont("Astra-bold", 12)
    #     canvases.drawString(250, 600, "Объяснительная")
    #     canvases.setFont("Astra", 12)
    #     canvases.drawString(160 * mm, 10 * mm, 'Подпись ___________')
    #     canvases.drawString(40 * mm, 10 * mm, 'Дата ___________')
    #     canvases.showPage()
    #     canvases.save()

    # create_document(name_document)
    # first_page(title, name_document)


if __name__ == '__main__':
    main()
    # create_document("test_python.pdf")
    # first_page("title", "test_python.pdf")


# my_path = 'test_python.pdf'
# width, height = A4
# c = canvas.Canvas(my_path, pagesize=A4)
#
# line1 = ('Наименование', 'Расходы', 'Выручка')
# line2 = ('ИАТ', '10000', '100000')
# line3 = ('ИРКАТ', '20000', '100000')
# line4 = ('УРФУ', '25000', '500000')
#
# elements = []
# data = [line1, line2, line3, line4]
#
# t = Table(data, colWidths=100, rowHeights=20)
# t.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (1, -1), colors.black),
#                        ('GRID', (0, 1), (-1, -1), 2, colors.black),
#                        ('FONTNAME', (0, 1), (-1, -1), 'Astra'),
#                        ('FONTNAME', (0, 0), (3, 0), 'Astra-bold')]))
#
#
# my_Style_one = ParagraphStyle('My style 1',
#                               fontName='Astra',
#                               fontSize=14,
#                               alignment=0)
# my_Style_two = ParagraphStyle('My style 2',
#                               fontName='Astra-bold',
#                               fontSize=14,
#                               alignment=1)
# my_Style_three = ParagraphStyle('My style 3',
#                                 fontName='Astra',
#                                 fontSize=30,
#                                 aligment=1,
#                                 alpha=1)
#
# p1 = Paragraph('<b>Hello</b>', my_Style_two)
# p2 = Paragraph('Welcome to our online classes. We are learn python.'
#                'We are creating PDF by using ReportLab. На данный '
#                'я использую русский язык, чтобы проверить шрифт.',
#                my_Style_one)
#
# p1.wrapOn(c, 450, 50)
# p1.drawOn(c, width - 500, height - 100)
#
# p2.wrapOn(c, 450, 50)
# p2.drawOn(c, width - 500, height - 150)
#
# t.wrapOn(c, width, height)
# t.drawOn(c, 150, 600)
#
# c.rotate(45)
# c.setFont('Astra', 100)
# c.drawString(400, 150, 'Confidential')
# c.save()
