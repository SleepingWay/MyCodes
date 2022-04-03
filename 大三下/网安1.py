import os

message = ['Amt', 'aimeite', 'alex', 'Alone', '312', '114514', 'hahaha']
symbol = "!@#$%^&*"
strR = []
f = open('D:\Pycharm\pythoncode\pythonProject1\string.txt', 'r')
for line in f.readlines():
    strR.append(line[:-1])


def textCreate(name):
    # 自动获取桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop/")
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.close()
    return full_path


def msgInput():
    print("请输入目标姓名简拼：")
    message.append(input())
    print("请输入目标姓名全拼：")
    message.append(input())
    print("请输入目标英文名：")
    message.append(input())
    print("请输入目标常用用户名：")
    message.append(input())
    print("请输入目标出生日期：")
    message.append(input())
    print("请输入目标的特殊数字：")
    message.append(input())
    print("请输入目标邮箱前缀：")
    message.append(input())


filePath = textCreate('keysDirectory')
print("生成密码字典的路径为: ", filePath)
res = open(filePath, 'w')
# msgInput()
for i in range(len(message)):
    for j in range(len(symbol)):
        for k in range(len(strR)):
            key = message[i] + symbol[j] + strR[k] + '\n'
            res.write(key)
