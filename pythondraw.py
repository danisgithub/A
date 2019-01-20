import turtle#库引用 函数不会重名
turtle.setup(650,350,200,200)#turtle.setup(wight,hight,startx,starty) 设置窗体的大小及位置（左上角位置）
turtle.penup()#抬起画笔，轨迹不在画布上出现
turtle.fd(-250)#海龟坐标体系，向海龟前方行进，后退250但朝向不变 运动控制函数
turtle.pendown()#画笔落下，海龟爬行，以下轨迹开始出现
turtle.pensize(25)#画笔宽度
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):#i 表示循环的次数 取值为0 , i-1 range()产生循环计数序列
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()#程序运行完后不退出，去掉即自动退出

#turtle.goto(x,y) 绝对坐标体系
#turtle.fd(d)
#turtle.bk(d)
#turtle.circle(r,extent)#根据半径r绘制exent角度的弧形 默认圆心在海龟（朝向）左侧r距离的位置上，负数为右侧，如无extent则画圆
#turtle.seth(angle)  绝对角度0/360,90,180,270）只改变方向，不行进 将海龟当前的方向改为某一绝对的角度
#turtle.left(angle) 海龟角度 当前朝向转
#turtle.right(angle)
#turtle.colormode(mode) 1.0/255
#turtle.pencolor('color')/(255,255,255)
#range(n)产生0到n-1的整数序列，共n个
#range(m,n)产生m到n-1的整数序列，共n-m个

'''from<库名>import<函数名>
from<库名>import* #之后直接调用库中的函数'''
'''from turtle import*
setup(650,350,200,200)'''

#import <库名>as<库别名>
'''import turtle as t
t.setup()'''
