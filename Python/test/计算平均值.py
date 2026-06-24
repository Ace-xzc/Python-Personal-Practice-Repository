
print ('你好，我是一个求平均值的一个程序')
total = 0
count = 0
user_input = input('请输入数字(完成所有数字的输入后，输入STOP停止):')
while user_input != 'STOP':
    number = float(user_input)
    total += number
    count += 1
    user_input = input('请输入数字(完成所有数字的输入后，输入STOP停止):')
if count == 0:
    result = 0
else:
    result = total/count
print('您输入的平均值为:' + str(result) )

