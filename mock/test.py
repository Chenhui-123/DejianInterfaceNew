# encoding: utf-8
"""
@author: 周帅
@file: test.py
@time: 2019/11/4 17:12
"""

# lasttime = ''  # 设置多少未启动
# pay = False  # 设置是否有真实消费，False为没有真实消费，True为有真实消费
# lastpay = 0  # 设置多久没有进行过真实消费
# vip = False  # 设置是否是VIP，False为不是VIP，True为是VIP
# yuebing = 0  # 设置是否有阅饼余额，根据你输入的额度来筛选
# daijinquan = 0  # 设置是否有代金券余额，根据你输入的额度来筛选


# 位置参数 默认参数 *args
def vip():
    print("VIP======================")
def lasttime():
    print("lasttime======================")
def lastpay():
    print("lastpay=======================")
def pay():
    print("pay=======================")
def ff(key):
    numbers = {
            lasttime: lasttime(),
            "pay": pay(),
            "lastpay": lastpay(),
            "vip": vip(),
            "yuebing": "",
            "daijinquan": "",
    }
    # key_value= numbers.get(key)
    # print (key_value)
    numbers[key] #此处返回值需带None，否则报错
    
def func1(kwargs):
    #print(kwargs)
    # for i in kwargs:
    #     dic[i]
    #     print ("字典传值：",dic(i))
    for key in  kwargs.keys():
        print(key)
        ff(key)
        
        
           
            

data={
    lasttime:10,
    # 'lastpay':100,
    # 'vip':False,
    # 'yuebing':0
}
func1(data)


