# from poium import Page, Element
# class BaiduPage(Page):
#     search_input = Element(id_="kw")
#     search_button = Element(id_="su")
# '''参数id必须为 “id_"'''
from poium import Page,Element
class login_page(Page):
        search_input_username = Element(id_="username",describe="用户名")
        search_input_password = Element(id_="password",describe="密码")
        search_button_login = Element(id_="login_submit",describe="登录")
        search_name_error = Element(xpath='//*[@id="error"]', describe="第N次输入错误")

        search_button_commonly_used_function = Element(xpath='/html/body/div[3]/div[1]/div[2]/div[1]/div/ul/div[1]/li/div/span',describe="常用功能")
        search_button_sales_management = Element(xpath='//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span',describe="销售管理")
        search_button_sea = Element(xpath='//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/ul/li/span',describe="海纳百川")
        search_button_sea_add = Element(xpath ='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/button[3]',describe="新增")
