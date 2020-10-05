from xlwt import Workbook
workbook=Workbook()
worksheet =workbook.add_sheet('Test')
worksheet.write(0,0,'AA')
workbook.save(r'c:\tmp\aa.xls')