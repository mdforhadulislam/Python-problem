year = int(input("Enter your year: "))

def is_leap(year):
    leap=False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 or year % 4 != 0:
        leap=False
    elif year % 100 != 0:
        leap=True
    return leap

print(is_leap(year))


