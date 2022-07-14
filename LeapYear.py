#
# INPUT
# Year
#
# OUTPUT
# Is leap year?
#

def is_leap(year):
    leap = False
    
    is_4_multiple = year % 4 == 0
    is_100_multiple = year % 100 == 0 
    is_400_multiple = year % 400 == 0

    if is_4_multiple:
        if is_100_multiple:
            leap = is_400_multiple
        else: leap = True
    
    return leap

year = int(input())
print(is_leap(year))