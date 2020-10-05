import pandas as pd
import openpyxl
from openpyxl import Workbook
df =pd.read_csv(r'c:\tmp\elcand.csv',names=['c0','c1','c2','c3','c4','c5','name','c7','gender','birthYear','c10','c11','c12','c13','elected','c15'])
f=Workbook()
active_worksheet=f.active
a1=1
b1=1
for x in df['name']:
    active_worksheet[f'A{a1}']=x
    a1=a1+1
for x in df['birthYear']:
    active_worksheet[f'b{b1}']=x
    active_worksheet[f'C{b1}'] = f'=99-B{b1}'
    b1+=1
active_worksheet.oddHeader.center.size=14
active_worksheet.oddHeader.center.text='2010年村里長'
active_worksheet.evenHeader.center.size=14
active_worksheet.evenHeader.center.text='2010年村里長'
active_worksheet.oddFooter.right.text='第 &[Page]頁 共&N頁'
active_worksheet.evenFooter.right.text='第 &[Page]頁 共&N頁'
f.save(filename=r'c:\tmp\hw.xlsx')