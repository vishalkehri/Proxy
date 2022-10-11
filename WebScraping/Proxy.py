from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Users/19053/chromedriver.exe')

urlTest = 'https://httpbin.org/ip'

urlProxy = 'https://free-proxy-list.net/'

driver.get(urlProxy)

from selenium.webdriver.common.by import By

driver.get('https://free-proxy-list.net/')

content = driver.page_source
products = []

soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'table-responsive'}):
    ip=a.find('td')

    products.append(ip.text)

df = pd.DataFrame({'Proxy':products}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
