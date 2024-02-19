from openpyxl import w
wb=load_workbook('Book1.xlsx')
ws=wb.active
print(ws)