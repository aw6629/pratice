import openpyxl
workbook=openpyxl.load_workbook(r'c:\tmp\aa.xlsx')
active_worksheet= workbook.active
for i in range(1,5):
    active_worksheet[f'B{i}']=f'=A{i}*A{i}'
workbook.save(filename=r'c:\tmp\ac.xlsx')
