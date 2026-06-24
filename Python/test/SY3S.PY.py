##宋子烨20255120210003
num = int(input("请输入一个十进制整数: "))
bin_str = bin(num)[2:]
oct_str = oct(num)[2:]
hex_str = hex(num)[2:]
print(f"二进制: {bin_str}")
print(f"八进制: {oct_str}")
print(f"十六进制: {hex_str}")