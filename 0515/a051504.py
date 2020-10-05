import openpyxl
workbook=openpyxl.load_workbook(r'c:\tmp\aa.xlsx')
active_worksheet=workbook.active
active_worksheet.oddHeader.center.size =14
active_worksheet.oddHeader.center.text='ABC'
active_worksheet.evenHeader.center.size =14
active_worksheet.evenHeader.center.text='ABC'

active_worksheet.oddFooter.right.text='第&[Page]頁,共&N頁'
workbook.save(r'c:\tmp\bb.xlsx')