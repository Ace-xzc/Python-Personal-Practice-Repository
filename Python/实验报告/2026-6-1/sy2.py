#20255120201140 李泓毅
n = int(input("请输入数字的个数N："))
max_num = 0
for i in range(n):
    num = int(input(f"请输入第{i+1}个正整数："))
    if num > max_num:
        max_num = num
print(f"输入的{n}个数字中的最大值是：{max_num}")