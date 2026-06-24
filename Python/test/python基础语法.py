import math
from email.header import Header

print ('hello world')
print ('你好世界')
print ('1+1=2')
a = 'Hello world '
b = '1+1=2'
c = '你好世界'
d = 'I like playing PUBG'
print (a+d)

import keyword
print (keyword.kwlist)
Xzc = ('新手')
A = ('我是')
print (A+Xzc)
#print的用法
print('Dad!!!')
print ('Hello'+' dad'+' !!!')
print ('Hello "你好"')
print ("我是第一行\n我是第二行")
print ('let\'s go')
print ('''将进酒
作者：李白

　　君不见，黄河之水天上来，奔流到海不复回。
　　君不见，高堂明镜悲白发，朝如青丝暮成雪！
　　人生得意须尽欢，莫使金樽空对月。
　　天生我材必有用，千金散尽还复来。
　　烹羊宰牛且为乐，会须一饮三百杯。
　　岑夫子，丹丘生，将进酒，杯莫停。
　　与君歌一曲，请君为我倾耳听。
　　钟鼓馔玉不足贵，但愿长醉不复醒。
　　古来圣贤皆寂寞，惟有饮者留其名。
　　陈王昔时宴平乐，斗酒十千恣欢谑。
　　主人何为言少钱，径须沽取对君酌。
　　五花马、千金裘，呼儿将出换美酒，与尔同销万古愁！''')
#变量的用法
greet = ('您好，您吃了吗？')
print (greet + ' 王一')
my_love = ('13719945352')
my_ex = my_love
print (my_ex)
my_love = ('20060628')
print (my_love)
greet = ('hello world')
greet_english = greet
greet_chines = ('你好世界')
print (greet)
print (greet_chines)

#计算
#-x**2-2x+3=0
a = -1
b = -2
c = 3
result1 = ((-b + math.sqrt (b ** 2 - 4 * a * c)) /(2 * a))
result2 = ((-b - math.sqrt (b ** 2 - 4 * a * c)) /(2 * a))
print (result1)
print (result2)
#对字符串求长度
print (len ('Hello world'))
#通过索引获取单个字符串的长度
print ('HELLO WORLD'[4])
print ('Hello world'[len ('Hello world') -1])
#布尔类型
b1= True
b2= False
#空值类型
n = None
#type函数
print (type(a))
print (type(n))
print (type(b1))
#列表的使用
shopping_list = []
shopping_list.append('键盘')
shopping_list.append('音响')
shopping_list.append('电竟椅')
shopping_list.append('键帽')
shopping_list.remove('键盘')
print(shopping_list)
print(len(shopping_list))
print(shopping_list[1])
shopping_list[1] = '硬盘'
print(shopping_list)
price = [200, 799, 1024, 220]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(sorted_price)
print(max_price)
print(min_price)

