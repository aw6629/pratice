import openpyxl
import requests
from openpyxl import Workbook
excel_file =Workbook()
sheet=excel_file.active
i=1
while i<10:
    columnA = 'A' + str(i)
    columnB = 'B' + str(i)
    columnC = 'C' + str(i)
    columnD = 'D' + str(i)
    sheet.append([columnA,columnB,columnC,columnD])
    i=i+1
excel_file.save(r'C:\tmp\test.xlsx')


