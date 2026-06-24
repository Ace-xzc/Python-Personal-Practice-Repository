import random
#20255120201100 廖懋雄
d = {'数学': 101, '语文': 202, '英语': 203, '物理': 204, '生物': 206}
#keys_list = list(d.keys())
#values_list = list(d.values())
d['化学'] = 205
d['数学'] = 201
'''
print("键:", list(d.keys()))
print("值:", list(d.values()))
print("键列表:", keys_list)
print("值列表:", values_list)
print("物理的值：",d['物理'])
#del d['生物']
removed_value = d.pop('生物')
'''
remove = random.choice(list(d.keys()))
d.pop(remove)
d.clear()
print(d)


