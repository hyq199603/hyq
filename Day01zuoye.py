'''
Celsius = int(input('摄氏温度'))
fahrenheit = (9/5) * Celsius +32
print ('华氏温度'+fahrenheit)

import math
radius = int(input('半径'))
length = int(input('高'))
area = 2 * radius * math.pi
print (area)
volume = area * length
print (volume)

feet = float(input('英尺:'))
merters = feet / 3.279
print(str(feet) +'英尺'+'是'+str(merters)+'米')

M = int(input('多少千克的水？')) 
initialtemperature = int(input('起始温度为:'))
finaltemperature = int(input('最终温度为:'))
Q = M * (finaltemperature - initialtemperature) * 4184
print ('加热所需的能量为'+ str(Q))

C = float(input('差额是:'))
N = float(input('年利率是:'))
LX = C / (N / 1200)
print ('下月月供的利息是:' + str(LX))

V0 = int(input('起始速度为:'))
V1 = int(input('末速度为:'))
t = int(input('所用时间为:'))
a = (V1 - V0)/t
print ('平均加速度为:'+ str(a))

a = int(input('每月存钱:'))
b = float(input('年利率为:'))
c = b / 12
d = a * (1 + c)
i = (a + d) * (1 + c)
f = (a + i) * (1 + c)
g = (a + f) * (1 + c)
h = (a + g) * (1 + c)
j = (a + h) * (1 + c)
print (j)

num = int(input('请输入一个数字'))
bai = num//100%10
shi = num//10%10
ge = num%10
s = (ge + shi + bai)
print (s)
'''
import random 
a = 0
for i in range(4):
    账号 = '1518844536@qq.com'
    密码 = '123456'
    zh = str(input('请输入账号:'))
    if '@qq.com' not in zh:
        print('账号格式不正确')
        input('请重新输入账号')
    mm = str(input('请输入密码'))
    if 账号 == zh and 密码 == mm:
        print('登录成功')
        break
    else:
        print('账号或者密码错误') 
    for j in range(10):
        b = (random.randint(1000,9999))
        print(b)
        c = eval(input('请输入验证码'))
        if c == b:
            print('验证码正确')
            break 
        elif b != c:
            print('验证码错误')
            c = eval(input('请再次输入')) 
    a += 1   
    if a > 3:
        print('账号已锁定')
        