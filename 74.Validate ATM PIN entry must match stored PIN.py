stored_pin = 1234
ur_pin = int(input("Enter your four digit  pin"))
if ur_pin == stored_pin:
    print("ATM pin Validated")
else:
    print("Wrong pin, Try Again")