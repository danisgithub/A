#tempconvert
#0C-32F 100C-212F
#C=(F-32)/1.8
#F=C*1.8+32
tempstr = input('daiyoufuhaodewenduzhi:')
if tempstr[-1] in ['f','F']:
    C = (eval(tempstr[0:-1]) - 32)/1.8
    print('zhuanhuanhoudewendushi{:.2F}C'.format(C))
elif tempstr[-1] in ['c','C']:
    F = 1.8*eval(tempstr[0:-1]) + 32
    print('zhuanhuanhoudewendushi{:.2f}F'.format(F))
else:
    print('error')
