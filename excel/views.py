from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import xlwt

from excel.models import Company_details


def export_data(request):
    response = HttpResponse(content_type='excel/template.html')
    response['Content-Disposition'] = 'attachment; filename="sheets/company_details.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Company_details')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Company_name', 'CTC', 'Date_of_visit', 'Eligibility', 'Branch']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)


    font_style = xlwt.XFStyle()

    rows = Company_details.objects.all().values_list('Company_name', 'CTC', 'Date_of_visit', 'Eligibility', 'Branch')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response