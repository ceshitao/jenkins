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
#正则
'''新增'''
class Test_new_add():
    @allure.title("用例标题0")
    @allure.story("这里是第一个二级标签")
    def test_new_add(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_button_sea_add.click()
        '''种类下拉框'''
        Page.search_button_kinds_list.click()
        #显示等待
        wait = WebDriverWait(self.driver,3,poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[last()]/div[1]/div[1]/ul/li[1]")))
        Page.search_button_request.click()
        '''来源下拉框'''
        Page.search_button_source_list.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[last()]/div[1]/div[1]/ul/li[1]")))
        Page.search_button_client.click()
        '''来源信息'''
        Page.search_text_Source_information.send_keys("来源信息啊")
        '''联系人'''
        Page.search_text_Contact_linkman.send_keys("张博啊")
        '''联系人电话'''
        Page.search_text_Contact_phone.send_keys("1234567890")
        '''等级先择'''
        Page.search_text_four.click()
        '''上报人'''
        Page.search_button_reporter_list.click()
        Page.search_button_reporter.click()
        '''上报人电话'''
        Page.search_text_reporter_phone.clear()
        Page.search_text_reporter_phone.send_keys("1234567890")
        '''负责跟踪人'''
        Page.search_button_follower_list.click()
        Page.search_button_follower.click()
        '''负责人电话'''
        Page.search_text_Responsible_phone.clear()
        Page.search_text_Responsible_phone.send_keys("1234567890")
        '''主题简介'''
        Page.search_text_Topic_introduction.send_keys("主题简介啊")
        '''备注'''
        Page.search_text_Remark.send_keys("备注啊")
        '''详情内容'''
        Page.search_text_send.send_keys("ceshi")
        Page.search_text_upload_texts.send_keys(r'C:\Users\root\Desktop\包装相关指令整理.docx')
        Page.search_text_upload_images.send_keys(r'C:\Users\root\Desktop\包装相关指令整理.docx')
        Page.search_text_upload_images.send_keys(r'C:\Users\root\Desktop\309807.jpg')
        '''保存'''
        Page.search_button_save.click()
        Page.search_Navigation_bar_all_num.click()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

'''导航栏的页码匹配'''
class Test_Navigation_bar_num():
    @allure.title("用例标题2")
    @allure.story("这里是第一个二级标签")
    def test_incomplete_num(self, web_login, browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_incomplete_num.click()
        Navigation_bar_incomplete_num = re.findall('\\d+',Page.search_Navigation_bar_incomplete_num.text)
        time.sleep(2)
        Navigation_bar_last_num = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        serial_number_num = re.findall('\\d+', Page.search_serial_number_num.text)
        assert Navigation_bar_incomplete_num == Navigation_bar_last_num == serial_number_num

    def test_request_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_request_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_request_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        time.sleep(1)
        # wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[last()]/td[1]/div/span')))
        Page.search_pagenumber_num.click()
        time.sleep(2)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)
        assert num == num1 == num2

    def test_consultation_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_consultation_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_consultation_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)
        assert num == num1 == num2

    def test_suggestion_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_suggestion_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_suggestion_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)
        assert num == num1 == num2

    def test_complaint_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_complaint_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_complaint_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)
        assert num == num1 == num2

    def test_feedback_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_feedback_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_feedback_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)
        assert num == num1 == num2

    def test_initiated_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_initiated_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_initiated_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)
        assert num == num1 == num2

    def test_all_num(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_all_num.click()
        num = re.findall('\\d+',Page.search_Navigation_bar_all_num.text)
        time.sleep(2)
        num1 = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(2)
        num2 = re.findall('\\d+', Page.search_serial_number_num.text)

        assert num == num1 == num2

'''搜索'''
class Test_search():
    '''[['HNB','','','','']] 搜索的内容'''
    @pytest.mark.parametrize('Servicenum,Topic_introduction,informant,Responsible_tracker,Source_information',
            [['HNB','','','','']])
    def test_incomplete_search(self,web_login,browser,Servicenum,Topic_introduction,informant,Responsible_tracker,Source_information):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys(Servicenum)
        Page.search_Iputbox_Topic_introduction.send_keys(Topic_introduction)
        Page.search_Iputbox_informant.send_keys(informant)
        Page.search_Iputbox_Responsible_tracker.send_keys(Responsible_tracker)
        Page.search_Iputbox_Source_information.send_keys(Source_information)
        Page.search_button_sea_query.click()

        wait = WebDriverWait(self.driver, 3, poll_frequency=1)
        wait.until(EC.presence_of_element_located((By.ID,'tab-未完成')))
        Navigation_bar_incomplete_num = re.findall('\\d+', Page.search_Navigation_bar_incomplete_num.text)
        Navigation_bar_last_num = re.findall('\\d+', Page.search_Navigation_bar_last_num.text)
        wait = WebDriverWait(self.driver, 3, poll_frequency=1)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
        Page.search_pagenumber_num.click()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 3, poll_frequency=1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[last()]/td[1]/div/span')))
        serial_number_num = re.findall('\\d+', Page.search_serial_number_num.text)
        assert Navigation_bar_incomplete_num == Navigation_bar_last_num == serial_number_num


        number = int(Navigation_bar_last_num[0])
        page_num = int(number/50) + 1
        if page_num >= 2:
            for i in range(1,page_num):
                time.sleep(0.2)
                wait = WebDriverWait(self.driver, 3, poll_frequency=1)
                wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
                self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[' + str(i) + ']').click()
                for number1 in range(1,51):
                    '''5个查询的匹配条件  业务编号 主题简介 上报人 负责跟踪人 来源信息  流程状态'''
                    time.sleep(0.2)
                    search_Servicenum = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number1) + ']/td[8]/div').text
                    search_Topic_introduction = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number1) + ']/td[4]/div').text
                    search_informant = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number1) + ']/td[6]/div').text
                    search_Responsible_tracker = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number1) + ']/td[7]/div').text
                    time.sleep(0.2)
                    self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number1) + ']/td[8]/div').click()
                    source_information = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div/table/tbody[2]/tr/td[2]/pre').text
                    '''流程状态'''
                    search_Process_status = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number1) + ']/td[9]/div/div/span').text
                    assert search_Process_status != "已完成"
                    assert search_Servicenum == Servicenum or Servicenum in search_Servicenum
                    assert search_Topic_introduction == Topic_introduction or Topic_introduction in search_Topic_introduction
                    assert search_informant == informant or informant in search_informant
                    assert search_Responsible_tracker == Responsible_tracker or Responsible_tracker in search_Responsible_tracker
                    assert source_information == Source_information or Source_information in source_information
            wait = WebDriverWait(self.driver, 3, poll_frequency=1)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
            self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[' + str(page_num) + ']').click()
            for number2 in range (1,(number-(page_num-1)*50)+1):
                    '''5个查询的匹配条件  业务编号 主题简介 上报人 负责跟踪人 来源信息  流程状态'''
                    wait = WebDriverWait(self.driver, 3, poll_frequency=1)
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[last()]/td[2]/div')))
                    time.sleep(0.2)
                    search_Servicenum = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number2) + ']/td[8]/div').text
                    search_Topic_introduction = self.driver.find_element(By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number2) + ']/td[4]/div').text
                    search_informant = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number2) + ']/td[6]/div').text
                    search_Responsible_tracker = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number2) + ']/td[7]/div').text
                    time.sleep(0.2)
                    self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number2) + ']/td[8]/div').click()
                    source_information = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div/table/tbody[2]/tr/td[2]/pre').text
                    '''流程状态'''
                    search_Process_status = self.driver.find_element(By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(number2) + ']/td[9]/div/div/span').text
                    assert search_Process_status != "已完成"
                    assert search_Servicenum == Servicenum or Servicenum in search_Servicenum
                    assert search_Topic_introduction == Topic_introduction or Topic_introduction in search_Topic_introduction
                    assert search_informant == informant or informant in search_informant
                    assert search_Responsible_tracker == Responsible_tracker or Responsible_tracker in search_Responsible_tracker
                    assert source_information == Source_information or Source_information in source_information
        else:
            wait = WebDriverWait(self.driver, 3, poll_frequency=1)
            wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]')))
            self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[' + str(page_num) + ']').click()
            for i in range (1,number+1):
                    '''5个查询的匹配条件  业务编号 主题简介 上报人 负责跟踪人 来源信息  流程状态'''
                    wait = WebDriverWait(self.driver, 3, poll_frequency=1)
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[last()]/td[2]/div')))
                    time.sleep(0.2)
                    search_Servicenum = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[8]/div').text
                    search_Topic_introduction = self.driver.find_element(By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[4]/div').text
                    search_informant = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[6]/div').text
                    search_Responsible_tracker = self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[7]/div').text
                    wait = WebDriverWait(self.driver, 3, poll_frequency=1)
                    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/div')))
                    time.sleep(0.2)
                    self.driver.find_element(By.XPATH,'//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[8]/div').click()
                    source_information = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div/table/tbody[2]/tr/td[2]/pre').text
                    '''流程状态'''
                    search_Process_status = self.driver.find_element(By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[9]/div/div/span').text
                    assert search_Process_status != "已完成"
                    assert search_Servicenum == Servicenum or Servicenum in search_Servicenum
                    assert search_Topic_introduction == Topic_introduction or Topic_introduction in search_Topic_introduction
                    assert search_informant == informant or informant in search_informant
                    assert search_Responsible_tracker == Responsible_tracker or Responsible_tracker in search_Responsible_tracker
                    assert source_information == Source_information or Source_information in source_information


    def test_request_search(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_request_num.click()
        time.sleep(1)

        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

    def test_consultation_search(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_consultation_num.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

    def test_suggestion_search(self, web_login, browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_suggestion_num.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

    def test_complaint_search(self, web_login, browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_complaint_num.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

    def test_feedback_search(self, web_login, browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_feedback_num.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

    def test_initiated_search(self, web_login, browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_initiated_num.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

    def test_all_search(self, web_login, browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span')))
        Page.search_Navigation_bar_all_num.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("")
        Page.search_button_sea_query.click()

class Test_click():
    def test_click(self,web_login,browser):
        self.driver = browser
        Page = web_main(self.driver)
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span')))
        Page.search_button_sales_management.click()
        Page.search_button_sea.click()
        time.sleep(1)
        Page.search_Iputbox_Servicenum.send_keys("HNBC2023")
        Page.search_Iputbox_Topic_introduction.send_keys("测试")
        Page.search_Iputbox_informant.send_keys("客户")
        Page.search_Iputbox_Responsible_tracker.send_keys("")
        Page.search_Iputbox_Source_information.send_keys("需求")
        Page.search_button_sea_query.click()
        time.sleep(2)
        Page.search_button_sea_clear.click()
        time.sleep(2)
        assert Page.search_Iputbox_Servicenum.text == Page.search_Iputbox_Topic_introduction.text == Page.search_Iputbox_informant.text \
        == Page.search_Iputbox_Responsible_tracker.text == Page.search_Iputbox_Source_information.text

