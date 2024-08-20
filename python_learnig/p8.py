#Program to check if the given year is a leap year or not


year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leaap year")