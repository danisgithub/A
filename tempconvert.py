'''tempconvert
0C-32F 100C-212F
C=(F-32)/1.8
F=C*1.8+32''' 
tempstr = input('daiyoufuhaodewenduzhi:')
if tempstr[-1] in ['f','F']:
    C = (eval(tempstr[0:-1]) - 32)/1.8#[0:-1] 切片 取倒数第一位 
    print('zhuanhuanhoudewendushi{:.2F}C'.format(C))#print函数的格式化 {}表示槽，将后面fomat()的值填入，:.2f表示保留小数点后两位
elif tempstr[-1] in ['c','C']:
    F = 1.8*eval(tempstr[0:-1]) + 32
    print('zhuanhuanhoudewendushi{:.2f}F'.format(F))
else:
    print('error')
#评估函数eval() 去掉参数最外侧的引号，将字符串变为数值

