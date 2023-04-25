import json
'''读取json文件内容'''
def jsondu(path):
    with open(path, "r") as f:
        data = f.read()
    user_list = json.loads(data)
    print(user_list)
    shuju_list = []
    return shuju_list
jsondu(path = "ceshi")