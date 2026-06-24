#BMI=体重/身高**2
user_weight = float(input('请输入你的体重(单位kg):'))
user_high = float(input('请输入你的身高(单位m):'))
user_BMI = user_weight / user_high ** 2
print (user_BMI)
if user_BMI >= 30:
    print ('你太胖了，该减肥了。')
elif user_BMI >= 18.5 and user_BMI <= 25:
    print('你很健康继续保持')
elif 25 <= user_BMI  <= 30:
    print('你有点胖有肥胖风险')
else:
    print('你太瘦了，你要多吃一')
data = input('请问您是否同意将数据上传云端：')
if data == '同意':
    print('上传成功，谢谢您的参与。')
else:
    print('谢谢您使用该程序')

#心情指数
mood_index = int(input('心情指数:'))
if mood_index >= 50:
    print('今晚能够打游戏')
    print('happy!!!')
else:  # mood_index < 50
    print('今晚不能打游戏')