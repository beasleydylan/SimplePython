#import calendar and datetime
import calendar
import datetime

def predict(date):
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[born])

# Gets user input of when their birthday is and tells them what day it will fall on
date = input('(Ex: 00 00 0000)Enter your birthday and year of when you want to know the day: ')
print(predict(date))