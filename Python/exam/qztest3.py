secret_number = 7
count = 0
while True:
    guess = int(input("请输入猜测的数字："))
    count += 1
    if guess > secret_number:
        print("猜大了")
    elif guess < secret_number:
        print("猜小了")
    else:
        print("恭喜！猜对了！")
        print(f"你总共猜了 {count} 次")
        break