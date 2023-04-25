from poium import Page, Element


class web_main(Page):
    '''按钮'''
    search_button_commonly_used_function = Element(xpath='/html/body/div[3]/div[1]/div[2]/div[1]/div/ul/div[1]/li/div/span', describe="常用功能")
    search_button_sales_management = Element(xpath='//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/div/span', describe="销售管理")
    search_button_sea = Element(xpath='//*[@id="app_menu"]/div[2]/div[1]/div/ul/div[3]/li/ul/li[1]/span', describe="海纳百川")
    search_button_sea_clear = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[1]/span', describe='清除')
    search_button_sea_query = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[2]/span', describe='查询')
    search_button_sea_add = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[3]/span', describe="新增")
    search_button_sea_modify = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[6]/button[4]/span', describe="修改")
    search_refresh = Element(xpath='//*[@id="app_head"]/div[2]/div[2]/div[1]/dl/dt/i', describe="刷新")
    '''导航栏（Navigation_bar）'''
    search_Navigation_bar_incomplete_num = Element(id_='tab-未完成', describe="未完成")
    search_Navigation_bar_request_num = Element(id_='tab-需求', describe="需求")
    search_Navigation_bar_consultation_num = Element(id_='tab-咨询', describe="咨询")
    search_Navigation_bar_suggestion_num = Element(id_='tab-建议', describe="建议")
    search_Navigation_bar_complaint_num = Element(id_='tab-投诉', describe="投诉")
    search_Navigation_bar_feedback_num = Element(id_='tab-反馈', describe="反馈")
    search_Navigation_bar_initiated_num = Element(id_='tab-我发起的', describe="我发起的")
    search_Navigation_bar_all_num = Element(id_='tab-全部', describe="全部")
    search_Navigation_bar_last_num = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/span[1]', describe="最下方的数量")
    '''最下方的页码切换'''
    search_pagenumber_num = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[2]/ul/li[last()]',describe="页码号")
    search_serial_number_num = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[last()]/td[1]/div/span', describe="序号")
    '''输入框（Input box）'''
    search_Iputbox_Servicenum = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[1]/div/div/input', describe="业务编号")
    search_Iputbox_Topic_introduction = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[2]/div/div/input', describe="请输入主题简介")
    search_Iputbox_informant = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[3]/div/div/input', describe="请输入上报人")
    search_Iputbox_Responsible_tracker = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[4]/div/div/input', describe="请输入负责跟踪人")
    search_Iputbox_Source_information = Element(xpath='//*[@id="haiNaBaiChuan"]/div[2]/div[1]/form/div[5]/div/div/input', describe="请输入来源信息")

    '''种类下拉内容'''
    search_button_kinds_list = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[1]/div/div/div/span', describe="种类列表")
    search_button_request = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[1]", describe="需求")
    search_button_suggest = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[2]", describe="建议")
    search_button_complaint = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[3]", describe="投诉")
    search_button_feedback = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[4]", describe="反馈")
    search_button_consult = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[5]", describe="咨询")

    '''来源下拉内容'''
    search_button_source_list = Element(
        xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[1]/div[1]/div/div[2]/div/div/div/span',
        describe="来源列表")
    search_button_client = Element(xpath='/html/body/div[last()]/div[1]/div[1]/ul/li[1]', describe="客户")
    search_button_partner = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[2]", describe="合作伙伴")
    search_button_staff = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[3]", describe="员工")
    search_button_exhibition = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[4]", describe="展会")
    search_button_others = Element(xpath="/html/body/div[last()]/div[1]/div[1]/ul/li[5]", describe="其他")
    '''上报人下拉内容'''
    search_button_reporter_list = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[3]/div[1]/div/div/div/div/input', describe="上报人列表")
    search_button_reporter = Element(xpath='/html/body/div[last()]/div[1]/div[1]/ul/li[210]/span', describe="上报人")
    '''跟踪人下拉内容'''
    search_button_follower_list = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[3]/div[3]/div/div/div/div/input')
    search_button_follower = Element(xpath='/html/body/div[last()]/div[1]/div[1]/ul/li[210]', describe='跟踪人')

    '''来源信息'''
    search_text_Source_information = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[1]/div[2]/div/div/div/input', describe='来源信息')
    '''联系人'''
    search_text_Contact_linkman = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div/input', describe='联系人')
    '''联系人电话'''
    search_text_Contact_phone = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/input', describe='联系人电话')
    '''上报人电话'''
    search_text_reporter_phone = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div/input', describe='上报人电话')
    '''主题简介'''
    search_text_Topic_introduction = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[4]/div[1]/div[1]/div/div/input', describe='主题简介')
    '''备注'''
    search_text_Remark = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[4]/div[2]/div/div/div/textarea', describe='备注')
    '''等级选择'''
    search_text_five = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/label[1]/span[1]/span', describe="五星")
    search_text_four = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/label[2]/span[1]/span', describe="四星")
    search_text_three = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/label[3]/span[1]/span', describe="三星")
    search_text_two = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/label[4]/span[1]/span', describe="二星")
    search_text_one = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/label[5]/span[1]/span', describe="一星")
    '''负责人联系电话'''
    search_text_Responsible_phone = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[3]/div[4]/div/div/div/input', describe='负责人联系电话')
    '''详情内容输入'''
    search_text_send = Element(xpath='/html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/form/div[4]/div[3]/div/div/div/div[2]/div[1]/p')
    '''保存和取消'''
    search_button_save = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[3]/span/button[2]/span', describe='保存')
    search_button_cancel = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[3]/span/button[1]', describe='取消')
    '''上传文件'''
    search_text_upload_images = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[4]/div[1]/div[2]/div[1]/div/div/div/input', describe='图片')
    search_text_upload_texts = Element(xpath='//*[@id="haiNaBaiChuan"]/div[3]/div/div[2]/form/div[4]/div[1]/div[2]/div[2]/div/div/div/input', describe='文件')
    "-------------------------------------------------------------------"
    ''''''
