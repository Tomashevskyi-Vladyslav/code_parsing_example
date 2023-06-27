from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = r' https://tomashevskyi-vladyslav.github.io/For_lovely_mom/'


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