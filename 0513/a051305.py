from xlrd import open_workbook
workbook=open_workbook(r'c:\tmp\elcand.xlsx')
worksheet =workbook.sheet_by_name('123a')
print(worksheet.cell(1,6))
print(type(worksheet.cell(1,6)))