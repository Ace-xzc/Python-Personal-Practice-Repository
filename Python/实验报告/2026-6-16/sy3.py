#20255120201140 李泓毅
d = {'数学':101,'语文':202,'英语':203,'物理':204,'生物':206}
#print(d.keys())
#print(d.values())
#print(list(d.keys()))
#print(list(d.values()))
#print(d["物理"])
d["数学"] = 201
d["化学"] = 205
#del d["生物"]
d.popitem()
#d.clear()
print(d)
