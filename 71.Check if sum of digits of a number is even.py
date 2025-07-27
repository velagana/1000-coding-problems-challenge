num = int(input("Enter a number: "))
sum_digits = 0
temp = num

while temp > 0:
    sum_digits += temp % 10
    temp = temp // 10

if sum_digits % 2 == 0:
    print("The sum of the digits is even.")
else:
    print("The sum of the digits is odd.")
