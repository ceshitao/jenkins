from selenium import webdriver
import pytest
import json
from project_01.page.webhome_page import web_main        #主界面
'''显示等待'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import allure
class Test():
    def test_01(self):
        driver = webdriver.Chrome()
        driver.get('https://www.csdn.net/')

