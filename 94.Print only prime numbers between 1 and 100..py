for num in range(2, 101):  # start from 2 up to 100
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
