'''
import csv
import json
hyq = 'C:\\Users\\Administrator\\Desktop\\Python\HomeWork3\\wenjian\\dashuju.csv'
hyq1 = csv.reader(open (hyq,'r',encoding = 'utf8'))
for i in hyq1:
    print(hyq1)
第一题
a = 0
c = 0
while c >= 0:
    b = float(input('输入值'))
    if b == 0:
        print(a / c)
        break     
    while b != 0:
        a += b
        c += 1
        print(a)
        break
第三题
a = 0
c = 0
d = 0
f = 0
while c >= 0:
    b = float(input('输入值'))
    if b > 0:
        d += 1
    if b < 0: 
        f += 1 
    if b == 0:
        print(a / c) 
        print('正数的个数为'+str(d))
        print('负数的个数为'+str(f))
        break     
    while b != 0:
        a += b
        c += 1
        print(a)
        break
 第五题
a = 0
while a**2<12000:
    a += 1
    print (a)

a = 200
while a**3 >12000:
    a -=1
    print(a)
第七题
a = 0
n = 0 
while n >= 0:
    n +=1
    a += 1/n
    if n == 50000:
        print(a)
        break
a = 0
n = 50001 
while n <= 50001:
    n -=1
    a += 1/n
    if n == 1:
        print(a)
        break
第四题
t = 0
for i in range(100,1000):
    if i % 5 == 0 and i % 6 == 0:
        print(i,end = ' ')
        t += 1
        if t % 10 == 0:
            print("\n")
第八题
a = 1
b = 3
c = 0
while a >=1:
    c += a/b
    a += 2
    b += 2
    if a > 97:
        print(c)
        break
第二题
a = [10000]
for i in range(10):    
    x = a[i] * 1.05    
    a.append(x)
print("十年后的学费：%.2f"%a[10])
print("现在及十年后的学费：%.2f"%sum(a))
第九题
i = 1
π = 0
while i >0:
    b = 4*((-1)**(i+1)/(2*i-1))
    i += 1
    π += b
    if i %10000==0:
        print(π)
    elif i >100000:
        break
第十一题
sum = 0
for i in range(1,8):
    for j in range(1,8):
        if i != j:
            print(i,j)
            sum += 1
print(sum)
第十二题
a = int(input('请输入第一个数字'))
b = int(input('请输入第二个数字'))
c = int(input('请输入第三个数字'))
d = int(input('请输入第四个数字'))
e = int(input('请输入第五个数字'))
f = int(input('请输入第六个数字'))
g = int(input('请输入第七个数字'))
h = int(input('请输入第八个数字'))
i = int(input('请输入第九个数字'))
j = int(input('请输入第十个数字'))
n = (a+b+c+d+e+f+g+h+i+j)/10
print('平均数'+str(n))
标准方差 = (((a-n)**2+(b-n)**2+(c-n)**2+(d-n)**2+(e-n)**2+(f-n)**2+(g-n)**2+(h-n)**2+(i-n)**2+(j-n)**2)/n)**0.5
print ('标准方差：'+str(标准方差))
第十题
'''
def p_number(n):
    count = 0
    for i in range(1,n):
        if n % i ==0:
            count += i
    if n == count:
        return True
    return False

for i in range(1,10001):
    if p_number(i):
        print("10000内的完全数：%d"%i)