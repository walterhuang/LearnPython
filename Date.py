from datetime import datetime, timedelta

current_date = datetime.now()

print('Today is: ' + str(current_date))

today = datetime.now()
print('Today is: ' + str(today))

# You can use timedelta to add or remove days, or weeks to a date
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

#######

birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d%m%Y')
print('Birthday: ' + str(birthday_date))