import openpyxl
workbook=openpyxl.Workbook()
active_worksheet =workbook.active
active_worksheet['A1'].value ='AA'
workbook.save(filename=r'c:\tmp\ab.xlsx')