import openpyxl
workbook=openpyxl.load_workbook(r'c:\tmp\aa.xlsx')
active_worksheet=workbook.active
active_worksheet['A4'].number_format='#,###'
import datetime
active_worksheet['A5']=datetime.datetime.now()
active_worksheet['A5'].number_format='yyyy/mm/dd hh:mm:ss'
workbook.save(filename=r'c:\tmp\bb.xlsx')