from xlrd import open_workbook
workbook=open_workbook(r'c:\tmp\elcand.xlsx')
print('worksheet.count=',workbook.nsheets)
for worksheet in workbook.sheets():
    print('worksheet name =',worksheet.name)
    print('rows =',worksheet.nrows)