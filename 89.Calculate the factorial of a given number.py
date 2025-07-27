
num = int(input("Enter the factorial number you want :"))
factorial = 1
if num < 0:
    print("NOT A VALID NUMBER")
for i in range(1,num+1):
    factorial = factorial * i
    print(factorial)
