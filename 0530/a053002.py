import  requests
import time
start= time.time()
r=requests.get('https://www.cns11643.gov.tw/wordView.jsp',params={'SN':'王'})
print(r.text)
print(time.time()-start)