js='''
        var id = document.getElementById('id');
        id.value =100;
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://localhost:5000')
driver.execute_script(js)