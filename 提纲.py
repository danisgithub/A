#Python练习
#print
print ('1024 * 768 =', 1024*786)

#变量赋值与input
name = input('your name:')
print ('hello',name)

#list and  tuple
group = [1,2,3]    #可修改
num = (1,2,3)    #不可修改

#条件判断    if elif else
if    :
    print（）
else    :
    print（）
else:
    print（）    
	
#循环
#for in 循环
name = ['one','two','three']
for x in name:
    print(x)
	
sum = 0    #100累加
for x in rang(101):
    sum = sum + x
print (sum)
    
#while循环
n = 1    
while n <= 100:    #输出1-100
    print(n)
    n = n + 1
print('end')

#break停止，需借助if条件判断
n = 1
while n <= 100:
    if n > 10: 
        break
    print(n)
    n = n + 1
print('end')

#continue跳过循环
n = 0
while n < 10:
    n = n + 1
    if n%2 = 0:    #n/2的余数为0，也就是偶数
    continue
print(n)    #此程序输出10以内的奇数

#{}
#dict    dictionary字典
#其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'one':1,'two':2,'three':3}
d['a'] = 4    #直接插入
'b' in d    #查看b是否存在于d，返回布尔值
d.pop('a')    #删除，pop()
#set可以看成数学意义上的无序和无重复元素的集合，借助list
s = set([1,2,3,4])
s.add(5)
s.remove(5)

#函数
#https://docs.python.org/3/library/functions.html
a = abs    #变量a指向abs函数
#定义函数
def jdz(a):
    if a >= 0:
	    return a
	else:
	    return -a

#空函数
def none():
    pass    #pass可用来占位，让程序先运行

#数据类型检查函数isinstance()
if not isinstance(x, (int, float)):    
    raise XXXXXXXXX    #如果x的类型不是整数或浮点数，则报错

#导入math包，可以使用sin cos
import math

#从一个点到另一个点 xy坐标，位移，角度
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x,y = move()
print(x,y)
