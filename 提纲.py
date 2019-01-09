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

#break    停止，需借助if条件判断
n = 1
while n <= 100:
    if n > 10: 
        break
    print(n)
    n = n + 1
print('end')

#continue    跳过循环
n = 0
while n < 10:
    n = n + 1
    if n%2 = 0:    #n/2的余数为0，也就是偶数
    continue
print(n)    #此程序输出10以内的奇数

#dict    dictionary字典

