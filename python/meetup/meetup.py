from datetime import date

def is_leap_year(year):
    if year%400 == 0:
        return True
    elif year%4 == 0 and not year%100 == 0:
        return True
    else:
        return False

def meetup_day(year, month, weekday, descriptor):
    leap = is_leap_year(int(year))

    day_dict = {'monday':0,
                'tuesday':1, 'wednesday':2,
                'thursday':3, 'friday':4,
                'saturday':5, 'sunday':6}
    if leap:
        days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
   
    weekday_as_int = day_dict[weekday.lower()]
    max_day        = days_in_month[month-1]

    count = 0 
    for day in range(1,max_day+1):
        weekday = date(year,month,day).weekday()

        if weekday_as_int == weekday:
            count += 1 
            if descriptor =='teenth' and day>12 and day < 20:
                return date(year,month,day)

            if descriptor =='last' and (max_day-day)<7:
                return date(year,month,day)
                
        if descriptor[0].isdigit():
            if int(descriptor[0]) == count:
                return date(year,month,day)

    # If criterion is never met, raise error
    raise ValueError("This day doesn't exist!")
