from xlwt import Workbook
workbook=Workbook()
worksheet =workbook.add_sheet('Test')
worksheet.write(0,0,1)
worksheet.write(1,0,1)
from xlwt import Formula
worksheet.write (2,0,Formula('SUM(A1:A2)'))
workbook.save(r'c:\tmp\aa.xls')