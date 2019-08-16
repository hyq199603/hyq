'''
def hyq (a,b,c):
    if b**2 - 4*a*c < 0:
        print('该方程没有实根')
    else:
        print('方程有两个实根')
        hyq1(a,b,c)
def hyq1 (a,b,c):
    r1 = (-b + (b**2 -4*a*c))**0.5/2*a
    r2 = (-b - (b**2 -4*a*c))**0.5/2*a
    print ('r1='r1,'r2='r2)
def start ():
    a = float(input('请输入a的值：'))
    b = float(input('请输入b的值：'))
    c = float(input('请输入c的值：'))
    hyq(a,b,c)
start()

import random
def hyq (a):
    b = (random.randint(0,100))
    c = (random.randint(0,100))
    if a == b+c:
        print('回答正确')
    else:
        print('回答错误')
def star (a):
    a = int(input('请输入一个数字'))
    hyq (a)
star('a')

def hyq (a):
    if a <= 6 and a == 0:
        print('今天是星期日')
    elif a <= 6 and a == 1:
        print('今天是星期一')
    elif a <= 6 and a == 2:
        print('今天是星期二')
    elif a <= 6 and a== 3:
        print('今天是星期三')
    elif a <= 6 and a == 4:
        print('今天是星期四')
    elif a <= 6 and a == 5:
        print('今天是星期五')
    elif a <= 6 and a == 6:
        print('今天是星期六')
    elif a %7 == 0 :
        print ('今天是星期日')
    elif a %7 == 1:
        print('今天是星期一')
    elif a %7 == 2:
        print('今天是星期二')
    elif a %7 == 3:
        print('今天是星期三')
    elif a %7 == 4:
        print('今天是星期四')
    elif a %7 == 5:
        print('今天是星期五')
    elif a %7 == 6:
        print('今天是星期六')
    hyq1(a)
def hyq1 (a):
    b = int(input('请输入到未来某天的天数'))
    if b <= 6 and a+b == 0:
        print('今天是星期日')
    elif b <= 6 and a+b == 1:
        print('今天是星期一')
    elif b <= 6 and a+b == 2:
        print('今天是星期二')
    elif b <= 6 and a+b== 3:
        print('今天是星期三')
    elif b <= 6 and a+b == 4:
        print('今天是星期四')
    elif b <= 6 and a+b == 5:
        print('今天是星期五')
    elif b <= 6 and a+b == 6:
        print('今天是星期六')
    elif abs(b-(a+b)) %7 == 0 :
        print ('那天是星期日')
    elif abs(b-(a+b)) %7 == 1:
        print('那天是星期一')
    elif abs(b-(a+b)) %7 == 2:
        print('那天是星期二')
    elif abs(b-(a+b)) %7 == 3:
        print('那天是星期三')
    elif abs(b-(a+b)) %7 == 4:
        print('那天是星期四')
    elif abs(b-(a+b)) %7 == 5:
        print('那天是星期五')
    elif abs(b-(a+b)) %7 == 6:
        print('那天是星期六')


def start (a):
    a = int(input('请输入一个数字'))
    hyq(a)
start('a')    

def hyq (a,b,c):
    d = [a,b,c]
    d.sort()
    for i in d:
        print (i)
def hyq1(a,b,c):
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    c = int(input('请输入第三个整数'))
    hyq (a,b,c)
hyq1('a','b','c')

def hyq (a,b,c,d):
    if a/b < c/d:
        print('第二种大米好')
    else:
        print('第一种大米好')
def hyq1(a,b,c,d):
    a = int(input('请输入第一种大米的重量'))
    b = int(input('请输入第一种大米的价钱'))
    c = int(input('请输入第二种大米的重量'))
    d = int(input('请输入第二种大米的价钱'))
    hyq(a,b,c,d)
hyq1('a','b','c','d') 

import calendar 
def num(year,month):
    print(calendar.monthrange(year, month)[1])
def start():
    year = int(input('Enter year: ')) 
    month = int(input('Enter month number: '))
    num(year,month)
start()

import random
def hyq (a,b):
    正面 = 0
    反面 = 1
    if a == b:
        print('正确')
    else:
        print('错误')
def hyq1 (a,b):
    b = (random.randint(0,1))
    a = str(input('正面还是反面？'))
    hyq (a,b)
hyq1 ('a','b')    

import random
def caiquan(people):
    0 == '剪刀'
    1 == '石头'
    2 == '布'
    c = random.randint(0,2)
    print(c)
    if people == c:
        print('平局')
    else:
        if C == 0 and people == 1:
            print('电脑赢了')
        elif C == 1 and people == 2:
            print('电脑赢了')
        elif C == 2 and people == 0:
            print('电脑赢了')
        else:
            print('你赢了')
def start():
    people = int(input('请你出拳：'))
    caiquan(people)
start()

def main():
    year = int(input('输入哪一年:'))
    m = int(input('输入月份1-12:'))
    d = int(input('输入月份第几天1-31:'))
    a = ['周六','周日','周一','周二','周三','周四','周五']
    if m == 1:
        m = 13
        year = year - 1
        if m ==2:
            m = 14
            year = year - 1
            h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
            day = a[h]
            print('那一天是一周中的:%s' %day)
def Start():
    main()
Start()

import random
def pai():
    shu = ["a",2,3,4,5,6,7,8,9,10,"jack","queen","king"] 
    hua = ["梅花","红桃","方块","黑桃"]
    a = random.choice(shu)
    b = random.choice(hua)
    print("这张是{}{}".format(b,a))
pai()

def hyq (a):
    bai = a//100%10
    shi = a//10%10
    ge = a%10
    if ge == bai :
        print('这个数是回文数')
    else:
        print('这个数不是回文数')
def hyq1():
    a = int(input('请输入一个三位数'))
    hyq(a)
hyq1()
''' 
def hyq (a,b,c):
    if a < c+b and b<a+c and c<a+b:
        print(a+b+c)
    else:
        print('这个输入是非法的')
def hyq1 ():
    a = int(input('三角形的第一条边是'))
    b = int(input('三角2形的第二条边是'))
    c = int(input('三角形的第三条边是'))
    hyq(a,b,c)
hyq1()