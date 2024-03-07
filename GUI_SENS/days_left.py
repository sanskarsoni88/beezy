from datetime import date

def days_until_next_test():
    today = date.today()

    today_month = int(today.month)
    today_year = int(today.year)
    today_day = today.day
   

    longer_month = [1,3,5,7,8,10,12]
    shorter_month= [4,6,9,11]

    thirty_one= longer_month.count(today_month)
    thirty = shorter_month.count(today_month)

    if thirty_one == 1:
        days = 31-today_day
    elif thirty == 1:
        days = 30-today_day
    elif today_year%4 == 0:
        days = 29-today_day
    else:
        days = 28-today_day
    
    return days

