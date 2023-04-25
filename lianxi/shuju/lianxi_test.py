from selenium import webdriver
import logging
import time

logging.basicConfig(level=logging.DEBUG)
# 启动浏览器驱动服务器
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)

# 点击设置
ele = driver.find_element_by_xpath('//span[@id="s-usersetting-top"]').click()
time.sleep(2)

# 点击高级搜索
driver.find_element_by_xpath('//div[@id="s-user-setting-menu"]//a[text()="高级搜索"]').click()
time.sleep(2)

# 触发下拉列表
driver.find_element_by_xpath('//span[text()="所有网页和文件"]').click()
time.sleep(2)

# 获取所有的下来列表
ele2 = driver.find_elements_by_xpath('//span[@id="adv-setting-ft"]//div[@class="c-select-dropdown-list"]/p')
for ele in ele2:
    print(ele)
    if ele.text == "所有格式":
        ele.click()
    else:
        print("不是所有格式不点击")
