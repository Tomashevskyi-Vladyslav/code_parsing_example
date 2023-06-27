from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = r''#Your Link


def get_html_new(url=None):
    browser = webdriver.Chrome()
    browser.get(str(url))
    html = browser.page_source
    time.sleep(2)
    return html


html = get_html_new(url=url)
soup = BeautifulSoup(html, 'lxml')
teg = soup.find("body")
print(teg)
