# -*- coding: utf-8 -*-
import time
import os
import sys
import urllib
import urllib.request
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
import requests
from PIL import Image
from bs4 import BeautifulSoup

def clear_string(string):  # В основном только для того, что удать знак "рубль" из строки "цена"
    return re.sub(r'\D', '', string)


class StartMonitoring():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=499,800")
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--log-level=3')
        #chrome_options.add_argument("--start-maximized")
        prefs = {"profile.managed_default_content_settings.images": 2}
        #chrome_options.add_experimental_option("prefs", prefs)
        self.login_url = 'https://5kings.ru/'
        self.driver = webdriver.Chrome(options=chrome_options,
                                       executable_path=os.getcwd() + './chromedriver')
        
        self.URL = 'https://kwork.ru/projects?c=41'


    def main(self):
        keyword = ['Бот', 'Бота', 'Боты' 'Автоматизация', 
                    'Авторегистрация', 'Телеграм', 'Telegram','Парсинг', 
                    'Спарсить', 'Скрипт', 'Чекер', 'API','Просмотров', 'Накрутка']
        self.driver.get(self.URL)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        orders = soup.find('div', {'id': 'app'})
        cd = []
        data = []
        for child in orders:
            orders_block = child.find_all("div", {"class": "card__content"})
            for tag in orders_block:
                title = tag.find('a').text
                price = clear_string(tag.find("div", {"class": "wants-card__header-price"}).text)
                data.append({'Название заказа:':title, 'Цена заказчика:': price})
                #wants-card__header-price - PRICE
        self.driver.close()
        print(data)
if __name__ == "__main__":
    st = StartMonitoring()
    st.main()  
        
        