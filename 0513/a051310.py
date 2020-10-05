import openpyxl
workbook=openpyxl.load_workbook(r'c:\tmp\ab.xlsx')
active_worksheet =workbook.create_sheet(title='worksheet1')
active_worksheet['A1'].value ='ASDF'
workbook.save(filename=r'c:\tmp\ab.xlsx')