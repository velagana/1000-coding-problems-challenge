n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


    #0,1,1,2,3,5
   # i , i+1,i+1+1,i+3
    # i,i+1,i+2,