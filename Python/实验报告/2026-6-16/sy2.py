#20255120201140 李泓毅
districts=['越秀','荔湾','番禺','天河','海珠','南沙','白云','花都']
districts.extend(['黄埔', '从化'])
districts.insert(3, '增城')
districts.sort()
districts.remove('增城')
dis_a = districts.copy()
print(dis_a)
