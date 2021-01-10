# Author: Knight

'''
import sys
print(sys.path) #打印环境变量
print(sys.argv) #打印绝对路径
----------------------------------------------
import os
#cmd_res = os.system("dir") #执行命令，不保存结果
cmd_res = os.popen("dir").read()
print('-->', cmd_res)
os.mkdir("new_dir")
'''

'''
msg = '我爱北京天安门'
print(msg)
print(msg.encode(encoding = "utf-8"))
print(msg.encode(encoding = "utf-8").decode(encoding = "utf-8"))
'''

'''
names = ["DiRenJie", "LiYuanFang", "HuJingHui", "HuiWenZhong"]
namess = ["ChengYuanBa", "XiaoYuanChu", "SuXianEr"]
#names.append("ChengYuanBa") #增加
#names.append("ChengYuanBa") #增加
#names.insert(1, "XiaoYuanChu") #插入
#names[2] = "SuXianEr" #改值
#names.remove("SuXianEr") #删除
#del names[2] #删除
#del names #删除
#names.pop() #删除 默认删除最后一个
#names.pop(2) #删除
#print(names[0], names[4])
#print(names[1:2])
#print(names[1:3])
#print(names[0:3]) #切片
#print(names[-1])
#print(names[-3])
#print(names[-3:-1])
#print(names[-3:])
#names.clear() #清空列表
#print(names)
#print(names.index("HuJingHui"))
#print(names[names.index("HuJingHui")])
#print(names.count("ChengYuanBa"))
names.reverse() #反转
print(names)
names.sort() #ASCII排序（符号，数字，大写，小写）
print(names)
names.extend(namess) #扩展
print(names, namess)
'''

'''
import copy

names = ["DiRenJie", ["LiYuanFang", "ChengYuanBa"], "HuJingHui", "HuiWenZhong"]
#namesss = names.copy() #浅拷贝
#namesss = copy.copy(names) #浅拷贝
#namesss = names[:] #浅拷贝
#namesss = list(names) #浅拷贝
#namesss = copy.deepcopy(names) #深拷贝
#print(names)
#print(namesss)
#names[0] = "狄仁杰"
#names[1][1] = "程元霸"
#print(names)
#print(namesss)

print(names[0:-1:2])
print(names[::2])
print(names[:])
#range(1, 10, 2) #步长打印
for i in names:
    print(i)
'''

'''
program = ('C', 'Java') #元组不可变，只能查，又称只读列表
print(program.count('C'))
print(program.index('C'))
'''

'''
#购物车程序
product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120),
]
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):  #for item in product_list:
            print(index, item)                          #print(product_list.index(item), item)
        user_choice = input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m" %(p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print('-----------shopping list-----------')
            for p in shopping_list:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print("invalid option")
else:
    print("请输入数字！！！")
'''

'''
name = 'my name is {name}'
print(name.capitalize())  #首字母大写
print(name.count('i'))  #计数
print(name.center(50, "-"))  #美观
print(name.endswith("ie"))  #判断以某结尾
print(name.expandtabs(tabsize = 30))  #没啥用
print(name[name.find("n"):])
print(name.format(name = 'direnjie'))
print(name.format_map({'name': 'direnjie'}))
print('a1'.isalnum())  #阿拉伯字符
print('1'.isalpha())  #阿拉伯字母
print('0x10'.isdecimal())  #判断十进制
print('1'.isdigit())    #判断数字
print('1'.isidentifier())  #判断是不是一个合法的标志符
print('22'.isnumeric())  #是不是只有数字
print('My Is'.istitle())  #所有首字母是不是大写
print('My Is'.isprintable())  #tty drive不能打印
print('My Is'.isupper())  #是不是全部大写
print('+'.join(['1', '2', '3']))  #1+2+3
print(name.ljust(50, '*'))
print(name.rjust(50, '*'))
print('ABc'.lower())
print('ABc'.upper())
print(' \nABc'.lstrip())
print(' \nABc \n'.rstrip())
print('  ABc \n'.strip())
p = str.maketrans("abcdef", "1$@4#6")
print("direnjie".translate(p))
print('direnjie'.replace('e', 'E', 1))
print('direnjie'.rfind('e'))
print('1+2+3+4'.split('+'))
print('1+2\n+3+4'.splitlines())
print('DiRenJie'.swapcase())
print('di ren jie'.title())
print('di ren jie'.zfill(50))
'''

'''
info = {
    'key1': "DiRenJie",
    'key2': "HuJingHui",
    'key3': "HuiWenZhong",
}
print(info)
info['key1'] = "狄仁杰"
info['key4'] = "程元霸"
#del info
#del info['key1']
#info.pop('key1')
#info.popitem()  #随机删
print(info)
print(info.get('key5'))
print(info.get('key4'))
print('key5' in info)
'''

'''
av_catalog = {
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"
av_catalog.setdefault("大陆",{"www.baidu.com":[1,2]})  #若有则取，没有则建
print(av_catalog)
info = {
    'key1': "DiRenJie",
    'key2': "HuJingHui",
    'key3': "HuiWenZhong",
}
b = {
    'key1': "ChengWuTing",
    'key4': "XiaoYuanChu",
}
info.update(b)
print(info)
print(info.items())  #转为列表
#print(dict.formkeys([6, 7, 8], "test"))  #用不了
#print(dict.formkeys([6, 7, 8], [1, {"test": "ty"}, 444]))  #用不了
info = {
    'key1': "DiRenJie",
    'key2': "HuJingHui",
    'key3': "HuiWenZhong",
}
for i in info:  #建议使用
    print(i, info[i])
for k, v in info.items():
    print(k, v)
'''

'''
#三级菜单程序
data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}
exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t", i4)
                        choice4 = input("最后一层，按b返回>>:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
'''






