# Get input from user
num = int(input("Enter a number: "))

# Step 1: Handle numbers less than or equal to 1
if num <= 1:
    print("Not a prime number")

# Step 2: Check divisibility from 2 to num - 1
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Step 3: Output result
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
