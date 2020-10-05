from selenium import webdriver
driver= webdriver.Chrome()
driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query')
id_elem=driver.find_element_by_id('pid')
id_elem.send_keys('A123456789')