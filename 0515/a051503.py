import openpyxl
workbook=openpyxl.load_workbook(r'c:\tmp\aa.xlsx')
active_worksheet=workbook.active
from openpyxl.styles.borders import Border,Side
thin_side=Side(style='thin')
thin_border= Border(left=thin_side,top=thin_side,right=thin_side,bottom=thin_side)
active_worksheet['A1'].border=thin_border
workbook.save(filename=r'c:\tmp\bb.xlsx')