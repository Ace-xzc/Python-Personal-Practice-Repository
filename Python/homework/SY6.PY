#20255120201140 李泓毅
s = input("请输入一个由字母组成的字符串：")
upper_s = s.upper()
count_e = s.count('e')
replace_s = s.replace('e', 'abc')
print(f"全部大写：{upper_s}")
print(f"字母'e'出现的次数：{count_e}")
print(f"替换后的字符串：{replace_s}")
