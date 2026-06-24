num = int(input("请输入一个三位数："))
hundred = num // 100
ten = (num // 10) % 10
unit = num % 10
print(f"百位:{hundred}")
print(f"十位:{ten}")
print(f"个位:{unit}")