#20255120201140 李泓毅
num = int(input("请输入一个三位数的整数："))
bai = num // 100
shi = (num // 10) % 10
ge = num % 10
print(f"百位：{bai}，十位：{shi}，个位：{ge}")
