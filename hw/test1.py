import requests
import re
import openpyxl
import time
datadaylist=[20160101,20160201,20160301,20160401,20160501,20160601,20160701,20160801,20160901,20161001,20161101,20161201,20170101,20170201,20170301,20170401,20170501,20170601,20170701,20170801,20170901,20171001,20171101,20171201,20180101,20180201,20180301,20180401,20180501,20180601,20180701,20180801,20180901,20181001,20181101,20181201]
workbook=openpyxl.Workbook()
for idx,x in enumerate(datadaylist):
    if idx >=1:
        workbook.create_sheet(str(x))
    else:
        workbook.active.title = str(x)
    data_sheet = workbook.worksheets[idx]
    r=requests.post(f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={x}&stockNo=2330')
    data = r'<td>(.*?)</td>'
    m_td = re.findall(data,r.text,re.S|re.M)
    for i in range(0,len(m_td),9):
        col=m_td[i:i+9]
        data_sheet.append(col)
    time.sleep(5)
workbook.save(r'c:\tmp\test1.xlsx')


