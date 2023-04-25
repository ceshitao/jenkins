import pytest
import allure
import os
import yagmail
import zipfile
'''1.result的清空'''
outcome = None
def clear_result():
    folder_path = "project_01/result"
    # 获取文件列表并删除
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)

def file_zip():
    '''文件压缩为zip'''
    # 要压缩的文件夹路径
    folder_path = "project_01/test_report"
    # 压缩后的文件名
    zip_file_name = 'report.zip'
    # 创建ZipFile对象
    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    # 遍历文件夹下的所有文件和子文件夹，并将它们添加到zip文件中
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            zip_file.write(file_path)
    # 关闭ZipFile对象
    zip_file.close()

def send_mail(recipients_mail):
    '''邮件上传'''
    yag = yagmail.SMTP(user="maituo_ceshi@163.com",password="SHMFEXHGBHWMYCTU",host="smtp.163.com")
    # '''正文'''
    contents = ["这是正文内容！！！！！！！！！！！！！！！"]
    # "发送邮件"
    yag.send(recipients_mail,"测试邮件",contents,["D:/project/report.zip"])

if __name__ == '__main__':
    clear_result()
    '''函数执行生成allure报告'''
    pytest.main(['-n 4','--reruns=2 ', 'project_01/test_dir/test_sales_management.py','--alluredir', "./project_01./result"])
    #pytest.main(['-n 5', '--reruns=2 ', 'project_01/test_dir/test_sales_management.py', 'project_01/test_dir/test_login.py','--alluredir', "./project_01./result"])
    #os.system("allure generate ./project_01./result -o ./project_01./test_report --clean")
    file_zip()
    # send_mail("2597115793@qq.com")

