'''
第一题
def hyq ():
    n = 1
    t = 0
    for i in range(100):
        i = n*(3*n-1)/2
        n += 1
        print(i,end = ' ')
        t += 1
        if t %10 ==0:
            print('\n')
hyq()
第二题
def hyq (a):
    bai = a//100%10
    shi = a//10%10
    ge = a%10
    print(bai+shi+ge)
def hyq1():
    a = int(input('请输入一个百位数'))
    hyq(a)
hyq1()
第三题
def hyq (a):
    sorted(a)
    print(a)
def hyq1():
    a = []
    for i in range(3):
        i = int(input('num'))
        a.append(i)
    hyq(a)
hyq1()
第四题
from prettytable import PrettyTable
list = []
def futureInvestmentValue(inAmount,rate,years):
    for i in range(1,years + 1):
        futureInvestment = inAmount + ((1 +rate) ** (12 * i))
        list.append([i,futureInvestment])
        table = PrettyTable(['year','Future Value'])
    for row in list:
        table.add_row(row)
        print(table)
if __name__ == "__main__":
    inAmount = int(input("请输入投资额："))
    rate = float(input("请输入百分比格式的年利率：")) / 12
    futureInvestmentValue(inAmount,rate,years = 30)
第五题
def printChars(ch1,ch2,numberPerLine):
    count = 0
    for i in range (ch1,ch2):
        numberPerLine = chr(i)
        count +=1
        print(numberPerLine,end = " ")
        if count % 10 ==0:
            print("\n")

if __name__ == '__main__':
    ch1 = 73
    ch2 = 91
    numberPerLine = ""
    printChars(ch1,ch2,numberPerLine)
第六题
def numberOfDaysInAYear(year):
    print("Years","\t","Days")
    for year in range(2010,2021):
        if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
            print(year,"\t",366) 
        else:
            print(year,"\t",365)

if __name__ == '__main__':
    year = 0
    numberOfDaysInAYear(year)
第七题
def distance(x1,y1,x2,y2):
    dis = ((x1-x2)**2+(y1-y2)**2)**0.5
    print(dis)

if __name__ == '__main__':
    x1,y1 = eval(input("x1,y1："))
    x2,y2 = eval(input("x2,y2："))
    distance(x1,y1,x2,y2)
第八题
def sushu():
    i = 2
    c = []
    d = []
    while i <=31:
        j = 2
        while j <= i:
            if i % j ==0:
                if i == j:
                    c.append(i)
                break
            j += 1
        i += 1
    print(c) 
    for x in c:
        sushu = 2 ** x - 1
        d.append(sushu)
    print(d) 
          
if __name__ == '__main__':
    sushu()

import time
a = time.time()
第十题
import random
def hyq(x):
    b = 0
    while b == 0:
        i = random.randint(1,6)    
        j = random.randint(1,6)
        y = i + j
        print(y)
        if y == x:
            print('你赢了')
            break
        elif y == 7:
            print('你输了')
            break
def hyq1():
    a = 0
    while a== 0:
        i = random.randint(1,6)    
        j = random.randint(1,6)    
        x = i+j    
        print(x)
        if x == 3 or x == 12 or x == 2:        
            print("你赢了！")
            break   
        elif x == 7 or x == 11:        
            print("你输了！")
            break         
        else:
            hyq(x)
hyq1()
'''