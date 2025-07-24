year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 == 0) or ( year % 100 != 0):
    print("The given year is leap year" )
else:
    print("The given year is not a leap year :")