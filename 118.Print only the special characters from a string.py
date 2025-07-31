str = input("Enter the string")
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
n ='0123456789'
for i in str:
    if i not in s and n:
        print(i)

