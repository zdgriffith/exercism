from datetime import datetime, timedelta

def add_gigasecond(date_and_time):
    return date_and_time + timedelta(0,10**9)
