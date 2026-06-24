#20255120201114 罗灏
districts = ['越秀', '荔湾', '番禺', '天河', '海珠', '南沙', '白云', '花都']
districts.extend(['黄埔', '从化'])
districts.insert(3, '增城')
districts.sort()
districts.remove('增城')
dis_a = list(districts)
dis_a_tuple = tuple(dis_a)
print(dis_a_tuple)