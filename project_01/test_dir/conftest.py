from project_01.page.login_page import login_page
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import allure
import time
import os
'''读取json文件内容'''
def jsonread(path):
    with open(path, "r") as f:
        data = f.read()
    user_list = json.loads(data)
    return user_list
list_a= jsonread(path="D:\project\project_01\datafile\login")

driver = None
'''先执行when='setup' 返回setup 的执行结果
然后执行when='call' 返回call 的执行结果
最后执行when='teardown'返回teardown 的执行结果'''
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

'''全局的dirver'''
@pytest.fixture(scope="session")
def browser():
    global driver
    if driver is None:
        #注释代码为下载代码
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,'download.default_directory': 'D:\project\project_01\download'}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(chrome_options=options)
        #
        driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function", params=list_a)
def web_login(request,browser):
    libiao = request.param
    url = libiao[0]
    username = libiao[1]
    password = libiao[2]
    driver = browser
    driver.get(url)
    '''元素定位'''
    Page = login_page(driver)
    Page.search_input_username = username
    Page.search_input_password = password
    Page.search_button_login.click()
    try:
        wait = WebDriverWait(driver,3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
    except Exception:
        assert False
    else:
        assert True

