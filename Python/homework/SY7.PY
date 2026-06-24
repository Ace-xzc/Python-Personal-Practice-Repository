#20255120201140 李泓毅
weight = 60
loss_rate = 0.002  
days = 30
for _ in range(days):
    weight *= (1 - loss_rate)
print(f"一个月后体重：{weight:.2f} 公斤")
