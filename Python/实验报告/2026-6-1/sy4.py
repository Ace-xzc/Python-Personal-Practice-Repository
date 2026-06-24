#20255120201140 李泓毅
prime_list = []
for num in range(2, 100):
    flag = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            flag = False
            break
    if flag:
        prime_list.append(str(num))
print("100以内的素数有:")
print(','.join(prime_list) + ',')