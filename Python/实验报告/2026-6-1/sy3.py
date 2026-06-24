#20255120201140 李泓毅
print("所有三位水仙花数：")
for num in range(100, 1000):
    hundred = num // 100
    ten = num // 10 % 10
    one = num % 10
    if hundred**3 + ten**3 + one**3 == num:
        print(num)